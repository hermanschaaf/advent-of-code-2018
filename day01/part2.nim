import strutils
import sets
import math

var
  val: int
  freqs: seq[int]
  prev = initSet[int](nextPowerOfTwo(10000000))

for line in "day1.in".lines:
  let f = parseInt(line)
  freqs.add(f)

proc find(): bool =
  for f in freqs.items:
    val += f
    if val in prev:
      return true
    prev.incl(val)
  return false

while true:
  let found = find()
  if found:
    break

echo val