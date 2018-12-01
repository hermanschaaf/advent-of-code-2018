# Notes

This is just some things I noted about Nim as I was learning it for Advent of Code.

## Making Nim Output less Verbose

When you run `nim c -r <file.nim>`, output is very verbose, showing lots of hints and C compilation steps. I didn't like this, and wanted output unrelated to my program itself be silent (similar to Python). So I immediately added an alias to my `~/.bashrc` file:

```
alias nimc="nim c --verbosity=0 -r --hints:off"
```

Now I can run:

```
nimc <program name>
```

and have the program compiled and run with no extra output.