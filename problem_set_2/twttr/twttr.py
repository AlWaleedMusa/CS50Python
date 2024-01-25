def main():

    user_input = input("Input: ").strip()
    vowel_list = ["a", "e", "i", "o", "u"]

    user_input_list = [x for x in user_input]
    new_list = []

    for letter in user_input_list:
        if letter.lower() in vowel_list:
            continue
        new_list.append(letter)


    print("Output: {}".format("".join(new_list)))

if __name__ == "__main__":
    main()
