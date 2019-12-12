with open('Список рецептов.txt') as f:
  cook_book = {}
  ingredients_dict = {}
  while True:
    ingredient_list = []
    food = f.readline().strip()
    for i in range(int(f.readline().strip(''))):
      ingredient = f.readline().strip().split('|')
      ingredient_list.append({'ingridient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
    f.readline().strip()
    cook_book[food] = ingredient_list
    print(cook_book)