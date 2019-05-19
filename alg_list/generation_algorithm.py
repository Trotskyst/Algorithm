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
                if method == 'asc':
                    if list[j] > list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
                elif method == 'desc':
                    if list[j] < list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
            position += 1
        else:
            for j in range(list_len - position - 1, position - 1, -1):
                if method == 'asc':
                    if list[j] < list[j - 1]:
                        list[j], list[j - 1] = list[j - 1], list[j]
                elif method == 'desc':
                    if list[j] > list[j - 1]:
                        list[j], list[j - 1] = list[j - 1], list[j]

    return list


def sort_comb_sort(list, method='asc'):
    """ Сортировка списка расческой (comb sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    list_len = len(list)
    koef = 1.247330950103979
    if list_len > 1:
        step = list_len / koef
    else:
        step = 0
    while step > 1:
        step_round = round(step)
        for i in range(list_len - step_round):
            if method == 'asc':
                if list[i] > list[i + step_round]:
                    list[i], list[i + step_round] = list[i + step_round], list[i]
            elif method == 'desc':
                if list[i] < list[i + step_round]:
                    list[i], list[i + step_round] = list[i + step_round], list[i]
        step /= koef

    return list


def sort_shell_sort(list, method='asc'):
    """ Сортировка Шелла (Shell sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    list_len = len(list)
    koef = 2
    step = list_len // koef
    while step > 0:
        for i in range(list_len - step):
            j = i
            if method == 'asc':
                while j >= 0 and list[j] > list[j + step]:
                    list[j], list[j + step] = list[j + step], list[j]
                    j -= 1
            elif method == 'desc':
                while j >= 0 and list[j] < list[j + step]:
                    list[j], list[j + step] = list[j + step], list[j]
                    j -= 1
        step = int(step / 2)

    return list


def sort_quick_sort(list, method='asc'):
    """ Быстрая сортировка списка (quick sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    if list == []:
        return []
    else:
        pillar = list[0]
        less = sort_quick_sort([element for element in list[1:] if element < pillar])
        over = sort_quick_sort([element for element in list[1:] if element >= pillar])
        if method == 'asc':
            return less + [pillar] + over
        elif method == 'desc':
            return over + [pillar] + less


def sort_merge_sort(list, method='asc'):
    """ Сортировка списка слиянием (merge sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """
    if len(list) > 1:
        mid = len(list) // 2
        left_sublist = list[:mid]
        right_sublist = list[mid:]

        sort_merge_sort(left_sublist)
        sort_merge_sort(right_sublist)

        left_step = 0
        right_step = 0
        k = 0
        while left_step < len(left_sublist) and right_step < len(right_sublist):
            if method == 'asc':
                if left_sublist[left_step] < right_sublist[right_step]:
                    list[k] = left_sublist[left_step]
                    left_step += 1
                else:
                    list[k] = right_sublist[right_step]
                    right_step += 1
            elif method == 'desc':
                if left_sublist[left_step] > right_sublist[right_step]:
                    list[k] = left_sublist[left_step]
                    left_step += 1
                else:
                    list[k] = right_sublist[right_step]
                    right_step += 1
            k += 1

        while left_step < len(left_sublist):
            list[k] = left_sublist[left_step]
            left_step += 1
            k += 1

        while right_step < len(right_sublist):
            list[k] = right_sublist[right_step]
            right_step += 1
            k += 1

    return list


def sort_radix_sort(list, method='asc'):
    """ Поразрядная сортировка (radix  sort)
        Параметры функции
            1. Неотсортированный список (current_list)
            2. Метод сортировки (method):
                'asc' - по возрастанию (по умолчанию),
                'desc' - по убыванию
        Результат - отсортированный список
    """

    if not list:
        return []
    else:
        list_len = len(list)

        limit = list[0]
        for i in range(1, list_len):
            if list[i] > limit:
                limit = list[i]

        rank = 1

        while limit // rank > 0:

            rank_list = [0] * 10

            for i in range(0, list_len):
                index = list[i] // rank
                rank_list[index % 10] += 1

            for i in range(1, 10):
                rank_list[i] += rank_list[i - 1]

            result = [0] * list_len

            i = list_len - 1

            while i >= 0:
                index = list[i] // rank
                result[rank_list[index % 10] - 1] = list[i]
                rank_list[index % 10] -= 1
                i -= 1

            i = 0
            for i in range(0, list_len):
                list[i] = result[i]

            rank *= 10

        if method == 'desc':
            for i in range(0, list_len // 2):
                list[i], list[list_len - i - 1] = list[list_len - i - 1], list[i]

        return list

