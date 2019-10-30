class Searching:
    def __init__(self, list_to_be_used, value):
        self.list_to_be_used = list_to_be_used
        self.value = value

    @staticmethod
    def equality_check(a, b):
        if type(a) == str:
            return a.__eq__(b)
        return a == b

    @staticmethod
    def compare_to(a, b):
        # a < b :: -1
        # a == b :: 0 || won't be needed
        # a > b :: 1
        if type(a) == str:
            return -1 if a < b else 1
        return -1 if a < b else 1

    def linear_search(self):
        it = 0
        while it < len(self.list_to_be_used):
            if self.equality_check(self.value, self.list_to_be_used[it]):
                break
            it += 1
        if it == len(self.list_to_be_used):
            return -1
        return it

    def binary_searching(self):
        lb = 0
        ub = len(self.list_to_be_used) - 1
        mid = 0
        while lb <= ub:
            mid = (lb + ub) / 2
            if self.equality_check(self.list_to_be_used[mid], self.value):
                break
            res = self.compare_to(self.list_to_be_used[mid], self.value)
            if res == -1:
                lb = mid + 1
            else:
                ub = mid + 1
        if lb > ub:
            return -1
        return mid


# checked for integer arrays
if __name__ == '__main__':
    num = int(input("Enter number of elements - "))
    list = [int(input("Element - ")) for it in range(0, num)]
    val = int(input("Enter element to be search"))
    obj = Searching(list_to_be_used=list, value=val)
    print("Linear Search results = {0}".format(obj.linear_search()))
    print("Binary Search results = {0}".format(obj.binary_searching()))
