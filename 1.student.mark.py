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

# helper func
def display_everything():
    for i in range(0, len(studls)):
        print("{}. {} - {}".format(i, studls[i]["id"], studls[i]["name"]))
    print()
    for i in range(0, len(courls)):
        print("{}. {} - {}".format(i, courls[i]["id"], courls[i]["name"]))
    print()
    if len(marks) == 0:
        print("No marks to display")
    else:
        for i in range(0, len(marks)):
            print("{}. {}".format(i, marks[i]["courid"]))
            print(marks[i]["mark"])

def input_score():
    scorels = []
    for i in range(0, len(studls)):
        score = float(input("Input student {} score: ".format(i)))
        scorels.append(score)
    return scorels

# main loop
while True:
    coursel = -1 # focus on this course with this index in courls
    display_everything()
    print("This action will overwrite previous recorded marks of that course. Proceed with caution.")
    ans = input("Enter c to continue inputting marks, any other key to exit: ")
    if ans.lower() != 'c':
        break

    while True:
        coursel = int(input("Select a course by entering its number in the list above: "))
        if coursel >= 0 and coursel < len(courls):
            break

    current_courid = courls[coursel]["id"]
    scores = input_score()
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
    
display_everything()
