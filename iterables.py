class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid']
        self._index = 0
    
    def __len__(self):
        return len(self._cities)

    def  __iter__(self):
        return self.CityIterator(self)
    
    def __getitem__(self, s):
        return self._cities[s]
    
    
    class CityIterator:
    
        def __init__(self, city_ref):
            self._city_ref = city_ref
            self._index = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index >= len(self._city_ref):
                raise StopIteration
            else:
                item = self._city_ref._cities[self._index]
                self._index += 1
                return item
    

city = Cities()
for item in city:
    print(item)

print(list(enumerate(city)))

city_iterator = city.__iter__()
for c in city_iterator:
    print(c)

# next(city_iterator) iterator was exhausted
