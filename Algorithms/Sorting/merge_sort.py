# Program in Python to demonstrate Merge Sorting algorithm
# Guide: https://www.geeksforgeeks.org/merge-sort/
#
# author: shubhojeet
# date: Oct 31, 2020: 2000 hrs
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_arr = []
    right_arr = []
    for it in range(0, mid):
        left_arr.append(arr[it])
    for it in range(mid, len(arr)):
        right_arr.append(arr[it])

    # Call merge sort on the first half
    merge_sort(left_arr)

    # Call merge sort on the second half
    merge_sort(right_arr)

    # Now, merging the sorted array
    it_l = 0
    it_r = 0
    it = 0
    while it_l < len(left_arr) and it_r < len(right_arr):
        if left_arr[it_l] <= right_arr[it_r]:
            arr[it] = left_arr[it_l]
            it_l += 1
        else:
            arr[it] = right_arr[it_r]
            it_r += 1
        it += 1
    while it_l < len(left_arr):
        arr[it] = left_arr[it_l]
        it += 1
        it_l += 1
    while it_r < len(right_arr):
        arr[it] = right_arr[it_r]
        it += 1
        it_r += 1


if __name__ == '__main__':
    arr = []
    size_of_array = int(input("Enter the number of elements: "))
    # Randomly generating numbers within the list: [0, 10007}
    for it in range(0, size_of_array):
        arr.append(random.randint(0, 1000000000007) % 10007)

    print("\nArray before sorting: {0}".format(arr))
    print("\n------------------------\n")

    merge_sort(arr)
    print("After Sorting: {0}".format(arr))
