from datetime import datetime

class Temporal:
    def __init__(self) -> None:
        self.now = datetime.now()
        self.weekday = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Satur", "Sun"]
        self.month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def timenow(self):
        self.__init__()
        expression = str(self.now.hour) + "hours  "  + str(self.now.minute) + " minutes "
        return expression
    
    def daynow(self):
        self.__init__()
        expression = "today is " + self.weekday[self.now.weekday()] + "day"
        return expression
    
    def monthnow(self):
        expression = "month is " + self.month[self.now.month - 1]
        return expression
    
    def yearnow(self):
        expression = "year is " + str(self.now.year)
        return expression

    def datenow(self):
        expression = str(self.now.day) + " " +  str(self.now.month) + " " +  str(self.now.year)
        return expression