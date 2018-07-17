#constant folding evaluate at compile time 
#rather than run time

#lists vs tuples

from dis import dis

dis(compile('(1, 2, 3, 4, "a")', 'string', 'eval'))
"""
  1           0 LOAD_CONST               5 ((1, 2, 3, 4, 'a'))
              2 RETURN_VALUE
"""
#now lets change tuple to list
dis(compile('[1, 2, 3, 4, "a"]', 'string', 'eval'))

"""
1             0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 LOAD_CONST               3 (4)
              8 LOAD_CONST               4 ('a')
             10 BUILD_LIST               5
             12 RETURN_VALUE
"""
#compiler had to load each individual value of list
#and build list and return it

dis(compile('(1, 2, 3, 4, [10, 20])', 'string', 'eval'))

"""
  1           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 LOAD_CONST               3 (4)
              8 LOAD_CONST               4 (10)
             10 LOAD_CONST               5 (20)
             12 BUILD_LIST               2
             14 BUILD_TUPLE              5
             16 RETURN_VALUE
"""