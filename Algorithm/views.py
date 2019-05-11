from django.shortcuts import render, get_object_or_404, get_list_or_404
from alg_list.models import GroupAlgorithm, Algorithm
from random import randint
from alg_list.generation_algorithm import *

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
    list_size = 100
    current_list = [randint(1, 1000)/randint(1, 1000) for i in range(list_size)]
    sorted_list = current_list[:]

    if id == 1:
        sorted_list = sort_booble_sort(sorted_list)
    elif id == 2:
        sorted_list = sort_selection_sort(sorted_list)
    elif id == 4:
        sorted_list = sort_insertion_sort(sorted_list)
    elif id == 5:
        sorted_list = sort_shaker_sort(sorted_list)

    # print(current_list)
    # print(sorted_list)

    algorithm = get_object_or_404(Algorithm, id=id)
    data = {
        'current_list': current_list,
        'sorted_list': sorted_list,
        'algorithm': algorithm,
    }
    return render(request, 'generation_algorithm.html', data)
