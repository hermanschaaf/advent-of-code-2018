n = input().strip()
l = len(str(n))
recipes = [3, 7]
a, b = 0, 1
s = 2
while True:
    digits = [int(d) for d in str(recipes[a] + recipes[b])]
    for d in digits:
        recipes.append(d)
        s += 1

        if d == int(n[-1]):
            k = recipes[-l:]
            k = "".join(map(str, k))
            if k == n:
                print(s - l)
                exit(0)

    a = (a + recipes[a] + 1) % len(recipes)
    b = (b + recipes[b] + 1) % len(recipes)
