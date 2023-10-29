import numpy as np
from anomalydetector_evt.utils.grimshaw2 import *
import matplotlib.pyplot as plt
from scipy.stats import pareto

init_level = 0.98
data = np.random.normal(0, 1, 2000)
t = np.sort(data)[int(init_level * data.size)]
peaks = data[data>t] - t
print(peaks)
num_candidates = 10
epsilon = 10e-8

gamma, sigma = grimshaw(peaks, t, num_candidates, epsilon)
print(gamma, sigma)
exit()
# Generar datos de la distribución Pareto generalizada
num_samples = 1000
data = pareto.rvs(b=gamma, scale=sigma, size=num_samples)

# Crear un rango de valores para el eje x
x = np.linspace(pareto.ppf(0.01, b=gamma, scale=sigma), pareto.ppf(0.99, b=gamma, scale=sigma), 100)

# Calcular la función de densidad de probabilidad (PDF)
pdf = pareto.pdf(x, b=gamma, scale=sigma)

# Graficar la distribución Pareto generalizada
plt.plot(x, pdf, 'r-', lw=2, label='PDF')
plt.hist(data, density=True, alpha=0.5, bins=20, label='Histograma de datos')
plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.title('Distribución Pareto Generalizada')
plt.show() 
