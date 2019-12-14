with open('Список рецептов.txt') as f:
    cook_book = {}
    ingredients_dict = {}
    while True:
        ingredient_list = []
        food = f.readline().strip()
        if not food:
            break
        for i in range(int(f.readline().strip(''))):
            ingredient = f.readline().strip().split('|')
            ingredient_list.append(
                {'ingridient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
        f.readline().strip()
        cook_book[food] = ingredient_list


def dishes_lists(d, p):
    for item, value in cook_book.items():
        if item == d:
            print(item)
            for val in list(value):
                count_0 = val.get('ingridient_name')
                variable = val.get('quantity')
                count_2 = val.get('measure')
                print(count_0, int(variable) * p, count_2)


def counting():
    while True:
        dish = input("Введите блюдо  ")
        count = input('Введите количество блюд  ')
        count_ints = int(count)
        dishes_lists(dish, count_ints)


counting()
