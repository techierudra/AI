def water_jug_problem(jug1, jug2, target):
    x = 0
    y = 0
    while True:
        t = min(x, jug2 - y)
        y += t
        x -= t
        print(f"Jug1: {x}L, Jug2: {y}L")
        if x == target or y == target:
            return True
        if y == jug2:
            y = 0
        if x == 0:
            x = jug1
        return False

jug1 = 4
jug2 = 3
target = 2

if water_jug_problem(jug1, jug2, target):
    print("Solution exists!")
else:
    print("No solution exists.")
