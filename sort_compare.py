import argparse
# other imports go here

import random
import time
def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end_time = time.time()
    return end_time - start_time


def shellSort(a_list):
    start_time = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)

        sublistcount = sublistcount // 2

    end_time = time.time()
    return end_time - start_time


def gapInsertionSort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentvalue:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = currentvalue


def python_sort(a_list):

    start_time = time.time()
    a_list.sort()
    end_time = time.time()
    return end_time - start_time



if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        total_time_insertion = 0
        total_time_shell = 0
        total_time_python = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)


            total_time_insertion += insertion_sort(mylist[:])


            total_time_shell += shellSort(mylist[:])


            total_time_python += python_sort(mylist[:])

        avg_time_insertion = total_time_insertion / 100
        avg_time_shell = total_time_shell / 100
        avg_time_python = total_time_python / 100

        print(  f"Insertion sort took {avg_time_insertion:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Shell sort took {avg_time_shell:10.7f} seconds to run, on average for a list of {the_size} elements")
        print(f"Python sort took {avg_time_python:10.7f} seconds to run, on average for a list of {the_size} elements")
