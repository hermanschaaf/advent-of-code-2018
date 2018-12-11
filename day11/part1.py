n = 300
serial = int(input())
grid = [[0 for c in range(n)] for r in range(n)]

for y in range(1, n+1):
    for x in range(1, n+1):
        rack_id = x + 10
        power = rack_id * y
        power += serial
        power *= rack_id
        power = (power // 100) % 10
        power -= 5
        grid[y-1][x-1] = power

mx, mx_score = None, None
for y in range(1, n+1-3):
    for x in range(1, n+1-3):
        score = sum(sum(grid[y+r-1][x+c-1] for c in range(3)) for r in range(3))
        if mx_score is None or score > mx_score:
            mx_score = score
            mx = (x, y)

print("{},{}".format(*mx))
