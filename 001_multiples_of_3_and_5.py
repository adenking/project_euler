'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def Check_Multiple(number):
    if(number % 3 == 0)or(number % 5 == 0):
        return True


def Start(total):
    total_value = 0
    for number in range(1, (total)):
        if(Check_Multiple(number)):
            total_value += number
    print(f'The sum of the multiples of {total} is {total_value}')


if __name__ == "__main__":
    Start(10)
    Start(1000)
