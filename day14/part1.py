n = int(input())
recipes = [3, 7]
a, b = 0, 1
s = 0
while True:
    digits = [int(d) for d in str(recipes[a] + recipes[b])]
    recipes += digits
    a = (a + recipes[a] + 1) % len(recipes)
    b = (b + recipes[b] + 1) % len(recipes)

    if len(recipes) >= n + 10:
        print("".join(map(str, recipes[n:n+10])))
        break

    s += 1
