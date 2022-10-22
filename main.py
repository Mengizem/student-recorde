# def main():
#     print("Welcome to class IT-566")
#     print("Enter '1' to list all the students")
#     n = int(input())
#     print(n)
#     print(type(n))
#
#
# main()
# from util import Util
# def main():
#     print("welcome to class IT_566")
#     print("enter '1' to see all the list of the students")
#     n = int(input())
#
#     if n == 1:
#         Util.list_students()
#     else:
#         print("invalid choice")
#
# main()
from util import Util


def main():
    print("welcome to student console app")

    while 1:
        print("Enter 1 to")
        print("enter '2' to add student")
        print("enter '3' to display all student data")
        print("enter '4' to calculate the average age")
        print("enter '5' to exit app")

        n = int(input())
        if n == 1:
            Util.list_students()
        elif n == 2:
            Util.add_student()
        elif n == 3:
            Util.display_all()
        elif n == 4:
            Util.average_age()
        elif n == 5:
            break
        else:
            print("invalid choice")





main()
