"""
Content of a student list: Student objects

Content of a course list:
    - Each element is a list s.t. the first element is the Course object, second is list of marks
    - The mark list has its elements' indices correspond to that of student list (aka student index 0 can find their mark in index 1 of the mark list, and so on)
--> [[Course, <marks>], [Course, <marks>]] (<marks> is NOT an actual list!)
"""

import uuid

class Student:
    def __init__(self):
        self.id_ = ""
        self.name = ""
        self.dob = ""

    def insert_info(self):
        self.id_ = input("Input student ID: ")
        self.name = input("Input student name: ")
        self.dob = input("Input date of birth: ")

class Course:
    def __init__(self):
        self.id_ = ""
        self.name = ""
        self.has_mark = False

    def insert_info(self):
        self.id_ = input("Input course ID: ")
        self.name = input("Input course name: ")

class CourseMarkManagement:
    courls_ls = []

    def __init__(self, instance_id):
        self.cournum = 0
        self.courls = []
        self.instance_id = instance_id
        CourseMarkManagement.courls_ls.append(self)
    
    # not in use for now...
    @classmethod
    def show_all_courls(cls):
        for i in range(len(cls.courls_ls)):
            print("{}. {}".format(i, cls.courls_ls[i].instance_id))

    @classmethod
    def find_courls(cls, inst_id):
        for i in range(len(cls.courls_ls)):
            if inst_id == cls.courls_ls[i].instance_id.__str__():
                return i
        return -1

    # insert courses into course list
    def insert_cour(self, studnum):
        self.cournum = int(input("Enter number of courses: "))
        enter_mark = input("Would you like to enter marks while creating courses? [y/<any other key>]: ")
        for i in range(self.cournum):

            # create a list sub_courls which contains a Course object and a mark list
            sub_courls = []
            cour = Course()
            cour.insert_info()
            sub_courls.append(cour)
            self.courls.append(sub_courls)

            # if the user wants to enter marks right away
            if enter_mark.lower() == 'y':
                self.insert_mark(studnum, i)
    
    # actually not in use
    def _find_cour(self, courid, courname):
        if courid == "":
            for i in range(self.cournum):
                if courname.lower() == self.courls[i][0].name.lower():
                    return i
        else:
            for i in range(self.cournum):
                if courid.lower() == self.courls[i][0].id.lower():
                    return i
        return -1
    
    # param_idx == -1: enter marks for all courses
    # param_idx != -1: enter marks for the course at index <param_idx>
    def insert_mark(self, studnum, param_idx):
        print("Order of input follows the student list")
        if param_idx != -1:
            for i in range(studnum):
                mark = float(input("Input student {} mark: ".format(i)))
                self.courls[param_idx].append(mark)
            self.courls[param_idx][0].has_mark = True
        else:
            for i in range(self.cournum):
                for j in range(studnum):
                    mark = float(input("Input student {} mark: ".format(j)))
                    self.courls[i].append(mark)
                self.courls[i][0].has_mark = True

    def show_all_cour(self):
        if self.cournum == 0:
            print("No courses to show")
        for i in range(self.cournum):
            print("{}. {} - {}".format(i, self.courls[i][0].id_, self.courls[i][0].name))

    def show_stud_mark(self, cour_idx, stud_idx):
        # show all marks if cour_idx == -1
        if cour_idx == -1:
            for i in range(self.cournum):
                if self.courls[i][0].has_mark == False:
                    print("No recorded mark for {} - {}".format(self.courls[i][0].id_, self.courls[i][0].name))
                else:
                    print("{} - {}: {}".format(self.courls[i][0].id_, self.courls[i][0].name, self.courls[i][stud_idx + 1]))
        else:
            if self.courls[cour_idx][0].has_mark == False:
                print("No recorded mark")
            else:
                print("{} - {}: {}".format(self.courls[cour_idx][0].id_, self.courls[cour_idx][0].name, self.courls[cour_idx][stud_idx + 1]))
    
    def show_cour_mark(self, cour_idx):
        if self.cournum == 0:
            print("No courses to show")
        else:
            # show all marks if cour_idx == -1
            if cour_idx == -1:
                for i in range(self.cournum):
                    print("{} - {}".format(self.courls[i][0].id_, self.courls[i][0].name))
                    print(self.courls[i][1:])
                    print()
            else:
                print("{} - {}".format(self.courls[cour_idx][0].id_, self.courls[cour_idx][0].name))
                print(self.courls[cour_idx][1:])

    def mod_mark(self, cour_idx, stud_idx):
        # modify all marks if cour_idx == -1
        if cour_idx == -1:
            for i in range(self.cournum):
                if self.courls[i][0].has_mark == False:
                    print("No marks for {} - {} to modify".format(self.courls[i][0].id_, self.courls[i][0].name))
                else:
                    mark = float(input("New mark for {} - {}: ".format(self.courls[i][0].id_, self.courls[i][0].name_)))
                    self.courls[i][stud_idx + 1] = mark
        else:
            if self.courls[cour_idx][0].has_mark == False:
                print("No marks to modify")
            else:
                mark = float(input("New mark: "))
                self.courls[cour_idx][stud_idx + 1] = mark

    def mod_cour(self, cour_idx):
        if self.cournum == 0:
            print("No courses to modify")
        else:
            # modify all courses if cour_idx == -1
            if cour_idx == -1:
                for i in range(self.cournum):
                    print("{}. {} - {}".format(i, self.courls[i][0].id_, self.courls[i][0].name))
                    new_id = input("New course ID (leave blank if no changes): ")
                    new_name = input("New course name (leave blank if no changes): ")
                    if new_id != "":
                        self.courls[i][0].id_ = new_id
                    if new_name != "":
                        self.courls[i][0].name = new_name
            else:
                new_id = input("New course ID (leave blank if no changes): ")
                new_name = input("New course name (leave blank if no changes): ")
                if new_id != "":
                    self.courls[cour_idx][0].id_ = new_id
                if new_name != "":
                    self.courls[cour_idx][0].name = new_name


