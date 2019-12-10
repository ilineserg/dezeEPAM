def is_armstrong(number):
    return sum(map(lambda x: int(x) ** len(str(number)), [i for i in str(number)])) == number


assert is_armstrong(153) == True, "Число Армстронга"
assert is_armstrong(10) == False, "Не число Армстронга"
