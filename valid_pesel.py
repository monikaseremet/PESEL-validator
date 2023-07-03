from datetime import datetime

def is_it_valid(pesel: str) -> bool, str:
    if len(pesel) != 11:
        return False
    
    for num in pesel:
        if num not in '0123456789':
            return False
    
    year = int(pesel[:2])
    month = int(pesel[3])
    day = int(pesel[4:6])
    century = int(pesel[2])

    if century == 8 or century == 9:
        year += 1800
        if century == 9:
            month += 10
    if century == 0 or century == 1:
        year += 1900
        if century == 1:
            month += 10
    if century == 2 or century == 3:
        year += 2000
        if century == 3:
            month += 10

    try:
        date_of_birth = datetime(year, month, day)
    except ValueError:
        return False

    numbers_weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_number = 0
    for i in range(10):
        control_number += (int(pesel[i]) * numbers_weight[i]) % 10

    if int(pesel[-2]) % 2 == 0:
        gender = 'woman'
    else:
        gender = 'man'

    return (10 - (control_number % 10)) == int(pesel[-1]), gender

