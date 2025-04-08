# your function should return the maximum value in `my_list`

def max_int_in_list(my_list):
    maxim = my_list[0]
    for num in my_list:
        if num > maxim:
            maxim = num

    return maxim

