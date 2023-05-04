# PostgreSQL

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


## Lesson 3. SQL Query Language. DDL, DML commands

- SQL - Structure query language


- DBMS - DataBase Management System

### SQL Commands
-  SQL
    - DDL - Create, Alter, Drop, Truncate, Rename
    - DML - Select, Insert, Update, Delete
    - DCL - Grant, Revoke
    - TCL - Save Point, Roll Back, Commit
   
### DDL (Data Definition Language)
- Ma'limotlarni ta'rif tili
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
- Ma'lumotlarni manipulatsiya tili
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
 - DELETE operatori jadvaldagi mavjud ma'lumotlarni o'chirish uchun ishlatiladi
    ```
   DELETE FROM table_name WHERE condition;
   
   DELETE FROM TeacherInfo WHERE TeacherName='John';
   ```
   
#### SELECT
 - SELECT iborasi m'lumotlar bazasidan ma'lumotlarni tanlash uchun ishlatiladi
    ```
   1 - usul.
        SELECT column1, column2, column3, .... FROM table_name;
   
   2 - usul.
        SELECT * FROM table_name;
   ```

## Lesson 4. DCL, TCL, Build structure

### DCL - DATA CONTROL LANGUAGE
 - DATA CONTROL LANGUAGE - Ma'lumotlarni boshqarish tili


 - Ushbu bo'lim ma'lumotlar bazasidagi imtiyozlarni boshqarish uchun ishlatiladigan buyruqlardan iborat. Buyruqlar quyidagilar 
   - #### GRANT 
   - #### REVOKE


#### GRANT
 - GRANT buyrug'i foydalanuvchiga kirish huquqini yoki sxema uchun boshqa imtiyozlarni berish uchun ishlatiladi.
    ```
   GRANT privileges ON object TO user;

   GRANT INSERT ON TeachersInfo TO PUBLIC;
   ```

#### REVOKE
 - REVOKE buyrug'i GRANT buyrug'i yordamida foydalanuvchining kirish huuqlarini bekor qilish uchun ishlatiladi
    ```
   REVOKE privileges ON object FROM user;
   
   
   REVOKE INSERT ON TeacherInfo FROM PUBLIC;
   ```
 
### TCL - TRANSACTIONAL CONTROL LANGUAGE
 - PostgreSQL da TCL tranzaksiyalarni bosharish tilini anglatadi
 - Ma'lumotlar bazasidagi yagona ish birligi buyruqlar ketma-ket bajarilgandan so'ng tranzaksiya shakllanadi.
 - PostgreSQL da TCL buyruqlari deb nomlanivchu ma'lum buyruqlar mavjud bo'lib, ular foydalanuvchiga ma'lumotlar bazasida amalga oshiriladigan tranzaktsiyalarni boshqarishga yordam beradi.
 - Ular quyidagilar:
    - #### BEGIN
    - #### COMMIT
    - #### ROLLBACK
    - #### SAVEPOINT
    - #### RELEASE SAVEPOINT
    - #### SET TRANSACTION

#### BEGIN
 - Tranzaksiyani boshlash uchun BEGIN TRANSACTION buyrug'i ishlatiladi.
    ```
   BEGIN;
   BEGIN TRANSACTIOn;
   ```
   
#### COMMIT 
 - COMMIT buyrug'i oxirgi COMMIT yoki ROLLBACK buyrug'idan keyin ma'lumotlar bazasiga barcha operatsiyalarni saqlaydi.
    ```
   DELETE * FROM TeacherInfo WHERE Salary = 65000;
   COMMIT;
   ```

#### ROLLBACK 
 - ROLLBACK buyrug'i so'nggi COMMIT yoki ROLLBACK buyrug'i chaqirilgandan keyin tranzaktsiyalarni bekor qilish uchun ishlatiladi.
    ```
   DELETE * FROM TeacherInfo WHERE Salary = 65000;
   ROLLBACK;
   ```

#### SAVEPOINT 
 - SAVEPOINT joriy tranzaktsiya doirasida yangi saqlash nuqtasini belgilaydi.
    ```
   Syntax:
        SAVEPOINT savepoint_name; 
        ROLLBACK TO savepoint_name
        ROLLBACK;
   
   
   Example:
        SAVEPOINT SP1; 
        DELETE FROM TeacherInfo WHERE Fees = 65000;
        SAVEPOINT SP2;
   ```

#### RELEASE SAVEPOINT
 - RELEASE SAVEPOINT buyrug'i siz yaratgan SAVE POINTni olib tashlash uchun ishlatiladi.

    ```
   Syntax:
        RELEASE SAVEPOINT savepoint_name;
   
   
   Example:
        RELEASE SAVEPOINT SP2;
   ```

#### SET TRANSACTION
 - SET TRANSACTION buyrug'i joriy tranzaksiya xarakteristikalarini o'rnatadi
    ```
   Syntax:
        SET TRANSACTION transaction_mode;
   ```
   
## Lesson 5. Operators, PostgreSQL fundamentals

- #### OPERATOR - bu taqqoslash va arifmetik amallar kabi amallarni bajarish uchun asosan PostgreSQL bayonotining WHERE bandida ishlatiladigan zahiradagi so'z yoki belgi.
- Operatorlar PostgreSQL bayonotida shartlarni belgilash va bayonotda bir nechta shartlar uchun brikma sifatida xizmat qilish uchun ishlatiladi.
- Quyida operatorlar turlari:
    - #### Arifmetik Operatorlar
    - #### Taqqoslash Operatorlar
    - #### Mantiqiy Operatorlar
    - #### Baytli Operatorlar
    - V.h ...

<h4 align="center"> Arifmetik Operatorlari  </h4>
<p align="center"> 
    <img width="800" src="http://telegra.ph//file/3a4523b1202cb34badb88.jpg" alt="">
</p>

!['Arifmetik amallar'](http://telegra.ph//file/3a4523b1202cb34badb88.jpg)

center Solishtirish Operatorlari

![](http://telegra.ph//file/6f89720cc8cdba63064e9.jpg)

<p style="text-align: center">  </p>








