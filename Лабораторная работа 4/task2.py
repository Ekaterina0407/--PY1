def get_count_char(str_):
    total = {}
    str_ = str_.lower()

    for char in str_:
        if not char.isalpha():
            continue

        if char not in total:
            total[char] = 1
        else:
            total[char] += 1
    return total
def percentage(dictionary):
    total_ = sum(dictionary.values())
    percentage_total = {}

    for char, amount in dictionary.items():
        percentage_total[char] = amount / total_ * 100.0
    return percentage_total


print(get_count_char("Абв абв аа бб в а б в"))
print(percentage(get_count_char("Абв абв аа бб в а б в")))


