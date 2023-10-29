import numpy as np
from .grimshaw import grimshaw

def calc_zq(q, gamma, sigma, n, Nt, t):

    zq = t + (sigma / gamma) * ((q * n/Nt)**(-gamma) - 1)

    return zq

def POT(data, q):

    """
    Funcion para la calibracion inicial del cuantil zq tal que  P(X>zq)<q.
    """

    # Calcular el umbral inicial
    t = np.sort(data)[int(q * data.size)]

    # Calcular los excesos X_i - t (peaks)
    peaks = data[data > t] - t

    # Ajustar una distribución pareto generalizada a los excesos
    gamma, sigma = grimshaw(peaks)

    # Calcular el cuantil
    n = len(data) # total de observaciones
    Nt = len(peaks) # total de excesos

    zq = calc_zq(q, gamma, sigma, n, Nt, t)

    return zq, t
