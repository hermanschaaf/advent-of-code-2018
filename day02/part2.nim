import tables
import strutils

proc diff_by_one(w: string, w2: string): string = 
  var d: int = 0
  var pos: int = 0
  for i, ch in w.pairs:
    if ch != w2[i]:
      d += 1
      pos = i
  if d != 1:
    return ""
  let a = w[0 .. pos-1]
  let b = w[pos+1 .. w.len-1]
  return join(@[a, b], "")

proc solve(words: seq[string]): string =
  for i, w in words.pairs:
    for u in i .. words.len-1:
      var w2 = words[u]
      var ans = diff_by_one(w, w2)
      if ans != "":
        return ans
  return ""

var words: seq[string]
for line in "input".lines:
  words.add(line)

echo solve(words)