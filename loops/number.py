import random
from matplotlib import pyplot as plt

# Add your code below:
numbers_a = range(1, 13)
numbers_b = [random.randint(1, 1000) for i in range(12)]
plt.plot(numbers_a, numbers_b)
plt.show()