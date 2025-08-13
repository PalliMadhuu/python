import csv;
print("------------------Welcome to Grade management system------------------")

allStudentsInfo = []


def printStudentInfo(studentInfo):
    try:
        print(f'{studentInfo["studentName"]}     {studentInfo["rollNumber"]}     '
              f'{studentInfo["engMarks"]}     {studentInfo["mathsMarks"]}     {studentInfo["physicsMarks"]}     '
              f'{studentInfo["averageMarks"]}     {studentInfo["studentResult"]}')
    except Exception as e:
        print(f"{e}")


def getStudentInfo():
    try:
        isStudentContinue = True
        while isStudentContinue:
            name = input("Enter your name : ")
            rollNumber = int(input("Enter your Roll Number : "))
            engMarks = int(input("Enter your marks in English : "))
            mathsMarks = int(input("Enter your marks in Mathematics : "))
            physicsMarks = int(input("Enter your marks in Physics : "))

            averageMarks = (engMarks + mathsMarks + physicsMarks) / 3

            currentStudentInfo = {
                "studentName": name,
                "rollNumber": rollNumber,
                "engMarks": engMarks,
                "mathsMarks": mathsMarks,
                "physicsMarks": physicsMarks,
                "averageMarks": averageMarks,
                "studentResult": "Pass" if averageMarks > 50 else "Fail"
            }

            isStudentAlreadyExists = False
            for studentInfo in allStudentsInfo:
                if studentInfo["rollNumber"] == currentStudentInfo["rollNumber"]:
                    isStudentAlreadyExists = True
                    break

            if not isStudentAlreadyExists:
                allStudentsInfo.append(currentStudentInfo)
                userRes = input("Do you want to enter more students info : YES or NO : ")
                if userRes.strip().lower() == 'no':
                    isStudentContinue = False

                    print("\nStudent Name     Roll Number     English Marks     Maths Marks     Physics Marks     Average Marks     Student Results")
                    for studentInfo in allStudentsInfo:
                        printStudentInfo(studentInfo)

                    isUserOkayToContinue = True
                    while isUserOkayToContinue:
                        userRes = input("\nEnter SEARCH to search, UPDATE to update, DELETE to delete: Else No or Something to EXIT: ")

                        if userRes.strip().lower() == 'search':
                            userRollNum = int(input("Please enter the Roll Number you want to search: "))
                            isUserFound = False
                            for studentInfo in allStudentsInfo:
                                if studentInfo["rollNumber"] == userRollNum:
                                    isUserFound = True
                                    printStudentInfo(studentInfo)
                                    break
                            if not isUserFound:
                                print("Student Not Found")

                        elif userRes.strip().lower() == 'update':
                            userRollNum = int(input("Please enter the Roll Number you want to update: "))
                            isUserFound = False
                            for studentInfo in allStudentsInfo:
                                if studentInfo["rollNumber"] == userRollNum:
                                    isUserFound = True
                                    printStudentInfo(studentInfo)

                                    name = input("Enter your Updated name : ")
                                    rollNumber = int(input("Enter your Updated Roll Number : "))

                                    isExistingRollNumber = False
                                    for existingStudentInfo in allStudentsInfo:
                                        if existingStudentInfo["rollNumber"] == rollNumber:
                                            isExistingRollNumber = True
                                            break

                                    if not isExistingRollNumber:
                                        engMarks = int(input("Enter your Updated marks in English : "))
                                        mathsMarks = int(input("Enter your Updated marks in Mathematics : "))
                                        physicsMarks = int(input("Enter your Updated marks in Physics : "))
                                        studentInfo["studentName"] = name
                                        studentInfo["rollNumber"] = rollNumber
                                        studentInfo["engMarks"] = engMarks
                                        studentInfo["mathsMarks"] = mathsMarks
                                        studentInfo["physicsMarks"] = physicsMarks
                                        studentInfo["averageMarks"] = (engMarks + mathsMarks + physicsMarks) / 3
                                        studentInfo["studentResult"] = "Pass" if studentInfo["averageMarks"] > 50 else "Fail"
                                        print("Student Info Updated Successfully")
                                    else:
                                        print("Student Already Exists")

                            if not isUserFound:
                                print("Student Not Found")

                        elif userRes.strip().lower() == 'delete':
                            userRollNum = int(input("Please enter the Roll Number you want to delete: "))
                            isUserFound = False
                            indexToRemove = -1
                            for index, studentInfo in enumerate(allStudentsInfo):
                                if studentInfo["rollNumber"] == userRollNum:
                                    isUserFound = True
                                    indexToRemove = index
                                    printStudentInfo(studentInfo)
                                    break
                            if not isUserFound:
                                print("Student Not Found")
                            else:
                                allStudentsInfo.pop(indexToRemove)
                                print("Student Deleted Successfully")

                        else:
                            print("Please check this path to view the student info")
                            with open("E:\StudentInfo.csv",'w',newline='') as csvfile:
                                fieldNames=["studentName","rollNumber","engMarks","mathsMarks","physicsMarks","averageMarks","studentResult"]
                                writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
                                writer.writeheader()
                                writer.writerows(allStudentsInfo)
                            print("Thanks for visiting")
                            isUserOkayToContinue = False
            else:
                print("A student already exists with that roll number! Please enter valid details.")
                getStudentInfo()
    except Exception as e:
        print(f"{e}")


getStudentInfo()
