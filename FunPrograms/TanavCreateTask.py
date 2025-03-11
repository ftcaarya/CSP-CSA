def list_even_odd(num_list):
    odds = []
    evens = []
    for num in num_list:
        if num % 2 == 0 and num not in evens:
            evens.append(num)
        elif num % 2 != 0 and num not in odds:
            odds.append(num)

    return evens, odds


def main(num_nums=int(input("How many numbers would you like to check?"))):
    total = []
    for i in range(num_nums):
        total.append(int(input(f"Enter a number: ")))

    finished_result = list_even_odd(sorted(total))
    print(f"All the even numbers: {' '.join(str(num) for num in finished_result[0])}")
    print(f"All the odd numbers: {' '.join(str(num) for num in finished_result[1])}")

main()