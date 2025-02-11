import sys


def plain_while():
    i = 0
    while i < 10:
        print(f"{i = }")
        i += 1


def complex_while():
    from my_functions import calculate_geometric_series

    while True:  # loop forever!
        a = int(input("a: "))
        r = float(input("r: "))
        n = int(input("n: "))
        s_n = calculate_geometric_series(a, r, n)
        print(f"{s_n = }")
        quit_ = input("to quit enter 'q': ")  # why do we use 'quit_' instead of 'quit'
        if quit_ == 'q':
            break


def loop_over_file():
    with open("paradoxical.txt") as f:
        while line := f.readline():
            print(f"{line = }")

def reverse_while():
    i = 9
    while i > -1:
        print(f"{i = }")
        i-=1

def sum_it():
    i = -12
    sum = 0
    while True:
        if sum >1000:
            break
            sum += 1
            i += 1
        print(f"{sum = }")

def main():
    # plain_while()
    # complex_while()
    # loop_over_file()
    # reverse_while()
    # sum_it()
    return 0


if __name__ == '__main__':
    sys.exit(main())
