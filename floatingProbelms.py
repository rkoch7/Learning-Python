x = 0.1
print(format(x,".25f"))

y = 0.125
print(format(y,".25f"))

x = 0.125 + 0.125 + 0.125
print(x)
print(format(x,".50f"))
y = 0.375
print(x == y) #x and y both have finite representation

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)
print(format(x,".25f"))
print(format(y, ".25f"))
import math
print(math.isclose(x,y,rel_tol=1e-09,abs_tol=1e-09))

#large absolute tolerance is pain
#smaller numbers relative tol does not work fine
#that is why we use math.isclose which uses both 
#relative and abs tolerance
