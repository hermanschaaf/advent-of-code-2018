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

the time now compared better with that of Python, but still not great (497ms vs Python's 57ms):

```
time nimc part2.nim 
81204

real    0m0.497s
user    0m0.388s
sys 0m0.109s
```

The HashSet implementation that comes with Nim must be extremely inefficient at increasing the bounds. It must do so in powers of two however, as the initialization function expects this. Quite strange...

Reading on https://forum.nim-lang.org/t/4416 , it seems like another option to fix it is to import from `intsets` and use `initIntSet()`. I tested this, and the result is slightly slower when including compilation, clocking in at 371ms for compilation + running, but a lot faster when only counting running time:

```
$ time ./part2 
81204

real    0m0.018s
user    0m0.015s
sys 0m0.004s
```
