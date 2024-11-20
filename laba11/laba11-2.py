def count_positive_in_halves(sequence):
    n = len(sequence)

    mid_index = (n + 1) // 2
    first_half = sequence[:mid_index]
    second_half = sequence[mid_index:]

    positives_first_half = len(list(filter(lambda x: x > 0, first_half)))
    positives_second_half = len(list(filter(lambda x: x > 0, second_half)))

    if positives_first_half > positives_second_half:
        return "У першій половині більше додатних елементів."
    elif positives_first_half < positives_second_half:
        return "У другій половині більше додатних елементів."
    else:
        return "Кількість додатних елементів однакова в обох половинах."

user_input = input("Введіть послідовність чисел, розділених пробілами: ")
sequence = list(map(int, user_input.split()))
result = count_positive_in_halves(sequence)
print(result)
