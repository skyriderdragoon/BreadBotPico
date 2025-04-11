import time
import math
import modules.EndTime as ET
import ujson as json
class Data:
    def __init__(self, Distance):
        self.ID = self.__Set_ID()
        self.InitialMeasurement = self.Measurement(Distance, time.time())
        self.FinalMeasurement = self.TargetMeasurement(Distance)
        self.Measurements = [self.Measurement(Distance, time.time())]
        self.StartTime = time.localtime()
        self.PredictedEndTime = "Unknown"
        self.RateOfChange = 0

    # External functions

    def Add_Measurement(self, distance):
        self.Measurements.append(self.Measurement(distance, time.time()))
        self.PredictedEndTime = self.__Calculate_End()
        return True

    def Check_Status(self, distance):
        return distance >= self.FinalMeasurement.distance

    # Internal functions

    def __Calculate_End(self):
        growth = self.Measurements[-1].distance - self.Measurements[-2].distance
        time_difference = self.Measurements[-1].time - self.Measurements[-2].time
        self.RateOfChange = growth / time_difference
        # Calculate the time it will take to reach the final measurement
        totalseconds = (self.FinalMeasurement - self.Measurements[-1].distance) / self.RateOfChange
        TimeUntilDone = self.Time.from_seconds(totalseconds)
        return TimeUntilDone
    
    def __Set_ID(self):
        data= None
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                data["ID"] = int(data["ID"]) + 1
                self.ID = "BreadBot_{}".format(data["ID"])
                f.close()
        except:
            print("Error:could not open file")
        try:
            with open('data.json', 'w') as f:
                json.dump(data, f)
                f.close()
        except:
            print("Error:could not open file")

    # Classes
    # These classes are used to store the measurements and any other required data

    class Measurement:
        def __init__(self, distance, time):
            self.distance = distance
            self.volume = ET.segment_volume(distance)
            self.time = time

    class TargetMeasurement:
        def __init__(self, distance):
            self.distance = distance
            self.volume = ET.segment_volume(distance)*2

    class Bowl:
        def __init__(self, width, flat_bottom):
            self.width = width
            self.top_radius = width / 2
            self.flat_bottom = flat_bottom
            self.effective_R = width / 2 - flat_bottom

    class Time:
        def __init__(self, hours, minutes, seconds):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

        def __str__(self):
            if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
                return "N/A"
            else:
                return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        
        @classmethod
        def from_seconds(cls, total_seconds):
            hours = math.floor(total_seconds // 3600)
            minutes = math.floor((total_seconds % 3600) // 60)
            seconds = math.floor(total_seconds % 60)
            return cls(hours, minutes, seconds)
        
            

    




