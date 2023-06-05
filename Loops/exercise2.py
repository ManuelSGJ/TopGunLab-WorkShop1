def isPrime(number):
    divisors = 0

    if number < 0: 
        return False

    for i in range(number):
        numPrevious = i + 1

        if number % numPrevious == 0:
            divisors = divisors + 1
        
        if divisors > 2:
            return False

    return True
if __name__ == '__main__':
    try:
        number = int(input('Please enter a number: '))
        if isPrime(number):
            print('The number is prime')
        else:
            print('The number is not prime')

    except Exception as err:
        print(err)