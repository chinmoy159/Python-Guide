# Program demonstrate the simple usage of try-except block
#
# try:      This block will test the excepted error to occur
# except:   Here you can handle the error
# else:     If there is no exception then this block will be executed
# finally:  Finally block always gets executed either exception is generated or not

def fnc_with_error(a, b):
    # A simple function that can generate ZeroDivisionError.
    return a/b


if __name__ == '__main__':
    t = int(input())  # number of test cases
    for it in range(0, t):
        try:
            a = int(input())
            b = int(input())
            res = fnc_with_error(a, b)
            print(res)
        except Exception as exc:
            print("Exception encountered: {0}".format(exc))
        else:
            print("Testcase successful")
