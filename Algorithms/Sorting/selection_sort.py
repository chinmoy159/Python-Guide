# Program in Python to demonstrate Selection Sorting algorithm
# Guide: https://www.geeksforgeeks.org/selection-sort/
#
# author: shubhojeet
# date: Oct 31, 2020: 2000 hrs
import random


def selection_sort(arr):
    size_of_array = len(arr)
    for i in range(0, size_of_array - 1):
        pos = i

        for j in range(i + 1, size_of_array):
            if arr[pos] > arr[j]:
                pos = j

        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp


if __name__ == '__main__':
    arr = []
    size_of_array = int(input("Enter the number of elements: "))
    # Randomly generating numbers within the list: [0, 10007}
    for it in range (0, size_of_array):
        arr.append(random.randint(0, 1000000000007) % 10007)

    print("\nArray before sorting: {0}".format(arr))
    print("\n------------------------\n")

    selection_sort(arr)
    print("After Sorting: {0}".format(arr))
