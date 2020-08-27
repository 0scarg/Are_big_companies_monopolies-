<<<<<<< HEAD
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
=======
#Run this to see all companies' yearly revenue.
#All info comes from macrotrends.com
import pandas

AMZN = "Amazondata.csv"
Amazon = pandas.read_csv(AMZN)
print("")
print("Yearly revenue for Amazon:")
print(Amazon)

APPL = "Appledata.csv"
Apple = pandas.read_csv(APPL)
print("")
print("Yearly revenue for Apple:")
print(Apple)

FB = "Facebookdata.csv"
Facebook = pandas.read_csv(FB)
print("")
print("Yearly revenue for Facebook:")
print(Facebook)

NFLX = "Netflixdata.csv"
Netflix = pandas.read_csv(NFLX)
print("")
print("Yearly revenue for Netflix:")
print(Netflix)

MSFT = "Microsoftdata.csv"
Microsoft = pandas.read_csv(MSFT)
print("")
print("Yearly revenue for Microsoft:")
print(Microsoft)

>>>>>>> 059e817b5174804d5f5ca79568889fde5b3b63f2
