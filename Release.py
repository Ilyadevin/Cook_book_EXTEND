with open('Список рецептов.txt') as f:
    cook_book = {}
    ingredients_dict = {}
    while True:
        ingredient_list = []
        food = f.readline().strip()
        for i in range(int(f.readline().strip(''))):
            ingredient = f.readline().strip().split('|')
            ingredient_list.append(
                {'ingridient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
        f.readline().strip()
        cook_book[food] = ingredient_list


        def dishes_lists(dishes, person_count):
            for key, value in cook_book.items():
                if key == dishes:
                    print(key)
                elif value == person_count:
                    print(value * person_count)
            return


        def command():
            while True:
                dishes = input("Введите блюдо  ")
                count = input(int('Введите количество блюд  '))
                dishes_lists(dishes, count)
