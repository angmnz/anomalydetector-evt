import numpy as np
from .utils.pot import calc_t, calc_zq, POT
from .utils.grimshaw import grimshaw

class DSPOT:

    """Clase para detección de anomalías en streaming data con drift."""

    def __init__(self, data, p, q, d):

        self.data = data
        self.p = p # percentil para definir peaks
        self.q = q # probabilidad para anomalia
        self.d = d # depth
        self.n = data.size
        self.Y = np.array([]) # para almacenar peaks
        self.A = np.array([]) # para almacenar anomalias
        self.Xnormalized = np.array([])

    def init(self):

        self.W = self.data[:self.d] # d valores normales
        self.M = self.W.mean() # promedio de los valores normales

        
        for i in range(self.d + 1, self.n - self.d):
            Xi_normalized = self.data[i] - self.M
            self.Xnormalized = np.append(self.Xnormalized, Xi_normalized)
            self.W = np.append(self.W[1:], self.data[i])
            self.M = self.W.mean()

        self.zq, self.t, Yn = POT(self.Xnormalized, self.p, self.q)
        self.Y = np.concatenate((self.Y, Yn))
        self.Nt = len(self.Y)
    
    def update(self, new_value):
        Xi_normalized = new_value - self.M

        if Xi_normalized > self.zq:

            self.A = np.append(self.A, new_value)
            
            return True

        elif Xi_normalized > self.t:

            new_Y = Xi_normalized - self.t
            self.Y = np.append(self.Y, new_Y)

            self.Nt += 1
            self.n += 1

            gamma, sigma = grimshaw(self.Y)

            self.t = calc_t(self.Xnormalized, self.p)
            self.zq = calc_zq(self.q, gamma, sigma, self.n, self.Nt, self.t)
            
            self.W = np.append(self.W[1:], new_value)
            self.M = self.W.mean() 

            return False
        
        else:
            self.n += 1
            self.W = np.append(self.W[1:], new_value)
            self.M = self.W.mean() 

            return False