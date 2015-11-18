import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace = True)

loansData.boxplot(column = 'Amount.Requested')
plt.savefig("boxplot_request.jpg")

plt.figure()
loansData.hist(column = 'Amount.Requested')
plt.savefig("hist_request.jpg")

plt.figure()
qq_graph = stats.probplot(loansData['Amount.Requested'],dist = 'norm', plot = plt)
plt.savefig("qq_plot_request.jpg")
