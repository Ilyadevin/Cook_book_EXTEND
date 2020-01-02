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
                {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
        f.readline().strip()
        cook_book[food] = ingredient_list


def get_ingredient(name_dishes, int_count):
    dishes_i = []
    s = []
    value_dict = {}
    for dishes in sorted(name_dishes[0]):
        dishes_i.append(dishes)
        dishes_i.count(dishes)
        s.append(dishes_i.count(dishes))
        for val in cook_book[dishes]:
            if dishes_i.count(dishes) == 1:
                value_dict = {val['ingredient_name']: {'quantity': int(val['quantity']) * int_count,
                                                       'measure': val['measure']}}
            elif dishes_i.count(dishes) >= 2:
                value_dict.update({val['ingredient_name']: {'quantity': 2 * int(val['quantity']) * int_count,
                                                            'measure': val['measure']}})
            print(value_dict)


def counting():
    while True:
        dish_list = []
        dish = input("Введите блюдо ")
        dish_list.append(dish.split(", "))
        count = input('Введите количество блюд ')
        int_count = int(count)
        get_ingredient(dish_list, int_count)


counting()
