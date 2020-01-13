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
                {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
        f.readline().strip()
        cook_book[food] = ingredient_list


def get_ingredient(name_dishes, int_count, ):
    q = []
    result = {}
    for dishes in sorted(name_dishes[0]):
        ingrs = cook_book[dishes]
        for ingredient in ingrs:
            if ingredient['ingredient_name'] in result:
                result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
                if int_count >= 2:
                    result[ingredient['ingredient_name']]['quantity'] *= int_count
            else:
                result[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'],
                                                         'measure': ingredient['measure']}
    print(result)


def counting():
    while True:
        dish_list = []
        dish = input("Введите блюдо ")
        dish_list.append(dish.split(", "))
        count = input('Введите количество блюд ')
        int_count = int(count)
        get_ingredient(dish_list, int_count)


counting()
