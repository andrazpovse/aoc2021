def get_number(numbers, bit_index, rating):
    count_ones = [0] * len(numbers[0])
    for number in numbers:
        count_ones = [x + y for x, y in zip(number, count_ones)]

    if count_ones[bit_index] >= len(numbers)/2:
        selected_bit = 1
    else:
        selected_bit = 0

    if rating == "co2":
        if selected_bit == 0:
            selected_bit = 1
        else:
            selected_bit = 0

    return [number for number in numbers if selected_bit == number[bit_index]]

def get_rating(rating, numbers):
    bit_index = 0

    while (True):
        numbers = get_number(numbers, bit_index, rating)
        bit_index += 1

        if len(numbers) == 1:
            return ''.join(str(i) for i in numbers[0])

with open('input.txt') as f:
    starting_numbers = [[int(c) for c in line.strip()] for line in f]

numbers = starting_numbers

oxygen = get_rating("oxygen", numbers)
co2 = get_rating("co2", numbers)

print(int(co2, 2) * int(oxygen, 2))
