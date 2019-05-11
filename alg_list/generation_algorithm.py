def sort_booble_sort(list, method='asc'):
    """ Сортировка списка пузырьком (booble sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    list_len = len(list)
    for i in range(list_len - 1):
        for j in range(list_len - i - 1):
            if method == 'asc':
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
            elif method == 'desc':
                if list[j] < list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]

    return list


def sort_selection_sort(list, method='asc'):
    """ Сортировка списка выбором (selection sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    list_len = len(list)
    for i in range(list_len - 1):
        i_sort = i
        for j in range(i + 1, list_len, 1):
            if method == 'asc':
                if list[j] < list[i_sort]:
                    i_sort = j
            elif method == 'desc':
                if list[j] > list[i_sort]:
                    i_sort = j
        if i_sort != i:
            list[i], list[i_sort] = list[i_sort], list[i]

    return list


def sort_insertion_sort(list, method='asc'):
    """ Сортировка вставками (insertion sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    list_len = len(list)
    print(list)
    for i in range(1, list_len):
        current_value = list[i]
        j = i - 1
        if method == 'asc':
            while j >= 0 and list[j] > current_value:
                list[j + 1] = list[j]
                j -= 1
        elif method == 'desc':
            while j >= 0 and list[j] < current_value:
                list[j + 1] = list[j]
                j -= 1
        list[j + 1] = current_value

    return list

def sort_shaker_sort(list, method='asc'):
    """ Шейкерная  сортировка списка (shaker sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    list_len = len(list)
    position = 0
    for i in range(list_len - 1):
        if i % 2 == 0:
            for j in range(position, list_len - position - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
            position += 1
        else:
            for j in range(list_len - position - 1, position - 1, -1):
                if list[j] < list[j - 1]:
                    list[j], list[j - 1] = list[j - 1], list[j]


    # for j in range(list_len - i - 1):
        #     if method == 'asc':
        #         if list[j] > list[j + 1]:
        #             list[j], list[j + 1] = list[j + 1], list[j]
        #     elif method == 'desc':
        #         if list[j] < list[j + 1]:
        #             list[j], list[j + 1] = list[j + 1], list[j]

    return list
