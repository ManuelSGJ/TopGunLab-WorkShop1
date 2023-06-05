if __name__ == '__main__':
    try:
        tempF = int(input('Please enter a temperature in farenheit unit: '))#cuatro
        tempC = (tempF - 32) * 5/9

        print(f'The temperature ${tempF}°F is equal to ${round(tempC, 3)}°C')
    except Exception as err:
        print(err)
