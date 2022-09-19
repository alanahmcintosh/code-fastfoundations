import sys


def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)

def get_max(a_list):
    maximum = None
    first = False
    for value in a_list:
        if not first:
            maximum = value
            first = True
        if value > maximum:
            maximum = value
    return maximum

def main():
    a = int(input("a: "))
    r = float(input("r: "))
    n = int(input("n: "))
    print(f"s_n = {calculate_geometric_series(a, r, n)}")
    return 0
 # my_list = [7,11,2,57]
 # my_max = get_max(my_list)
  #print(f"{my_max = }")





if __name__ == "__main__":
    sys.exit(main())




