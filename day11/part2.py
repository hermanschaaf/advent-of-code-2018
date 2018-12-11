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
sizes = [[0 for c in range(n)] for r in range(n)]

for y in range(1, n+1):
    for x in range(1, n+1):
        for s in range(1, 300-max(x, y)+1):
            g = sum(grid[y+s-1][x+c] for c in range(s))
            g += sum(grid[y+r][x+s-1] for r in range(s))
            score = sizes[y-1][x-1] + g
            sizes[y-1][x-1] = score
            if mx_score is None or score > mx_score:
                mx_score = score
                mx = (x+1, y+1, s)

print("{},{},{}".format(*mx))
