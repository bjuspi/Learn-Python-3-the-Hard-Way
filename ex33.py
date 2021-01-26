def ex33(upper_bound, increment):
    i = 0
    numbers = []

    while i < upper_bound:
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

ex33(10, 2)