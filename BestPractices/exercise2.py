import time
import random

def timer(func):
    def content(*args, **kwargs):
        timeInit = time.time()
        result = func(*args, **kwargs)
        timeFinal = time.time()
        totalTime = timeFinal - timeInit

        print(f'Total time execution: {totalTime}')
        return result
    
    return content

@timer
def randomList(length, min, max):
    numbers = []
    
    for i in range(length):
        numbers.append(random.randint(min, max))
    
    return numbers

numberResult = randomList(10, 1, 50)
print(f'The list is: {numberResult}')