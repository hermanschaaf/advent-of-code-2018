# Day 2


## Using <

In part 2, I used:

```
for u in i .. <words.len:
```

which resulted in a compiler warning:

```
part2.nim(9, 19) Warning: < is deprecated [Deprecated]
```

Strange, as I saw this syntax in the onboarding tutorial! Maybe that should be updated? For now I will change it to use -1

## Joining strings

Coming from Python, I thought I could join two strings like this:

```
join(a, b)
```

but actually this results in joining of string `a` (with itself) using separator `b`.

In actual fact, strings `a` and `b` should be put into a sequence and joined with an empty separator:

```
join(@[a, b], "")
```

Maybe I'll find a more natural way as I go along.