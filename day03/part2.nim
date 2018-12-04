import nre, options, strutils, sequtils, parseutils

var grid = newSeqWith(1000, newSeq[int](1000))

proc is_unique(left: int, top: int, width: int, height: int): bool = 
  for row in top .. (top + height - 1):
    for col in left .. (left + width - 1):
      if grid[row][col] > 1:
        return false
  return true

var total = 0
var claims = newSeqWith(1000, newSeq[int](5))
for line in "input".lines():
  let f = line.find(re"""#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)""")
  var claim = map(f.get.captures.toSeq(), proc(x: string): int = parseInt(x))
  var id = claim[0]
  var left = claim[1]
  var top = claim[2]
  var width = claim[3]
  var height = claim[4]
  claims.add(@[id, left, top, width, height])
  
  for row in top .. (top + height - 1):
    for col in left .. (left + width - 1):
      grid[row][col] += 1

for claim in claims:
  var uniq = is_unique(claim[1], claim[2], claim[3], claim[4])
  if uniq:
    echo claim[0]