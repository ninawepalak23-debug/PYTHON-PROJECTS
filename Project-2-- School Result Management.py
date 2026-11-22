subjects = ["English", "Physics", "Chemistry", "Maths", "Computer Science"]
theory_max = [80, 70, 70, 80, 70]
practical_max = [20, 30, 30, 20, 30]
theory_min = [27, 24, 24, 27, 24]
practical_min = [7, 10, 10, 7, 10]
sub_codes=['301','042','043', '041', '083']
total_max = 100
students=[]
print("=========================================")
print("             SCHOOL RESULT MANAGEMENT SYSTEM")
print("=========================================")
print("                         ACADEMIC SESSION 2026-27")
print("=========================================")
print()
print("             SUBJECT-WISE EXAMINATION STRUCTURE")
print()
print("-------------------------------------------------------------------------")
#Subject Wise exam structure
for i in range(len(subjects)):
    print("\nSubject Code :", sub_codes[i])
    print("Subject:", (subjects[i]).upper())
    print("Theory Marks :", theory_max[i])
    print("Practical:", practical_max[i])
    print("Total Marks:", total_max)
    print("Passing Marks:", theory_min[i], "Theory /",practical_min[i], "Practical")
    print("---------------------------------------------")
print("\n     OVERALL EXAMINATION SUMMARY")
print("\nTotal Subjects :", len(subjects))
print("Total Theory Marks :", sum(theory_max))
print("Total Practical/Internal Marks :", sum(practical_max))
print("Overall Maximum Marks: ", total_max*(len(subjects)))
print("=========================================")

print("=========================================")
print("                                STUDENT REGISTRATION")
print("=========================================")
#Student registration
while True:
      student={}
      theory_marks=[]
      practical_marks =[]
      adm_no = int(input("Enter Admission Number of student: "))
      s_name=input("Enter Student Name: ").strip().title()
      roll_no=int(input("Enter Roll No. : "))
      s_class=int(input("Enter Student Class(in digits only): "))
      s_section=input("Enter Student Section: ").strip().upper()
      duplicate = False
      for i in range(len(students)):
            if students[i]["Admission Number"] == adm_no:
                  duplicate = True
      if s_class>12 or s_class<1:
            print("Invalid class")
      elif s_name=='':
            print("Student Name cannot be empty")
      elif duplicate==True:
            print("Admission number already exists")
      else:
            student["Admission Number"]=adm_no
            student["Student Name"]=s_name
            student["Roll No. "]=roll_no
            student["Class"]=s_class
            student["Section"]=s_section
            student["Theory Marks"]=theory_marks
            student["Practical Marks"]=practical_marks
            students.append(student)
            print("Student Registered Successfully")
            print("---------------------------------------------")
      ch_1=input("Add another student(Y/N): ").strip().upper()
      if ch_1=='Y':
            continue
      else:
          break

print("=========================================")
print("                                STUDENT RECORDS")
print("=========================================")
#Display Student Records
if len(students)>0:
      for i in range(len(students)):
            print("\nAdmission Number: ",students[i]["Admission Number"])
            print("Student Name: ",students[i]["Student Name"])
            print("Roll No. : ",students[i]["Roll No. "])
            print("Class: ",students[i]["Class"])
            print("Section: ",students[i]["Section"])
            print("Theory Marks: ",students[i]["Theory Marks"])
            print("Practical Marks: ",students[i]["Practical Marks"])
            print("---------------------------------------------")
      print("Total Students Registered: ", len(students))
else:
      print("No student is registered")

print("=========================================")
print("                  SEARCH STUDENT RECORDS")
print("=========================================")
x=int(input("Enter Admission Number: "))
found=False
for i in range(len(students)):
      if students[i]["Admission Number"] == x:
            found=True
            print("\nStudent Record Found!")
            print("---------------------------------------------")
            print("Admission Number:", students[i]["Admission Number"])
            print("Student Name:", students[i]["Student Name"])
            print("Roll No.:", students[i]["Roll No."])
            print("Class:", students[i]["Class"])
            print("Section:", students[i]["Section"])
            print("Theory Marks:", students[i]["Theory Marks"])
            print("Practical Marks:", students[i]["Practical Marks"])
            print("---------------------------------------------")
if found==False:
      print("Student not found!")

