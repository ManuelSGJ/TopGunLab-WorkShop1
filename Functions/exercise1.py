def numberMajor(numbers):
    return max(numbers)

if __name__ == '__main__':
    exit = False
    numbers = []

    while not exit:
        number = int(input('Please enter a number: '))
        numbers.append(number)

        answer = input('Do you want to continue introducing numbers? (y/n): ').lower()
        if answer == 'n':
            exit = True

    print(f'The major number is {numberMajor(numbers)}')

