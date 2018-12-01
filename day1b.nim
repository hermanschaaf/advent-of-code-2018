import strutils
import sets

var
  val: int
  freqs: seq[int]
  prev: HashSet[int] = initSet[int]()

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