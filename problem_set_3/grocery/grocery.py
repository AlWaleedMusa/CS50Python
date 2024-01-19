item_li = []
while True:
    try:
        user_input = input()
        item_li.append(user_input)
    except EOFError:
        break

item_set = set()
for item in item_li:
    item_set.add((item, item_li.count(item)))

for a, b in sorted(item_set):
    print("{} {}".format(b, a.upper()))
