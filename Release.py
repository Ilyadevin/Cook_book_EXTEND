file = open("Recipes.txt")
onstring = file.read().split("\n")[:-1]
cook_book = dict()
for item in onstring:
    print(item)
    key = item.split("\n")[0]
    value = item.split("\n")
    cook_book[key] = value
    print(cook_book)