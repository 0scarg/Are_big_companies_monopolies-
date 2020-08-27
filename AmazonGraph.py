#Graph to show Amazon's yearly revenue
import pandas
import matplotlib.pyplot as plt

AMZN = "AmazonData.csv"
Amazon = pandas.read_csv(AMZN)

Year = Amazon.Year
Revenue = Amazon.Revenue

plt.plot(Year,Revenue)
plt.xlabel("Year")
plt.ylabel("Revenue(in millions of USD)")

plt.show()