def counter():
    i = 0
    def inc():
        nonlocal i
        i += 1
        return i
    return inc
 
class CallableIterator:
    
    def __init__(self, counter, sentinel):
        self._callable = counter
        self._sentinel = sentinel
        self._is_consumed = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._is_consumed:
            raise StopIteration

        result = self._callable()
        if result == self._sentinel:
            self._is_consumed = True
            raise StopIteration
        return result

cnt = counter()
cnt_iter = CallableIterator(cnt, 17)
print(list(cnt_iter))
#print(next(cnt_iter))

#iter provides the above form 

cnt = counter()
cnt_iter = iter(cnt, 10)
print(list(cnt_iter))