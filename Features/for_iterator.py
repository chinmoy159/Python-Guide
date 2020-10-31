# Interesting feature in for loop in Python
#     the variable over which _for_ iterates has a separate context altogether.
#     Therefore, we may use the same variable in inner loops as well,
#     and the outer loop will maintain it's context
# The below program will demonstrate the functionality
#
# author: shubhojeet
# date: Oct 31, 2020: 1900 hrs


def for_looping(starting_point):
    print("Starting value: {0}".format(starting_point))

    # Now, let us start a for-loop to iterate over the mentioned variable
    # OUTER LOOP
    for starting_point in range(1, 10):
        str_msg = "Value: {0}".format(starting_point)
        for starting_point in range (1, starting_point):
            # INNER LOOP
            str_msg = "{0} {1}".format(str_msg, starting_point*starting_point)
        print(str_msg)
        # After this, the outer loop will start from the next number in the list

    # Now, let's see what the value of the above variable is, outside the for_loop
    print("Final value of starting_point: {0}".format(starting_point))


if __name__ == "__main__":
    starting_point = int(input("Enter the starting number :"))
    for_looping(starting_point=starting_point)

    print("--------------------------------------------\n")
    print("An explanation to this functionality is as follows -")
    print("For loop in Python iterates over a list maintaining an index for the item "
          "which it is referring to in the current iteration.")
    print("That means, once an iteration is complete the value goes to the next item in the list "
          "even if the var is modified within the loop.")
    print("In the above code, the outer loop is iterating over a list : [1, 2, ,3 ,4, 5, 6, 7, 8, 9]")
    print("while the inner loop iterates over the respective list : [1 .. outer_loop item]")
    print("\nAnother point to be noted is that the value of the variable finally changes and it's just as expected.")
    print("Let\'s see if you can find the explanation for the value ;)")
