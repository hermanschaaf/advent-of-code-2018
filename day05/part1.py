def simplify(text):
    n = []
    changes = 0
    skip = False
    for a, b in zip(text, text[1:]):
        if skip:
            skip = False
            continue

        if a != b and a.lower() == b.lower():
            skip = True
            changes += 1
        else:
            n.append(a)
    if not skip:
        n.append(text[-1])

    if changes != 0:
        return simplify("".join(n))
    return "".join(n)


text = open("input.txt", 'r').read().strip()
print(len(simplify(text)))
