# Day 1

Part 1 was a straight-forward `for` loop.

Part 2 uses a HashSet, and proved very slow (11s) initially. An equivalent Python solution was faster by several orders of magnitude:

```
time nimc part2.nim 
81204

real    0m11.525s
user    0m11.484s
sys 0m0.024s
```

```
time python part2.py 
81204

real    0m0.057s
user    0m0.053s
sys 0m0.004s
```

The problem turned out to be with the initialization of the integer HashSet. When initializing it with a larger number, 

```
prev = initSet[int](nextPowerOfTwo(10000000))
```

the time compared better with that of Python:

```
time nimc part2.nim 
81204

real    0m0.497s
user    0m0.388s
sys 0m0.109s
```

The HashSet implementation that comes with Nim must be extremely inefficient at increasing the bounds.