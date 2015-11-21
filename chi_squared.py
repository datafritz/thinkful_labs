import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

chi, p = stats.chisquare(freq.values())

print chi

print p
