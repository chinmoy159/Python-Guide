# Program in Python to demonstrate Insertion Sorting algorithm
# Guide: https://www.geeksforgeeks.org/insertion-sort/
#
# author: spoorthi, shubhojeet
# date: Oct 31, 2020: 2000 hrs
import random


def insertion_sort(arr):
    size_of_array = len(arr)
    for i in range(1, size_of_array):
        num = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num


if __name__ == '__main__':
    arr = []
    size_of_array = int(input("Enter the number of elements: "))
    # Randomly generating numbers within the list: [0, 10007}
    for it in range(0, size_of_array):
        arr.append(random.randint(0, 1000000000007) % 10007)

    print("\nArray before sorting: {0}".format(arr))
    print("\n------------------------\n")

    insertion_sort(arr)
    print("After Sorting: {0}".format(arr))
