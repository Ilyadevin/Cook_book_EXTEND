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
    for dishes in name_dishes[0]:
        for item, value in cook_book.items():
            dish = dishes
            if item == dish:
                print('В блюдо - ', item, 'необоходимы следующие ингридиенты: ')
                for val in list(value):
                    val_key = val['quantity']
                    int_val = int(val_key)
                    print(val['ingridient_name'], int_val * int_count, val['measure'])


def counting():
    while True:
        dish_list = []
        dish = input("Введите блюдо  ")
        dish_list.append(dish.split(", "))
        count = input('Введите количество блюд  ')
        int_count = int(count)
        get_ingredient(dish_list, int_count)


counting()
