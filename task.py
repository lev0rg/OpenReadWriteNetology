# 1-ое задание
def create_cookbook(filename):
    with open(filename, encoding='utf-8') as file:
        cook_book = {}
        for text in file.read().split('\n\n'):
            name, count, *args = text.split('\n')
            ingredients = []
            for arg in args:
                ingredient_name, quantity, measure = arg.split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[name] = ingredients
        return cook_book

print(create_cookbook('recipes.txt'))

# 2-ое задание
def get_shop_list_by_dishes(dishes, person_count):
    cookbook = create_cookbook('recipes.txt')
    cook_dict = {}
    for dish, ingredients in cookbook.items():
        if dish in dishes:
            for ingr in ingredients:
                ingr_name = ingr['ingredient_name']
                if ingr_name not in cook_dict:
                    cook_dict[ingr_name] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
                else:
                    cook_dict[ingr_name]['quantity'] += ingr['quantity'] * person_count
    return cook_dict

print(get_shop_list_by_dishes(['Омлет','Фахитос'], 3))

# 3-е задание
files_list = ['1.txt', '2.txt', '3.txt']
content_list = []
for file in files_list:
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
        content_list.append((file, len(lines), lines))

content_list.sort(key=lambda x: x[1])

with open('general.txt', 'w', encoding='utf-8') as f_general:
    for file_name, line_count, lines in content_list:
        f_general.write(file_name + '\n')
        f_general.write(str(line_count) + '\n')
        f_general.writelines(lines)
        f_general.write('\n')

















        


            
    



        


