import sys


def using_math_library():
    import math
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:  # real
        x1 = (-b + math.sqrt(discriminant)) / 2 / a
        x2 = (-b - math.sqrt(discriminant)) / 2 / a
    else:  # imaginary
        x1 = complex(-b / 2 / a, math.sqrt(-discriminant) / 2 / a)
        x2 = complex(-b / 2 / a, -math.sqrt(-discriminant) / 2 / a)
    print(f"{x1 = }")
    print(f"{x2 = }")


def using_cmath_library():
    import cmath
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / 2 / a
    x2 = (-b - cmath.sqrt(discriminant)) / 2 / a
    print(f"{x1 = }")
    print(f"{x2 = }")


def using_datetime_library():
    import datetime
    from zoneinfo import ZoneInfo # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    print(datetime.datetime(2022, 4, 28, 11, 14, 32, 13432, ZoneInfo('Asia/Ashkhabad'))) # datetime
    print(datetime.date(2022, 4, 28)) # date
    print(datetime.time(14, 33, 7, 23422, ZoneInfo('Asia/Baku'))) # time
    datetime1 = datetime.datetime(2013, 9, 7, 8, 39, 58, 27389, ZoneInfo('Australia/Lindeman'))
    datetime2 = datetime.datetime.now(ZoneInfo('Europe/Kyiv'))
    print(f"{datetime2 - datetime1 = }") # timedelta
    print(f"{datetime.date.today() = }")

def solve_equation():
    import math
    a = float(input("a: "))
    b = float(input("b: "))
    g = float(input("g: "))
    discriminant = 2 * (a * b) * math.cos(g)
    c = math.sqrt((a + b) ** 2 - discriminant ** 2)
    print(f"{c = }")

def using_shuffle():
    import random
    my_list = list(range(127, 349))
    random.shuffle(my_list)
    print(f"{my_list = }")
    letter_list = ["a", "b", "c"]
    for value in range(10):
        print(f"{random.choice(letter_list) = }")
    print(f"{random.choices(letter_list, k=10) = }")

def cocoa_beans():
    import csv
    with open ('FAOSTAT_data_en_7-23-2022.csv', 'w') as table_together:
        table_csv =csv.reader(table_together)
        header = []
        header = next(table_csv)
        header
        rows = []
        for row in table_csv:
           rows.append(row)
        rows

def read_to_table():
    import csv
    ghana_data = dict()
    cote_data = dict()
    with open('FAOSTAT_data_7-23-2022.csv') as f:
        fao_reader = csv.reader(f)
        for row in fao_reader:
            data = row[11]
            field = row[5]
            year = row[9]
            if row[3] == "Ghana":
                if year not in ghana_data:
                    ghana_data[year] = dict()
                if field == 'Area Harvested':
                    cote_data[year]['Area Harvested'] = field
                elif field == 'Yield':
                    cote_data[year]['Yield'] = field
                elif field == 'Production':
                    cote_data[year]['Production'] = field
            elif row[3] == "Côte d'Ivoire":
                if year not in cote_data:
                    cote_data[year] = dict()
                if field == 'Area Harvested':
                    cote_data[year]['Area Harvested'] = field
                elif field == 'Yield':
                    cote_data[year]['Yield'] = field
                elif field == 'Production':
                    cote_data[year]['Production'] = field

    production_ghana = list()
    with open ('ghana.txt', 'w') as f:
        for year, data in ghana_data.items():
            print(f"{year}\t{data['Area Harvested']}\t{data['Yield']}\t{data['Production']}", file=f)
            production_ghana.append(int(data['Production']))












def main():
    # using_math_library()
    # using_cmath_library()
    # using_datetime_library()
    # solve_equation()
    # using_shuffle()
    # cocoa_beans()
    read_to_table()
    return 0


if __name__ == '__main__':
    sys.exit(main())
