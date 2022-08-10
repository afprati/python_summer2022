## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return "%02d:%02d" % (self.hour, self.minutes) 
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        mins = self.hour*60 + self.minutes + minutes
        mins = mins % (24 * 60)
        self.hour = mins // 60
        self.minutes = mins % 60
        

    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
       self.__add__(-1*minutes)
    
    ## Are two times equal?
    def __eq__(self, other):
         return self.hour == other.hour and self.minutes == other.minutes
    
    ## Are two times not equal?
    def __ne__(self, other):
        return not self.__eq__(other)

# You should be able to run these
clock1 = Clock(23, 5)
print(clock1) # 23:05
clock2 = Clock(12, 45)
print(clock2) # 12:45
clock3 = Clock(12, 45)
print(clock3) # 12:45

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("testing addition")
clock1 + 60
print(clock1) # 00:05
print(clock1 == Clock(0, 5)) # True

print("testing subtraction")
clock1 - 100
print(clock1) # 22:25
