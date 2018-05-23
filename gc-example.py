import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(address):
    for obj in gc.get_objects():
        if id(obj) == address:
            return "Object tracked by GC"
    return "Object not tracked by GC"

class A(object):
    def __init__(self):
        self.b = B(self)
        print("A {} B {} ".format(hex(id(self)),hex(id(self.b))))


class B(object):
    def __init__(self,a):
        self.a = a
        print("B {} A {} ".format(hex(id(self)),hex(id(self.a))))

gc.disable()

my_a = A()

print(ref_count(id(my_a)))
print(ref_count(id(my_a.b)))

print(object_by_id(id(my_a)))
print(object_by_id(id(my_a.b)))

id_A = id(my_a)
id_B = id(my_a.b)

my_a = None

print(ref_count(id(id_A)))
print(ref_count(id(id_B)))

gc.collect()
print(object_by_id(id_A))
print(object_by_id(id_B))

#dont do this 

print(ref_count(id_A))
print(ref_count(id_B))
