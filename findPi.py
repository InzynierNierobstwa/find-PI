import math
import decimal

def roundPiNum():
    roundNum = 0
    while roundNum <= 0:
        print('Please, input value: ')
        roundNum = int(float(input()))

        if roundNum > 27:
            roundNum = 0

        piValue = round(decimal.Decimal(math.pi), roundNum)

    print(f'The pi value after round by {roundNum} is {piValue}')

roundPiNum()