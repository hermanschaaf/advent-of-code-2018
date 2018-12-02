import tables
import strutils 

var 
  twos: int
  threes: int

for line in "input".lines:
  var d = initTable[char,int]()
  for ch in line:
    d.mgetOrPut(ch, 0) += 1

  var 
    found_twos: bool
    found_threes: bool

  for k, v in d.pairs():
    if v == 2:
      found_twos = true
    if v == 3:
      found_threes = true

  if found_twos:
    twos += 1
  if found_threes:
    threes += 1

echo(twos * threes)
