def number():
    try:
        x = int(input("Enter a percentace: "))
        if x < 0 or x > 100:
            print("ERROR!")
        else:
            if x > 90:
                print("A")
            else:
                if x >= 80 and x <= 89:
                    print("B")
                else:
                    if x >= 70 and x <= 79:
                        print("C")
                    else:
                        if x >= 60 and x <= 69:
                            print("D")
                        else:
                            print("F")
    except ValueError:
        print("ERROR: Please enter a valid number!")
        number()
number()