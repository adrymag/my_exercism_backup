from datetime import datetime

class Clock:
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = hour % 24 + int( (minute - minute % 60) / 60 )        

    def __repr__(self):
        self.minute = self.minute % 60
        self.hour = self.hour % 24 + int( (self.minute - self.minute % 60) / 60 ) 
        return "Clock(" + str(self.hour) + ", " + str(self.minute) + ")"
        # return "Clock(" + ("0" + str(self.hour))[-2:] + ", " + ("0" + str(self.minute))[-2:] + ")"

    def __str__(self):
        self.minute = self.minute % 60
        self.hour = self.hour % 24 + int( (self.minute - self.minute % 60) / 60 ) 
        return ("0" + str(self.hour))[-2:] + ":" + ("0" + str(self.minute))[-2:]
 
    def __eq__(self, other):
        if self.hour % 24 == other.hour % 24 and self.minute == other.minute:
            return True
        return False

    def __add__(self, minutes):
        if 60 - self.minute > minutes:
            self.minute += minutes
        else:
            self.minute += minutes % 60
            self.hour += int( (minutes - minutes % 60) / 60)
            self.hour %= 24
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        if self.minute >= minutes:
            self.minute -= minutes
        else:
            self.minute -= minutes % 60
            self.hour -= int( (minutes - minutes % 60) / 60)
            self.hour %= 24
        return Clock(self.hour, self.minute)