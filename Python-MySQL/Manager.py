import mysql.connector
conn = mysql.connector.connect(host="localhost",database='****',user="root",password="****")
cursor = conn.cursor()

"""Class Student and the create Students table statement """
class Student:
    def __init__(self, Sid, Sname, PhoneNumber):
        self.Sid = Sid
        self.Sname = Sname
        self.PhoneNumber = PhoneNumber
StudentsTable = """CREATE TABLE STUDENTS (
   SID  INT(20) NOT NULL,
   SNAME CHAR(20),
   PHONENUMBER INT ,
   PRIMARY KEY (SID))"""
# cursor.execute(StudentsTable)
""""Class Course and the create Course table statement """
class Course:
    def __init__(self, Cid , Cname , Semester):
        self.Cid = Cid
        self.Cname = Cname
        self.Semester = Semester
CourseTable = """CREATE TABLE COURSE (
    CID  INT(20) NOT NULL,
    CNAME CHAR(20),
    SEMESTER INT ,
    PRIMARY KEY (CID))"""
# cursor.execute(CourseTable)
"""Class Student and the create Students table statement"""

class Marks:
    def __init__(self,Sid , Cid , Marks):
        self.Sid = Sid
        self.Cid = Cid
        self.Marks = Marks
MarksTable = """CREATE TABLE MARKS (
    SID  INT(20) NOT NULL,
    CID INT(20)  NOT NULL,
    MARKS INT ,
    FOREIGN KEY (SID) REFERENCES STUDENTS(SID),
    FOREIGN KEY (CID) REFERENCES COURSE(CID))"""
# cursor.execute(MarksTable)

"""Normal lists contains the data in .txt files"""
StudentsList = []
CourseList = []
MarksList = []

"""List of Class objects """
StudentsObjList = []
CourseObjList = []
MarksObjList = []

"""4-a To read the .txt file that you've created"""
def read(list , filename):
    file1 = open(filename).readlines()
    for i in file1:
        list.append(i.split(','))
    print(filename+" Has been read successfully ")

"""4-a To populate data into object-list(Class Objects) you have to pass the following:
list: the list that has been read in the previous function
ClassName: the class name that you're going to populate data into it 
ojList: to return the object list(Class Object) for the desired class
"""
def populateData(list,ClassName,objList):
        x=0
        for i in list:
            objList.append((ClassName(list[x][0],list[x][1],list[x][2])))
            x += 1
        print("Object list of "+str(ClassName)+" has been filled")
        return  objList
"""This function accepts two parameter object list that you've just created using
populateData function and table name that have been created earlier 
 and insert it into the database """
def insert(objList,tableName):
    if tableName == "Students":
        x = 0
        for i in objList:
            sql = "INSERT INTO Students(Sid,Sname,PhoneNumber) VALUES (%s, %s, %s)"
            val = (objList[x].Sid, objList[x].Sname, objList[x].PhoneNumber)
            cursor.execute(sql, val)
            conn.commit()
            x =x+ 1
        print("Values Inserted Successfully to Student Table")

    elif tableName == "Course":
        x = 0
        for i in objList:
            sql = "INSERT INTO Course(Cid,Cname,Semester) VALUES (%s, %s, %s)"
            val = (objList[x].Cid, objList[x].Cname, objList[x].Semester)
            cursor.execute(sql, val)
            conn.commit()
            x =x+ 1
        print("Values Inserted Successfully to Course Table")

    elif tableName == "Marks":
        x = 0
        for i in objList:
            sql = "INSERT INTO Marks(Sid,Cid,Marks) VALUES (%s, %s, %s)"
            val = (objList[x].Sid, objList[x].Cid, objList[x].Marks)
            cursor.execute(sql, val)
            conn.commit()
            x =x+ 1
        print("Values Inserted Successfully to Marks Table")
    else:
        print("Table Not Found")
