def main():

    coke_price = 50
    print("Amount Due: {}".format(coke_price))
    while coke_price != 0:
        coin = int(input("Insert Coin: "))

        if coin == 5:
            coke_price -= coin
            if coke_price > 0:
                print("Amount Due: {}".format(coke_price))
        elif coin == 10:
            coke_price -= coin
            if coke_price > 0:
                print("Amount Due: {}".format(coke_price))
        elif coin == 25:
            coke_price -= coin
            if coke_price > 0:
                print("Amount Due: {}".format(coke_price))
        else:
            print("Amount Due: {}".format(coke_price))


        if coke_price == 0:
            print("Change Owed: {}".format(coke_price))
            break
        elif coke_price < 0:
            print("Change Owed: {}".format(coke_price * -1))
            break

if __name__ == "__main__":
    main()
