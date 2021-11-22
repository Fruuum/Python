# task6
word = input("введите слово: ")
letters = list(word)


def exam():
    for el in range(len(letters)):
        if 97 <= ord(letters[el]) <= 122:
            el += 1
        else:
            return f"Error"
    return word.title()


print(exam())

# task7

words = input("Введите слова: ")


def exam2():
    for ltr in words:
        if not (97 <= ord(ltr) <= 122 or ord(ltr) == 32):
            raise ValueError(f"Words {words} have not ascii char.")
    return words.title()


print(exam2())
