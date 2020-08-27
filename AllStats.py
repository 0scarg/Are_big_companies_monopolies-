#Run this to see yearly revenue of our chosen companies.
#All revenue is taken from macrotrends.com

import pandas

AMZN = "AmazonData.csv"
Amazon = pandas.read_csv(AMZN)
print("Yearly revenue of Amazon:")
print(Amazon)
print("-------------------------")

APPL = "AppleData.csv"
Apple = pandas.read_csv(APPL)
print("Yearly revenue of Apple")
print(Apple)
print("-------------------------")

FB = "FacebookData.csv"
Facebook = pandas.read_csv(FB)
print("Yearly revenue of Facebook:")
print(Facebook)
print("-------------------------")

GOOG = "GoogleData.csv"
Google = pandas.read_csv(GOOG)
print("Yearly revenue of Google:")
print(Google)
print("-------------------------")

MSFT = "MicrosoftData.csv"
Microsoft = pandas.read_csv(MSFT)
print("Yearly revenue of Microsoft")
print(Microsoft)
print("-------------------------")

NFLX = "NetflixData.csv"
Netflix = pandas.read_csv(NFLX)
print("Yearly revenue of Netflix:")
print(Netflix)
