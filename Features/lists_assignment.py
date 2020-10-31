# This program demonstrates the difference in the ways an assignment operator is used for lists in Python
#
# author: shubhojeet
# date: Oct 31, 2020: 2330 hrs
import random
if __name__ == '__main__':
    arr = []
    size_of_array = int(input("Enter size of array: "))
    for it in range(0, size_of_array):
        arr.append(random.randint(0, 1000000000007) % 10007)

    # the following line will create an alias
    arr_copy0 = arr
    # any changes in arr will be reflected in arr_copy0 and vice versa

    # this creates a full copy for the list
    arr_copy1 = arr.copy()
    # changes are not reflected in one another

    # line 20, 21 vs line 23
    arr_copy2 = []
    arr_copy3 = []
    # changes in copy2 and copy3 are independent of each other
    arr_copy4 = arr_copy5 = []
    # changes in copy4 & copy5 are reflected to one another

    for it in range(0, len(arr)//2):
        arr_copy2.append(arr[it])
        arr_copy4.append(arr[it])
    for it in range(len(arr)//2, len(arr)):
        arr_copy3.append(arr[it])
        arr_copy5.append(arr[it])

    # slight modification of a value in arr
    arr[random.randint(0, 1000000007)%len(arr)] = -1

    # using id(object) to print the address of the list as well.

    print("arr: {0}\n\taddress: {1}".format(arr, id(arr)))
    print("copy0: {0}\n\tshallow copy\taddress: {1}".format(arr_copy0, id(arr_copy0)))
    print("copy1: {0}\n\tdeep copy\taddress: {1}".format(arr_copy1, id(arr_copy1)))
    print("copy2: {0}\n\taddress: {1}".format(arr_copy2, id(arr_copy2)))
    print("copy3: {0}\n\taddress: {1}".format(arr_copy3, id(arr_copy3)))
    print("copy4: {0}\n\taddress: {1}".format(arr_copy4, id(arr_copy4)))
    print("copy5: {0}\n\taddress: {1}".format(arr_copy5, id(arr_copy5)))
