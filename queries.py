queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

lists = ['one people', 'two person', 'three mini dogs', 'four tall girl', 'five guys']


'''
Дан список поисковых запросов.
 Получить распределение количества слов в них.
  Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
'''
def count_world(list_):
    new_list = []
    for i in list_:
        world = i.split()
        new_list.append(len(world))
    return new_list


def count_(new_list):
    new_list_set = set(new_list)
    new_list1 = list(new_list_set)
    new_list1.sort()
    return new_list1


def count_queries(new_list1, new_list):
    for a in new_list1:
        b = new_list.count(
            a)  # считаю количество значений из второго списка которые есть в 1м(сколько двухзначеных и трехзначных слов)
        yield f'Поисковых запросов из {a} слов: {b * 100 / len(queries):.2f} % '




print(count_world(lists))





