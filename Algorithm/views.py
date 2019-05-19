from django.shortcuts import render, get_object_or_404, get_list_or_404
from alg_list.models import GroupAlgorithm, Algorithm
from random import randint
from alg_list.generation_algorithm import *
import time

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def index_view(request):
    algorithm_groups = GroupAlgorithm.objects.all()
    algorithms_menu = Algorithm.objects.all().order_by('group', 'id')
    data = {
        'algorithm_groups': algorithm_groups,
        'algorithms_menu': algorithms_menu,
    }
    return render(request, 'index.html', data)


def algorithm_view(request, **kwargs):
    group = kwargs['group']
    algorithm = kwargs['algorithm']
    algorithm_groups = get_object_or_404(GroupAlgorithm, slug=group)
    algorithms = get_object_or_404(Algorithm, slug=algorithm)
    algorithms_menu = Algorithm.objects.all().order_by('group', 'id')
    data = {
        'algorithm_groups': algorithm_groups,
        'algorithms': algorithms,
        'algorithms_menu': algorithms_menu,
    }
    return render(request, 'algorithm.html', data)


def generation_algorithm_view(request, **kwargs):
    id = kwargs['id']
    list_size = 10
    current_list = [randint(0, 101) for i in range(list_size)]
    # current_list = []
    sorted_list = current_list[:]
    if id == 1:
        sorted_list = sort_booble_sort(sorted_list)
    elif id == 2:
        sorted_list = sort_selection_sort(sorted_list)
    elif id == 4:
        sorted_list = sort_insertion_sort(sorted_list)
    elif id == 5:
        sorted_list = sort_shaker_sort(sorted_list)
    elif id == 6:
        sorted_list = sort_comb_sort(sorted_list)
    elif id == 7:
        sorted_list = sort_shell_sort(sorted_list)
    elif id == 8:
        sorted_list = sort_quick_sort(sorted_list)
    elif id == 9:
        sorted_list = sort_merge_sort(sorted_list)
    elif id == 10:
        sorted_list = sort_radix_sort(sorted_list)

    # print(current_list)
    # print(sorted_list)

    algorithm = get_object_or_404(Algorithm, id=id)
    data = {
        'current_list': current_list,
        'sorted_list': sorted_list,
        'algorithm': algorithm,
    }
    return render(request, 'generation_algorithm.html', data)


def speed_test_algorithm(request):
    count_tests = 5  # количество тестов
    max_list_size = 5000  # максимальный размер списка
    max_value_element = 1000  # максимальное значение элементов списка
    count_algorithm = 9  # количество сравниваемых алгоритмов

    algorithms_list = Algorithm.objects.filter(group_id=1)

    timer = {algorithms_list[i]: 0 for i in
             range(count_algorithm)}  # генератор словаря, в нём будут храниться результаты

    count_algorithm += 1
    timer['Встроенная сортировка Python'] = 0

    for counter in range(count_tests):
        list_size = randint(0, max_list_size)
        current_list = [randint(0, max_value_element + 1) for i in range(list_size)]

        for i in range(count_algorithm):
            start_time = time.time()
            sorted_list = current_list[:]
            if i == 0:
                sort_booble_sort(sorted_list)
            elif i == 1:
                sort_selection_sort(sorted_list)
            elif i == 2:
                sort_insertion_sort(sorted_list)
            elif i == 3:
                sort_shaker_sort(sorted_list)
            elif i == 4:
                sort_comb_sort(sorted_list)
            elif i == 5:
                sort_shell_sort(sorted_list)
            elif i == 6:
                sort_quick_sort(sorted_list)
            elif i == 7:
                sort_merge_sort(sorted_list)
            elif i == 8:
                sort_radix_sort(sorted_list)
            elif i == 9:
                sorted(sorted_list)

            if i == 9:
                timer['Встроенная сортировка Python'] += time.time() - start_time
            else:
                timer[algorithms_list[i]] += time.time() - start_time

    timer_list = list(timer.items())
    # print('timer_list1 ', timer_list)
    timer_list.sort(key=lambda i: i[1])
    # print('timer_list2 ', timer_list)
    data = {
        'count_tests': count_tests,
        'max_list_size': max_list_size,
        'max_value_element': max_value_element,
        'timer_list': timer_list,
    }
    return render(request, 'speed_test_algorithm.html', data)