class StudentManagement:
    studls_ls = []

    def __init__(self):
        self.studnum = 0
        self.studls = []
        self.name = ""
        self.instance_id = uuid.uuid4()
        StudentManagement.studls_ls.append(self)

    def __str__(self):
        if self.name != "":
            return self.name
        else:
            return self.instance_id

    @classmethod
    def show_all_studls(cls):
        if len(cls.studls_ls) == 0:
            print("No student list to show")
        else:
           for i in range(len(cls.studls_ls)):
               print("{}. {}".format(i, cls.studls_ls[i].__str__()))

    @classmethod
    def find_studls(cls, inst_id):
        for i in range(len(cls.studls_ls)):
            if inst_id == cls.studls_ls[i].instance_id.__str__():
                return i
        return -1

    # create a new student list
    def create_list(self):
        self.studnum = int(input("Enter number of students: "))

        # create a new course list linked to this student list
        linked_courls = CourseMarkManagement(self.instance_id)

        nom = input("Enter a name for this list (leave blank for default): ")
        if nom != "":
            self.name = nom

        # filling student list
        for i in range(self.studnum):
            stud = Student()
            stud.insert_info()
            self.studls.append(stud)

        ans = input("Would you like to enter the courses for this student list right now? [y/<any other key>]: ")
        if ans.lower() == 'y':
            linked_courls.insert_cour(self.studnum)

    # goes with show_a_stud(), mod_info() (ofc can use it whenever user wants to search for student but ok)
    def find_stud_idx(self, stud_id):
        for i in range(self.studnum):
            if stud_id.lower() == self.studls[i].id_.lower():
                return i
        return -1
    
    def show_all_stud(self):
        for i in range(self.studnum):
            print("{}. {} - {} - {}".format(i, self.studls[i].id_, self.studls[i].name, self.studls[i].dob))
        print()
    
    # only accept ID as other information cannot uniquely identify a student
    def show_a_stud(self, stud_idx):
        print("{} - {}".format(self.studls[stud_idx].name, self.studls[stud_idx].dob))

    def mod_info(self, stud_idx):
        current_stud = self.studls[stud_idx]
        self.show_a_stud(stud_idx)
        new_id = input("New student ID (leave blank if no changes): ")
        new_name = input("New student name (leave blank if no changes): ")
        new_dob = input("New date of birth (leave blank if no changes): ")
        if new_id != "":
            current_stud.id_ = new_id
        if new_name != "":
            current_stud.name = new_name
        if new_dob != "":
            current_stud.dob = new_dob

# remember which student and course list are selected
selected_student_list = None
selected_cour_list = None

# prompt
option_ls = """0. Select a student list
1. Create a student list
2. Insert courses and/or marks for a student list
3. Show all students in a list
4. Show all student lists
5. Show student personal information
6. Show all courses linked to the selected student list
7. Show student marks
8. Show all marks of a course linked to the selected student list
9. Modify student personal information
10. Modify student marks
11. Modify course information
12. Quit
"""

