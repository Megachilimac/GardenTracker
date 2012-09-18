import time;
import datetime;
planted = raw_input("Enter date planted as MM DD YY : ")

plantedDate = time.strptime(planted, "%m %d %y")
startDate = datetime.date(plantedDate.tm_year, plantedDate.tm_mon, plantedDate.tm_mday)

maturity = input("Enter days to maturity : ")
difference = datetime.timedelta(days=maturity)

harvestDate = startDate + difference
printableDate = harvestDate.timetuple()

print "Harvest date is : ", printableDate.tm_mon, "/", printableDate.tm_mday, "/", printableDate.tm_year
