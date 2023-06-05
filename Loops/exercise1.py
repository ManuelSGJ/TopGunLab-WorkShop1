if __name__ == '__main__':
    acum = 1
    previous = None
    sequence = []
    for i in range(10):
        if i == 0 or i == 1:
            sequence.append(acum)
        else:
            sequence.append(sequence[i-1] + sequence[i-2])
            
    print(sequence)