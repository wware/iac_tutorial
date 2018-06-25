import sys

many = [20 * [None] for _ in range(20)]

def display():
    width = 4
    for i in range(0, 20, 2):
        def s(x):
            t = str(x)
            n = len(t)
            a = (width - n) / 2
            b = width - (a + n)
            return (a * " ") + t + (b * " ")
        r = ""
        for x in many[i]:
            r += s(x)
        print r
        print
        r = ""
        for x in many[i+1]:
            r += s(x)
        print ((width / 2) * " ") + r
        print


def fill_in(u, v, value):
    if 0 <= u < 20 and 0 <= v < 20:
        many[u][v] = value


def scan(u, v, value, increment):
    for i in range(20):
        fill_in(u, v, value)
        u += 1
        if i % 2:
            v += 1
        value += increment


def main():
    a, b = int(sys.argv[1]), int(sys.argv[2])
    v = 0
    for i in range(30):
        scan(0, v - 10, i * b, a)
        v += 1
    z = many[10][10]
    for i in range(20):
        for j in range(20):
            many[i][j] -= z
    display()

if __name__ == '__main__':
    main()
