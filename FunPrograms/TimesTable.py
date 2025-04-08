def times_table(table: int, till: int):
    current = 1
    while current <= till:
        print(f"{table} x {current} = {table * current}")
        current += 1

    print("\nTime Table finished running.")

times_table(3, 15)
