# import json
import tabulate
# class Util:
#
#     @staticmethod
#     def list_students():
#         f = open("students.json",'r')
#         student_json_data = f.read()
#
#         student_list = json.loads(student_json_data)
#         for student in student_list["students"]:
#             print(student)
import json
import array
class Util:
    @staticmethod
    def list_students():
        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()
        for student in student_list["students"]:
            print(student)

    @staticmethod
    # def add_student():
    #     print("You are adding new student recorde")
    #     print("Enter student name")
    #     name = input()
    #
    #     print("Enter age")
    #     age = int(input())
    #
    #     f = open("students.json")
    #     student_list = json.loads(f.read())
    #     f.close()
    #
    #     students = student_list["students"]
    #     students.append({'name':name, 'age': age})
    #     student_list["students"] = students
    #
    #     js = json.dumps(student_list)
    #     f = open("students.json", 'w')
    #     f.write(js)
    #     f.close()
    #     for student in students:
    #         print(student)
    def add_student():
        print("Enter new student recorde")
        print("Enter student name")
        name = input()

        print("Enter student age")
        age = int(input())

        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()

        students = student_list["students"]
        students.append({'name':name, 'age':age})
        student_list["students"] = students
        js = json.dumps(student_list)

        f = open("students.json", 'w')
        f.write(js)
        f.close()
        for student in students:
            print(student)
    @staticmethod
    def display_all():
        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()
        for student in student_list["students"]:
            data = [['name', student["name"]], ['age', student["age"]]]
            print(tabulate.tabulate(data))

    @staticmethod
    def average_age():
        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()
        totalsum = 0
        count = 0
        for student in student_list["students"]:
            totalsum += student["age"]
            count += 1
        average = totalsum/count
        print("average student age: " + str(average))










