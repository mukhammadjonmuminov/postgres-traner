# Postgresql

- Lesson 1 - PostgreSQL DBMS.
- Lesson 2 - Data types and Constraint.
- Lesson 3 - SQL Query Language. DDL, DML commands.
- Lesson 4 - DCL, TCL, Build structure.
- Lesson 5 - Operators, PostgreSQL fundamentals.
- Lesson 6 - Joining Multible Tables
- Lesson 7 - Extra fundamentals for table
- Lesson 8 - Views
- Lesson 9 - Function
- Lesson 10 - Triggers, Lock and Privileges
- Lesson 11 - Postgresql advanced Feature



## Lesson 1. PostgreSQL DBMS

- Keng ma'noda ***Ma'lumotlar ombori (MO)*** deganda real dunyoning aniq bir ob'yeklar haqidagi ma'lumotlar to'plamini tushunish mumkun.
- ***Ob'ekt*** - bu mavjud va farqlanishi mumkin bo'lgan narsadir. Ob'ektlarga tegishli bir qator ma'lumotlar borki, ularning to'plami MO bo'la oladi.


## Lesson 2. Data types and Constraint

- SQL - Structure query language


- DBMS - DataBase Management System

### SQL Commands
-  SQL
    - DDL - Create, Alter, Drop, Truncate, Rename
    - DML - Select, Insert, Update, Delete
    - DCL - Grant, Revoke
    - TCL - Save Point, Roll Back, Commit
   
### DDL (Data Definition Language)
#### CREATE 
   - Ushbu buyruq sxema, jadval yoki indeks yaratish uchun ishlatiladi.
      ```
     CREATE SCHEMA schema_name;
      ```
     
#### ALTER
  - Ushbu buyruq cheklovlarni yoki ustunlarni qo'shish, o'zgartirish yoki o'chirish uchun ishlatiladi 
    ```
    ALTER TABLE table_name ADD column_name datatype;
    ```
    
#### DROP
  - Ushbu buyruq ma'lumotlar bazasini, jadvallarni yoki ustunlarni o'chirish uchun ishlatiladi 
    ```
    DROP TABLE table_name;
    ```

#### TRUNCATE
  - Ushbu buyruq jadval ichidagi mavjud bo'lgan ma'lumotlarni o'chirish uchun ishlatiladi. Lekin jadval o'chirilmaydi.
    ```
    TRUNCATE TABLE table_name;
    ```

#### RENAME
  - Ushbu buyruq bir yoki bir nechta jadval yoki ustunlar nomini o'zgartirish uchun ishlatiladi. Lekin jadval o'chirilmaydi.
    ```
    ALTER TABLE table_name RENAME TO new_table_name;
    
    ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name
    ```
    
### DML (Data Manipulation Language)
#### INSERT
 - INSERT operatori jadvalga yangi ma'lumotlarni kiritish uchun ishlatiladi.
   ```
   INSERT INTO table_name (column1, column2, column3, ....) VALUES (value1, value2, value3, ....);
   
   INSERT INTO table_name VALUES (alue1, value2, value3, ...)
   ``` 
 
#### UPDATE
 - UPDATE operatori jadvaldagi mavjud ma'lumotlarni o'zgartirish uchun ishlatiladi.
    ```
   UPDATE table_name SET column1 = value1, column2 = value2, ...
    WHERE condition;
   
   Exaple:
        UPDATE TeacherInfo SET TeacherName = 'John', City = 'Tashkent'
        WHERE TeacherID = '01';
   ```
#### DELETE 
 - DELETE 
















