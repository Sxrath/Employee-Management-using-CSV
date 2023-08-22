import csv
import csv as c
import os


class HR:
    def __init__(self, id, name, department, place, salary):
        self.id = id
        self.name = name
        self.department = department
        self.place = place
        self.salary = salary

    def insert(self):
        file_exists = os.path.isfile("em_det.csv")
        with open("em_det.csv", "a", newline="") as details:
            heads = ["id", "name", "department", "place", "salary"]
            file = c.DictWriter(details, fieldnames=heads)

            if not file_exists:
                file.writeheader()

            file.writerow({"id": self.id, "name": self.name, "department": self.department, "place": self.place,
                           "salary": self.salary})

    def update(self):

        with open("em_det.csv", "r") as file:
            employee = list(csv.DictReader(file))

            id = input("enter id  again to confirmation.......")
            for i in employee:
                if i["id"] == id:
                    i["name"] = self.name
                    i["department"] = self.department
                    i["place"] = self.place
                    i["salary"] = self.salary
                    # print(employee)
        with open("em_det.csv", "w") as details:
            heads = ["id", "name", "department", "place", "salary"]
            emp = csv.DictWriter(details, fieldnames=heads)
            emp.writeheader()
            for i in employee:
                # print(i)
                emp.writerow(i)
            print('your data successfully updated...')


def insertion(id, name, dept, place, salary):
    obj = HR(id, name, dept, place, salary)
    obj.insert()
    print('your data successfully inserted...')


def upd():
    id = input("enter the id to update")
    name = input("enter name to update/otherwise write old name")
    department = input("enter department to update/otherwise write old dprtmnt")
    place = input("enter place to update/otherwise write old place")
    salary = input("enter salary to update/otherwise write old salary")

    obj = HR(id, name, department, place, salary)
    obj.update()


def view():
    with open("em_det.csv", "r") as file:
        reader = c.DictReader(file)
        for i in reader:
            print("id:", i["id"], "name:", i["name"], "department:", i["department"], "place:", i["place"], "salary:",
                  i["salary"])


# def delete():
#         emp_id = input("Enter the ID to delete: ")
#         with open('em_det.csv', 'r') as file:
#             employees = list(c.DictReader(file))
#
#         found = False
#         updated_employees = []
#         for emp in employees:
#             if emp["id"] == emp_id:
#                 print(emp)
#                 found = True
#             else:
#                 updated_employees.append(emp)
#
#         if found:
#             with open('em_det.csv', 'w', newline='') as file:
#                 heads = ["id", "name", "department", "place", "salary"]
#                 csv_writer = c.DictWriter(file, fieldnames=heads)
#                 csv_writer.writeheader()
#                 csv_writer.writerows(updated_employees)
#             print("Employee data deleted successfully.")
#         else:
#             print("Employee with the given ID not found.")
def delete():
    id = input('Enter the id to delete ')
    with open("em_det.csv") as file:
        emp = list(csv.DictReader(file))
        for i in emp:
            if i["id"] == id:
                emp.remove(i)
    file.close()
    with open("em_det.csv", "w") as file:
        heads = ["id", "name", "department", "place", "salary"]
        employ = csv.DictWriter(file, fieldnames=heads)
        employ.writeheader()

        for i in emp:
            employ.writerow(i)
        print("data deleted successfuly.......")


# def update():
#
#     with open("em_det.csv","r")as file:
#         employee=list(csv.DictReader(file))
#
#         id=input("enter id do you want to update")
#         for i in employee:
#             if i["id"] == id:
#                 new_name = input("enter name to update/otherwise write old name")
#                 new_department = input("enter department to update/otherwise write old dprtmnt")
#                 new_place = input("enter place to update/otherwise write old place")
#                 new_salary = input("enter salary to update/otherwise write old salary")
#                 i["name"]=new_name
#                 i["department"]=new_department
#                 i["place"]=new_place
#                 i["salary"]=new_salary
#                 # print(employee)
#     with open("em_det.csv","w")as details:
#         heads = ["id", "name", "department", "place", "salary"]
#         emp = csv.DictWriter(details, fieldnames=heads)
#         emp.writeheader()
#         for i in employee:
#             # print(i)
#             emp.writerow(i)


class Employee():
    def _init_(self, id):
        self.id = id

    def view(id):
        with open("em_det.csv", "r") as file:
            reader = c.DictReader(file)
            for i in reader:
                print("id:", i["id"], "name:", i["name"], "department:", i["department"], "place:", i["place"],
                      "salary:", i["salary"])


def mainHR():
    print("1-insert")
    print("2-View")
    print("3-Delete")
    print("4-Update")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        id = input("enter id")
        name = input("Enter the name: ")
        department = input("Enter department: ")
        place = input("Enter place: ")
        salary = input("Enter salary: ")
        insertion(id, name, department, place, salary)
        x = input("do you want to continue? (y/n)")
        if x == "y":
            mainHR()
    if choice == 2:
        view()

        x = input("do you want to continue? (y/n)")
        if x == "y":
            mainHR()

    if choice == 3:
        delete()
        x = input("do you want to continue? (y/n)")
        if x == "y":
            mainHR()

    if choice == 4:
        upd()
        x = input("do you want to continue? (y/n)")
        if x == "y":
            mainHR()


def mainEM():
    selector = input('Enter your choice\n'
                     '1 . View')
    if selector == '1':
        id = input('Enter your id :')
        obj_view = Employee()
        obj_view.view()
    else:
        print('Invalid option')


def enter():
    x = int(input('You want to join as\n1. HR\n2. Employee\nSelect from the above options :'))
    if x == 1:
        mainHR()
    elif x == 2:
        mainEM()
    else:
        print("enter valid choice")


enter()
