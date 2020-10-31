# Program in Python to demonstrate Bubble Sorting algorithm
# Guide: https://www.geeksforgeeks.org/bubble-sort/
#
# author: shubhojeet
# date: Oct 31, 2020: 2300 hrs
import random


def bubble_sort(arr):
    size_of_array = len(arr)
    i = 0
    while i < size_of_array:
        j = 0
        while j < size_of_array - i - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1
    return


if __name__ == '__main__':
    arr = []
    size_of_array = int(input("Enter the number of elements: "))
    # Randomly generating numbers within the list: [0, 10007}
    for it in range(0, size_of_array):
        arr.append(random.randint(0, 1000000000007) % 10007)

    print("\nArray before sorting: {0}".format(arr))
    print("\n------------------------\n")

    bubble_sort(arr)
    print("After Sorting: {0}".format(arr))
