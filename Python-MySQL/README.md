## Python-MySQL 
The aim of this project is to manipulate students’ marks for some studded courses between python and mysql
### content : 
1. 3 Classes 
2. 2 Modules 
3. 3 `text files`
#### in this project I did the following : 
1. I manually filled the 3 `.txt` files with data about students and their marks information
2. Imported the necessary libraries in this case we only need libraries for the connection with the MySQL database which is `mysql.connector` 
3. I created 3 classes `Student` , ` course` and `marks`
4. I read the 3 text files using the read function that I wrote and I stored each text file into a list with the name of the text file for example : `Student.txt` was stored in Student list 
5. I populated the data recieved from the text file into a class objects using the function populateData 
6. After that I inserted the class objects of each class into the right table in MySQL using the function Insert
7. After the data was successfully inseted now we can perform queries as we like 
