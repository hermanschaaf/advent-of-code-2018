include "strutils"

var val = 0
for line in "day1.in".lines:
  let v = parseInt(line)
  val += v
echo val