menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

num = 0
while True:
    try:
        user_input = input("Item: ")
        for item, price in menu.items():
            if user_input.title() == item:
                num += price
                print("Total: ${:.2f}".format(num))
    except EOFError:
        break
