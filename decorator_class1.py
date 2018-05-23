#monkey patching classes at runtimes

from fractions import Fraction

f = Fraction(2,3)
print(f)
print(f.numerator, f.denominator)

Fraction.speak = lambda self : print(self.numerator,self.denominator)

f.speak(f)

Fraction.is_integral =  lambda self : self.denominator == 1

f1 = Fraction(2, 5)
f2 = Fraction(64, 8)

print(f1.is_integral(f1))

print(f2.is_integral(f2))

#################################################

from fractions import Fraction

def dec_speak(cls):
    cls.speak = lambda self, message : \
                        "{} says {}".format(self.__class__.__name__, message)

    return cls


Fraction = dec_speak(Fraction)

f1 = Fraction(2, 3)
print(f1.speak("hello"))

class Person:
    pass

Person = dec_speak(Person)
p = Person()
print(p.speak("this works"))

##################################################





        



