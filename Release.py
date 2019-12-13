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
            for key in cook_book.keys():
                if key == d:
                    print(key)
                    for value in cook_book.values():
                        for i in value:
                            for f in i.values():
                                print(f * p)
                else:
                    print('---------------------------------------------------------------')


        def counting():
            while True:
                dishes = input("Введите блюдо  ")
                count = input('Введите количество блюд  ')
                count_ints = int(count)
                dishes_lists(dishes, count_ints)


        counting()
