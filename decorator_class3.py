from datetime import datetime, timezone

def info(self):
    results = []
    results.append("time: {}".format(datetime.now(timezone.utc)))
    results.append("Class: {}".format(self.__class__.__name__))
    results.append("Obj Address: {}".format(hex(id(self))))
    for k, v in vars(self).items():
        results.append("{}: {}".format(k, v))
    
    return results


def debug_info(cls):
    cls.debug_info = info
    return cls

@debug_info
class Automobile:

    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError("Speed cannot exceed top_Speed")
        else:
            self._speed = new_speed

    

ford = Automobile("Ford", "Model T", 1908, 45)
print(ford)
print(ford.debug_info())

ford.speed = 40
print(ford.debug_info())