# main loop
while True:
    stud_length = len(StudentManagement.studls_ls)
    cour_length = len(CourseMarkManagement.courls_ls)
    sel_cour = None
    
    print()
    print(option_ls)
    if selected_student_list == None:
        print("No student list is currently selected. Available actions: 0, 1, 4, 12")
    else:
        print("Student list {} is currently selected".format(selected_student_list.__str__()))

    sel = int(input("Select an action: "))
    if selected_student_list == None:
        if sel not in [0, 1, 4, 12]:
            print("No student list is currently selected. Available actions: 0, 1, 4, 12")
            continue

    # action 0: select a student list
    if sel == 0:
        if stud_length == 0:
            print("No student list available")
        else:
            StudentManagement.show_all_studls()
            while True:
                sel_ls = int(input("Select a student list: "))
                if sel_ls > -1 and sel_ls < stud_length:
                    break
            selected_student_list = StudentManagement.studls_ls[sel_ls]
            selected_cour_list = CourseMarkManagement.courls_ls[sel_ls]
            print("Student list {} is now selected".format(selected_student_list.__str__()))
    
    # action 1: create a student list
    elif sel == 1:
        student_list = StudentManagement()
        student_list.create_list()
        sel_ls = input("Select this newly-created student list now? [y/<any other key>]: ")
        if sel_ls.lower() == 'y':
            selected_student_list = StudentManagement.studls_ls[-1]
            selected_cour_list = CourseMarkManagement.courls_ls[-1]
            print("Student list {} is now selected".format(selected_student_list.__str__()))

    # action 2: insert courses and/or marks for a student list
    elif sel == 2:
        # if there are no courses yet
        if selected_cour_list.cournum == 0:
            selected_cour_list.insert_cour(selected_student_list.studnum)
    
        # if there are courses but no marks yet
        else:
            selected_cour_list.show_all_cour()
            while True:
                sel_cour = int(input("Select a course to enter marks (-1 for all): "))
                if sel_cour > -2 and sel_cour < selected_cour_list.cournum:
                    break
            selected_cour_list.insert_mark(selected_student_list.studnum, sel_cour)

    # action 3: show all students in a list
    elif sel == 3:
        selected_student_list.show_all_stud()

    # action 4: show all student lists
    elif sel == 4:
        StudentManagement.show_all_studls()

    # action 5: show student personal information
    elif sel == 5:
        sel_stud = input("Enter student ID: ")
        idx = selected_student_list.find_stud_idx(sel_stud)
        if idx == -1:
            print("No student matched")
        else:
            selected_student_list.show_a_stud(idx)

    # action 6: show all courses linked to the selected student list
    elif sel == 6:
        selected_cour_list.show_all_cour()

    # action 7: show student marks
    elif sel == 7:
        if selected_cour_list.cournum == 0:
            print("No courses to show marks")
            continue
        sel_stud = input("Enter student ID: ")
        idx = selected_student_list.find_stud_idx(sel_stud)
        if idx == -1:
            print("No student matched")
            continue

        selected_cour_list.show_all_cour()
        while True:
            sel_cour = int(input("Select a course to show mark (-1 for all): "))
            if sel_cour > -2 and sel_cour < selected_cour_list.cournum:
                break
        selected_cour_list.show_stud_mark(sel_cour, idx)
    
    # action 8: show all marks of a course linked to the selected student list
    elif sel == 8:
        if selected_cour_list.cournum == 0:
            print("No courses to show marks")
            continue
        selected_cour_list.show_all_cour()
        while True:
            sel_cour = int(input("Select a course to show marks (-1 for all): "))
            if sel_cour > -2 and sel_cour < selected_cour_list.cournum:
                break
        selected_cour_list.show_cour_mark(sel_cour)

    # action 9: modify student personal information
    elif sel == 9:
        sel_stud = input("Enter student ID: ")
        idx = selected_student_list.find_stud_idx(sel_stud)
        if idx == -1:
            print("No student matched")
            continue
        selected_student_list.mod_info(idx)

    # action 10: modify student marks
    elif sel == 10:
        if selected_cour_list.cournum == 0:
            print("No courses to modify marks")
            continue
        sel_stud = input("Enter student ID: ")
        idx = selected_student_list.find_stud_idx(sel_stud)
        if idx == -1:
            print("No student matched")
            continue
        selected_cour_list.show_all_cour()
        while True:
            sel_cour = int(input("Select a course to modify mark (-1 for all): "))
            if sel_cour > -2 and sel_cour < selected_cour_list.cournum:
                break
        selected_cour_list.mod_mark(sel_cour, idx)

    # action 11: modify course information
    elif sel == 11:
        if selected_cour_list.cournum == 0:
            print("No courses to modify information")
            continue
        selected_cour_list.show_all_cour()
        while True:
            sel_cour = int(input("Select a course to modify the information (-1 for all): "))
            if sel_cour > -2 and sel_cour < selected_cour_list.cournum:
                break
        selected_cour_list.mod_cour(sel_cour)

    # action 12: quit
    elif sel == 12:
        break

    else:
        print("Invalid action")
