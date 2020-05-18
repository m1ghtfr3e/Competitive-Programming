# highest and lowest

def high_and_low(numbers):
    
    numbers = sorted(numbers.replace(' ', ''))
    solution = f'{numbers[-1]} {numbers[0]}'
    return solution



if __name__ == '__main__':

    print(high_and_low("1 2 3 4 5"))
    print(high_and_low("1 9 3 4 -5"))