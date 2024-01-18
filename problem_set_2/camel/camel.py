variable = input("camelCase: ").strip()
v_list = [x for x in variable]

for letter in v_list:
    if letter.isupper():
        idx = v_list.index(letter)
        v_list[idx] = v_list[idx].lower()
        v_list.insert(idx, "_")

print("snake_case: {}".format("".join(v_list)))
