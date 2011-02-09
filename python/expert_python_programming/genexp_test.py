#!/usr/bin/python
it = (x**2 for x in range(10) if x % 2 == 0)

for el in it:
    print(el)
        
