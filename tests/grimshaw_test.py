import random
from utils import *

initial_level = 0.98
data = random.normal(0, 1, 50)
t = np.sort(data)[int(init_level * data.size)]
peaks = data[data>t] - t
num_candidates = 10
epsilon = 10e-8

gamma, sigma = grimshaw(peaks, t, num_candidates, epsilon) 
print(gamma, sigma)
