import numpy as np
from scipy.optimize import brentq

def u(x, peaks):

    """Funcion para el método de grimshaw"""
    
    s = 1 + x * peaks
    return np.mean(s)

def v(x, peaks):

    """Función para el método de grimshaw"""
    
    s = 1 + x * peaks
    return 1 + np.mean(np.log(s))

def f(x, peaks):

    """Funcion para encontrar las soluciones"""
    
    s = 1 + x * peaks
    u = np.mean(1 / s)
    v = 1 + np.mean(np.log(s))

    return u * v - 1

def loglikehood(peaks, gamma, sigma):

    """Funcion de logverosimilitud de DPG a maximizar"""

    N = len(peaks)
    s = 1 + (gamma/sigma) * peaks
    llh = - N * np.log(sigma) - (1 + 1/gamma) * np.sum(s)

    return llh

def grimshaw(peaks:np.array):

    """Funcion que implimenta el método de Grimshaw para encontrar las 
    soluciones gamma y sigma de la distribución Pareto Generalizada desde
    una ecuación de una variable.

    Retorna gamma, sigma que minimizan la función de verosimilitud."""

    # Vector para almacenar las soluciones
    vec_roots = [] 

    # Valores para calcular los intervalos donde se buscarán las soluciones
    peaks_min = peaks.min()
    peaks_max = peaks.max()
    peaks_mean = peaks.mean()
    epsilon = min(1e-9, 0.5/peaks_max)

    # Intervalo izquierdo
    ai = -1 / peaks_max + epsilon
    bi = -epsilon

    # Intervalo derecho
    ad = epsilon
    bd = 2 * (peaks_mean - peaks_min) / (peaks_min**2)

    gamma, sigma = False, False

    try:
        vec_roots.append(brentq(f, ai, bi, args=peaks))

    except ValueError as e:
        None

    # Buscar raíces en el intervalo derecho
    try:
        vec_roots.append(brentq(f, ad, bd, args=peaks))

    except ValueError as e:
        None     

    llh = -10e10
    for root in vec_roots:

        gamma_ = v(root, peaks) - 1
        sigma_ = gamma_/root

        llh2 = loglikehood(peaks, gamma_, sigma_)

        if llh2 > llh:
            gamma = gamma_
            sigma = sigma_
            llh = llh2
    
    return gamma, sigma
