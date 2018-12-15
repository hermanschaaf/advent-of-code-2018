# Day 15: Beverage Bandits

To make today's problem a bit more interesting (and a bit less tedious), I decided to write the code as Pythonic as possible. I therefore made abundant use of magic methods (aka dunderscore methods), and implemented a Position class that can be added, subtracted, and more. 

For part 2 I used binary search to narrow in on the answer more quickly than a linear search through all attack powers. A* search would be another way to optimize this, but a simple BFS search and early exit when any elf dies sufficed to allow the problem to be solved in about 30 seconds.