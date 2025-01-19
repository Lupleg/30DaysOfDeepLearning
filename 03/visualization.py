import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np
import pandas as pd

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Matplotlib line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot using Matplotlib')
plt.legend()
plt.show()