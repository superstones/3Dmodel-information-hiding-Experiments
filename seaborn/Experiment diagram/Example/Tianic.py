import seaborn as sns
import pandas as pd
import pandas_profiling
import matplotlib.pyplot as plt


data = pd.read_csv('titanic.csv')
data.head()

pfr = pandas_profiling.ProfileReport(data)
pfr.to_file('report.html')
