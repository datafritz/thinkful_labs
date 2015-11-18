import matplotlib.pyplot as plt
from scipy import stats as stats
import numpy as np
# The dataset

x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4,\
4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9])

# gets the frequency of the array
freq_out = stats.itemfreq(x)

#outputs graphs to file
boxplot = plt.boxplot(x)
plt.savefig("boxplot.jpg")

plt.figure()
histogram = plt.hist(x, histtype = 'bar')
plt.savefig("histogram.jpg")

plt.figure()
qq_plot = stats.probplot(x, dist = 'norm', plot = plt)
plt.savefig("qq_plot.jpg")

#Prints the frequency
print freq_out
