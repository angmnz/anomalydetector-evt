import numpy as np
from .grimshaw import grimshaw

def calc_zq(q, gamma, sigma, n, Nt, t):

    zq = t + (sigma / gamma) * ((q * n/Nt)**(-gamma) - 1)

    return zq

def calc_t(data, p=0.98):

    return np.sort(data)[int(p * data.size)]

def POT(data, p, q):

    """
    Funcion para la calibracion inicial del cuantil zq tal que  P(X>zq)<q.
    """

    gamma, sigma = False, False

    # Ajustar una distribución pareto generalizada a los excesos
    i = 0
    while not (gamma and sigma):
   
        # Calcular el umbral
        t = calc_t(data, p-i)

        # Calcular los excesos X_i - t (peaks)
        peaks = data[data > t] - t

        gamma, sigma = grimshaw(peaks)

        i += 0.1


    # Calcular el cuantil
    n = len(data) # total de observaciones
    Nt = len(peaks) # total de excesos

    zq = calc_zq(q, gamma, sigma, n, Nt, t)

    return zq, t, peaks
