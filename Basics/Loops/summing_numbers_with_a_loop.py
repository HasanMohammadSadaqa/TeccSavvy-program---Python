while True:

    try:
        number = int(input("please enter a number: "))
        if number < 0:
            print("the number must be greater than 0")
        else:
            i = 1
            summation = 0
            while i < number:
                summation += i
                i += 1
            print(summation)
    except ValueError:
        print("please enter an integer number")
