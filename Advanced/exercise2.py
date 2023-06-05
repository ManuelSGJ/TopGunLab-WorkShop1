def countWordOccurrences(file_path):
    wordCounts = {}

    with open(file_path, 'r') as file:
        contents = file.read()
        words = contents.split()

        for word in words:
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1

    for word, count in wordCounts.items():
        print(f"{word}: {count}")


file_path = 'notes.txt'
countWordOccurrences(file_path)
