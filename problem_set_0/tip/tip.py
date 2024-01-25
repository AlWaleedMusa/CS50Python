def main():

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(num):
    """ remove a $ sign from the string and turn it to float

    args:
        num: user input passed to the function

    return:
        a float
    """
    number = num[1:]
    return float(number)


def percent_to_float(p):
    """ takes a string percent from the user
    
    args:
        p: percent from user input
        
    return:
        a float of the percent
    """
    percent = p[:-1]
    return float(percent) / 100

if __name__ == "__main__":
    main()
