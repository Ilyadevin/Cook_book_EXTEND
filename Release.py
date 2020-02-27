class CookBook:
    def __init__(self, name_dishes, int_count):
        self.name_dishes, self.int_count = name_dishes, int_count
        self.cook_book = {}

    def load_dish(self):
        with open('Список рецептов.txt') as f:
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
                self.cook_book[food] = ingredient_list

    def get_ingredient(self):
        result = {}
        for dishes in sorted(self.name_dishes[0]):
            ingrs = self.cook_book[dishes]
            for ingredient in ingrs:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
                    if self.int_count >= 2:
                        result[ingredient['ingredient_name']]['quantity'] *= self.int_count
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
        CookBook(dish_list, int_count).get_ingredient()


counting()
