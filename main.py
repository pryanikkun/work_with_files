import os


def make_dict_ingredient(line):
    """ Создает из строки словарь """
    ingredient, quantity, measure = line.split(' | ')
    return {'ingredient_name': ingredient,
            'quantity': int(quantity),
            'measure': measure}


def make_cook_book():
    """ Заполняет словарь cook_book """
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            if '|' in line:
                cook_book[dish].append(make_dict_ingredient(line.strip()))
            elif not line.strip().isdigit() and line.strip() != '':
                dish = line.strip()
                cook_book[dish] = []

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """ Расчет продуктов для блюд по кол-ву персон """
    cook_book = make_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list.keys():
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient_name]['quantity'] += \
                    ingredient['quantity'] * person_count
    return shop_list


def union_files():
    """ Объединение файлов в один """
    files = {
        '1.txt': {},
        '2.txt': {},
        '3.txt': {}
    }
    for file_name, file_param in files.items():
        file_path = os.path.join(os.getcwd(), 'sorted', file_name)
        with open(file_path, encoding='utf-8') as file:
            lines = file.readlines()
            file_param['length'] = str(len(lines))
            file_param['text'] = ''.join(lines)
    sorted_files = sorted(files.items(), key=lambda item: item[1]['length'])

    with open('result_file.txt', 'wt', encoding='utf-8') as file:
        for file_name, file_param in sorted_files:
            file.write(file_name + '\n')
            file.write(file_param['length'] + '\n')
            file.write(file_param['text'] + '\n')
