import pandas as pd
from scipy.stats import mode

# Dataset for DataFrame
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# Split the docstring into a list of strings
data = data.splitlines()
# List conprehention to convert a list of strings into list of list
# of strings
data = [i.split(',') for i in data]

# Converting list into a pandas DataFrame
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = column_names)

# Convert the array to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#build out functions to get discriptive statistics for Alcohol and Tobacco

def get_mode(mode_array):
    in_mode = mode(mode_array).mode[0]
    return in_mode

def get_mean(mean_array):
    in_mean = mean_array.mean()
    return in_mean

def get_median(median_array):
    in_median = median_array.median()
    return in_median

def get_range(range_array):
    in_range = max(range_array) - min(range_array)
    return in_range

def get_std(std_array):
    in_std = std_array.std()
    return in_std

def get_var(var_array):
    in_var = var_array.var()
    return in_var
#print results
print "Here are some statistics based on a dataset pulled from a UK study of Alcohol and Tobacco spending per household \n"
print "The mean of alcohol is {}".format(get_mean(df['Alcohol']))
print "The median of alcohol is {}".format(get_median(df['Alcohol']))
print "The mode of alcohol is {}".format(get_mode(df['Alcohol']))
print "The range of alcohol is {}".format(get_range(df['Alcohol']))
print "The standard deviation of alcohol is {}".format(get_std(df['Alcohol']))
print "The variance of alcohol is {} \n".format(get_var(df['Alcohol']))

print "The mean of tobacco is {}".format(get_mean(df['Alcohol']))
print "The median of tobacco is {}".format(get_median(df['Alcohol']))
print "The mode of tobacco is {}".format(get_mode(df['Alcohol']))
print "The range of tobacco is {}".format(get_range(df['Alcohol']))
print "The standard deviation of tobacco is {}".format(get_std(df['Alcohol']))
print "The variance of tobacco is {}".format(get_var(df['Alcohol']))
