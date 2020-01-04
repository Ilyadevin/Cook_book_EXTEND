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


def get_ingredient(name_dishes, int_count, ):
    q = []
    for dishes in sorted(name_dishes[0]):
        for val in cook_book[dishes]:

            ingredients = {'quantity': int(val['quantity']) * int_count,
                           'measure': val['measure']}
            value_dict = {val['ingredient_name']: ingredients}

            for key, value in value_dict.items():
                if key in q:
                    ingredients['quantity'] += int(val['quantity'])
                    value_dict = {val['ingredient_name']: ingredients}
                    if key in value_dict:
                        del key, value
                        ingredients['quantity'] += int(val['quantity'])
                        value_dict = {val['ingredient_name']: ingredients}
                        print(value_dict)
                    else:
                        print(value_dict)
                else:
                    q.append(key)
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
