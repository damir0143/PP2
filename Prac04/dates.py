#1
# Import the datetime module and display the current date:
#Импортируйте модуль datetime и отобразите текущую дату:
import datetime

x = datetime.datetime.now()
print(x)

#2 Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#3
#Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#4 
#Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#5 выведет текущий день недели на английском языке.
import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))