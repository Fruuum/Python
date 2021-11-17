words = input("введите слова, разделенные пробелами: ").split()
for ind, el in enumerate(words, 1):
    print(ind, el[:10])
