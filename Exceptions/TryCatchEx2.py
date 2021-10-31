# Program demonstrate the usage of try-except in multi-threading
#
# try:      This block will test the excepted error to occur
# except:   Here you can handle the error
# else:     If there is no exception then this block will be executed
# finally:  Finally block always gets executed either exception is generated or not
import sys
import time
from multiprocessing import Process
import traceback


def fnc_with_error(a, b):
    # A simple function that can generate ZeroDivisionError.
    return a/b


def Thread():
    t = 5
    a = [18, 28, 3, 4, 5]
    b = [4, 2, 0, 4, 1]
    for it in range(0, t):
        res = fnc_with_error(a[it], b[it])
        print("{0} || Testcase successful.".format(res))


if __name__ == '__main__':
    multi_process = Process(target=Thread)
    multi_process.start()
    multi_process.join()

    # Adding a little time delay to ensure that the prints in the threaded process come before the parent process
    time.sleep(3)

    print("Thread invoked successfully. Status: {0} PID: {1}".format("ALIVE" if multi_process.is_alive() else "DEAD",
                                                                     multi_process.pid))
    print("Execution of this line denotes that the exception in child thread is not propagated to the parent thread.")

    print(sys.exc_info())

    print("Following is the exception that occurred in the child process: {0}".format(traceback.print_exc()))
