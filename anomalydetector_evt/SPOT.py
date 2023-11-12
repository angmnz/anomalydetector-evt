import numpy as np
from .utils.pot import calc_t, calc_zq, POT
from .utils.grimshaw import grimshaw 

class SPOT:

    """Clase para detección de anomalías en streaming data con EVT."""

    def __init__(self, data, p, q):

        self.data = data
        self.p = p # percentil para definir peaks
        self.q = q # probabilidad para anomalia
        self.n = data.size
        self.Y = np.array([]) # para almacenar peaks
        self.A = np.array([]) # para almacenar anomalias

    def init(self):
        self.zq, self.t, Yn = POT(self.data, self.p, self.q)
        self.Y = np.concatenate((self.Y, Yn))
        self.Nt = len(self.Y)
    
    def update(self, new_value):

        if new_value > self.zq:

            self.A = np.append(self.A, new_value)
            
            return True

        elif new_value > self.t:

            new_Y = new_value - self.t
            self.Y = np.append(self.Y, new_Y)

            self.Nt += 1
            self.n += 1

            gamma, sigma = grimshaw(self.Y)

            self.t = calc_t(self.data, self.p)
            self.zq = calc_zq(self.q, gamma, sigma, self.n, self.Nt, self.t)

            return False
        else:

            self.n += 1

            return False

