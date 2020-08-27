#Comparing all the companies' highest revenue on a graph

import pandas
import matplotlib.pyplot as plt

HighRev = "HighRev.csv"
Comparison = pandas.read_csv(HighRev)

Company = Comparison.Company
HighestRev = Comparison.Highest_Revenue

plt.plot(Company,HighestRev)
plt.xlabel("Company")
plt.ylabel("Highest Revenue")

plt.show()