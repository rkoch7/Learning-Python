from datetime import datetime, timezone

def info(self):
    results = []
    results.append("time: {}".format(datetime.now(timezone.utc)))
    results.append("Class: {}".format(self.__class__.__name__))
    results.append("id: {}".format(hex(id(self))))
    for k,v in vars(self).items():
        results.append("{}: {}".format(k, v))
    return results


def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person1:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi(self):
        print("hi there")


p1 = Person1("John", 1939)
print(p1.debug())

