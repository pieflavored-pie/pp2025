# initialisation
marks = []

studnum = int(input("Input number of students: "))
studls = []
for i in range(0, studnum):
    studid = input("Input student ID: ")
    studname = input("Input student name: ")
    studdob = input("Input date of birth: ")
    studls.append({"id": studid, "name": studname, "dob": studdob})

cournum = int(input("Input number of courses: "))
courls = []
for i in range(0, cournum):
    courid = input("Input course ID: ")
    courname = input("Input course name: ")
    courls.append({"id": courid, "name": courname})

# helper funcs
def display_students():
    for i in range(0, len(studls)):
        print("{}. {} - {}".format(i, studls[i]["id"], studls[i]["name"]))
    print()

def display_courses():
    for i in range(0, len(courls)):
        print("{}. {} - {}".format(i, courls[i]["id"], courls[i]["name"]))
    print()

def display_marks(coursel):
    if len(marks) == 0:
        print("No marks to display")
    
    else:
        print(marks[coursel]["mark"])
    print()

def input_score():
    coursel = -1 # focus on this course with this index in courls
    while True:
        coursel = int(input("Select a course: "))
        if coursel >= 0 and coursel < len(courls):
            break

    current_courid = courls[coursel]["id"]
    scores = []
    for i in range(0, len(studls)):
        score = float(input("Input student {} score: ".format(i)))
        scores.append(score)
    scores = tuple(scores)
    
    # perform a linear search to overwrite if exists
    found = False
    for i in range(0, len(marks)):
        if marks[i]["courid"].lower() == current_courid.lower():
            marks[i]["mark"] = scores
            found = True
    # add if course has never had scores added to it
    if len(marks) == 0 or found == False:
        marks.append({"courid": current_courid, "mark": scores})

# main loop
while True:
    display_students()
    display_courses()
    print("Inputting marks will overwrite those previously recorded of that course. Proceed with caution.")
    ans = input("""Options: 
c: continue inputting marks
d: display marks of a course
any other key to exit: """)
    if ans.lower() == 'c':
        input_score()

    elif ans.lower() == 'd':
        display_courses()
        coursel = -1 # focus on this course with this index in courls
        while True:
            coursel = int(input("Select a course: "))
            if coursel >= 0 and coursel < len(courls):
                break
        display_marks(coursel)
    else:
        break
