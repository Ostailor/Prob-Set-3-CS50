grocery_list = {

}

while True:
    try:
        item = input().upper()
        if item not in grocery_list:
            grocery_list[item] = 1
        elif item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
    except EOFError:
        break

for i in sorted(grocery_list):
    print(f"{grocery_list[i]} {i}")
