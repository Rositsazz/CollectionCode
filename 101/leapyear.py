from math import floor


def which_year(year):
    is_leap = False
    first_day = 0
    if year % 4 == 0 and year % 100 != 0:
        is_leap = True
    century = (year // 100) % 4
    if century == 0:
        century = 6
    elif century == 1:
        century = 4
    elif century == 2:
        century = 2
    else:
        century = 0
    if is_leap:
        first_day = 7 + century + year % 100 + floor((year % 100) / 4)
    else:
        first_day = 1 + century + year % 100 + floor((year % 100) / 4)
    first_day = first_day % 7
    return first_day


# print(which_year(2013))


def friday_years(year1, year2):
    result = 0
    for year in range(year1, year2 + 1):
        which = which_year(year)

        is_leap = False
        if year % 4 == 0 and year % 100 != 0:
            is_leap = True
        if (which == 4 and is_leap == True) or which == 5:
            result += 1

    return result

print(friday_years(1753, 2000))
