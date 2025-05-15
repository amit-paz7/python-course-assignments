numbers = [1203, 1256, 312456, 98]
digit_counts = {}
digits = '0123456789'
for digit in digits:
    digit_counts[digit] = 0

for number in numbers:
    number_str = str(number)
    for digit in number_str:
        if digit in digit_counts:
            digit_counts[digit] += 1

for digit, count in digit_counts.items():
    print(f"{digit}  {count}")
