def reverseWord(word):
    return ''.join(reversed(word))

if __name__ == '__main__':
    words = input('Enter a word please: ')
    print(f'Your words in reverse order is: {reverseWord(words)}')