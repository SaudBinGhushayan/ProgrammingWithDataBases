import Manager
import mysql.connector
conn = mysql.connector.connect(host="localhost",database='****',user="root",password="****")
cursor = conn.cursor()

"""To read data from the text file and insert it into normal list """
try:
    Manager.read(Manager.StudentsList, "Student.txt")
    Manager.read(Manager.CourseList, "Course.txt")
    Manager.read(Manager.MarksList, "Marks.txt")
except AttributeError:
    print("Invalid Input please try again")
except FileNotFoundError:
    print("No such file or directory")
"""To populate data into object-list (Class objects)"""
try:
    Manager.populateData(Manager.StudentsList, Manager.Student, Manager.StudentsObjList)
    Manager.populateData(Manager.CourseList, Manager.Course, Manager.CourseObjList)
    Manager.populateData(Manager.MarksList, Manager.Marks, Manager.MarksObjList)
except AttributeError:
    print("Invalid Input please try again")
"""To insert the object-list into the database"""
try:
    Manager.insert(Manager.StudentsObjList, "Students")
    Manager.insert(Manager.CourseObjList, "Course")
    Manager.insert(Manager.MarksObjList, "Marks")
except AttributeError:
    print("Invalid Input please try again")
except mysql.connector.IntegrityError:
    print("Duplicate entry")

"""This function writes a query that selects all students marks """
def StudentsMarks():
    cursor.execute("select sid,marks from marks group by sid ,marks")
    result = cursor.fetchall()
    print("----First Query----")
    print("Studnets marks are :")
    for x in result:
        print(x)
"""This function writes a query that selects a specific Student mark """
def StudentMark(StudentId,CourseID):
    cursor.execute(f"select cname,marks from marks as m,course as c where c.cid = m.cid and m.sid = {StudentId} and m.cid = {CourseID}")
    result = cursor.fetchall()
    print("----Second Query----")
    print("The Student with ID number: "+str(StudentId)+" got in "+str(result[0][0])+" "+str(result[0][1])+"%")

"""This function writes a query that selects the average mark of all courses"""
def AllAverageMarks():
    cursor.execute("Select AVG(Marks) AS average from marks ")
    result = cursor.fetchall()
    print("----Thrid Query----")
    print("The mark average of all courses are : ")
    for x in result:
        print(x[0])
"""This function writes a query that selects the average mark for a specific course"""
def CourseAverageMark(courseID):
    cursor.execute(f"select avg(Marks) as average from MARKS where cid = {courseID} ")
    result = cursor.fetchall()
    print("----Fourth Query----")
    print("The Average Mark for the desired CourseID givin is "+str(result[0][0]))

"""This function writes a query that selects students full information  """
def StudentsFullInfo():
    cursor.execute("select * from students")
    result = cursor.fetchall()
    print("----Fifth Query----")
    print("Students Full Information")
    for x in result:
        print(x)

"""This function writes a query that selects Marks full information  """
def MarksFullInfo():
    cursor.execute("select * from Marks")
    result = cursor.fetchall()
    print("----Sixth Query----")
    print("Marks Full Information")
    for x in result:
        print(x)

"""This function writes a query that selects Course full information  """
def CourseFullInfo():
    cursor.execute("select * from students")
    result = cursor.fetchall()
    print("----Seventh Query----")
    print("Course Full Information")
    for x in result:
        print(x)
"""This function writes a query that retrieves the highest mark of all courses"""
def highestMark():
    cursor.execute("select MAX(marks) as max from marks")
    result = cursor.fetchall()
    print("Eighth Query")
    print("Hightest Mark is : "+str(result[0][0]))

"""For testing purposes"""
try:
    StudentsMarks()
    StudentMark(439887766,10)
    AllAverageMarks()
    CourseAverageMark(10)
    StudentsFullInfo()
    MarksFullInfo()
    CourseFullInfo()
    highestMark()
except AttributeError:
    print("Invalid inputs")

"""Closing the connection"""
try:
    conn.close()
    print("Connection closed successfully")
except:
    print("Connection did not close ")




























