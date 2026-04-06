def clean_input(data):
    parts = data.replace(",", " ").split()
    numbers = []
    for part in parts:
        if part.isdigit():
            numbers.append(int(part))
    return numbers


def analyze_dataset(data = input("Please enter the dataset: ")):
    numbers = clean_input(data)

    if not numbers:
        print("No valid numbers in dataset.")
        return

    total = 0
    freq = {}

    for num in numbers:
        total += num
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    average = total / len(numbers)
    print(f"Average: {average:.2f}")

    for num in sorted(freq.keys()):
        print(f"{num} appeared {freq[num]} times within the dataset")



analyze_dataset()
