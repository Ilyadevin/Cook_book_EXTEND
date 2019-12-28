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


def get_ingredient(name_dishes, int_count):
    if name_dishes[0][0] == name_dishes[0][1]:
        for dishes in name_dishes[0]:
            for item, value in cook_book.items():
                dish = dishes
                if item == dish:
                    for val in list(value):
                            value_dict = {val['ingridient_name']: {'quantity': 2 * int(val['quantity']) * int_count,
                                                                   'measure': val['measure']}}
                            print(value_dict)
                    return
    else:
        for dishes in name_dishes[0]:
            for item, value in cook_book.items():
                dish = dishes
                if item == dish:
                    for value_correct in list(value):
                        value_dictionary = {value_correct['ingridient_name']: {'quantity': int(value_correct['quantity']) * int_count,
                                'measure': value_correct['measure']}}
                        print(value_dictionary)


def counting():
    while True:
        dish_list = []
        dish = input("Введите блюдо  ")
        dish_list.append(dish.split(", "))
        count = input('Введите количество блюд  ')
        int_count = int(count)
        get_ingredient(dish_list, int_count)


counting()
