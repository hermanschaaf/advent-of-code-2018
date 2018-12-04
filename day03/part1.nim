import nre, options, strutils, sequtils, parseutils
import intsets

var ids = initIntSet()
var grid = newSeqWith(1000, newSeq[int](1000))
var total = 0
# claims = []
for line in "input".lines():
  let f = line.find(re"""#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)""")
  var claim = map(f.get.captures.toSeq(), proc(x: string): int = parseInt(x))
  var left = claim[1]
  var top = claim[2]
  var width = claim[3]
  var height = claim[4]
  
  for row in top .. (top + height - 1):
    for col in left .. (left + width - 1):
      grid[row][col] += 1
      if grid[row][col] == 2:
        total += 1

echo total
