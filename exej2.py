# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:20:43 2020

@author: Desktop
"""


import pyodbc 

direccion_servidor = 'DESKTOP-U6KU352'
nombre_bd = 'materiascursadas'
nombre_usuario = 'Royer23'
password = '2323'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("\n"*2)
    print("conexión exitosa")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
cursor= conexion.cursor()
print("se mostrara la tabla de estudiantes")
sql="select * from materiacursada"
cursor.execute(sql)
registros=cursor.fetchall()
print(registros)
print("sigla \t\t ci \t nota  ")
for registro in registros:
    print(registro[0],"\t",registro[1],"\t",registro[2])
cursor.close()
conexion.close()

'''
SCRPIT BD



CREATE TABLE estudiante
(
    ci integer NOT NULL,
    nombre varchar(30),
    paterno varchar(30),
    materno varchar(30),
   PRIMARY KEY (ci)
);
CREATE TABLE materia
(
    nombremat varchar(50),
    sigla varchar(10),
    PRIMARY KEY (sigla)
);
CREATE TABLE materiacursada
(
    sigla varchar(10)  NOT NULL,
    ci integer NOT NULL,
    nota integer,
   PRIMARY KEY (ci, sigla),
   FOREIGN KEY (ci) REFERENCES estudiante (ci),
  FOREIGN KEY (sigla) REFERENCES materia (sigla)
);
insert into estudiante values(111,'aaa','aaa','aaa');
insert into estudiante values(222,'bbb','bbb','bbb');
insert into estudiante values(333,'ccc','ccc','ccc');
insert into estudiante values(444,'ddd','ddd','ddd');

insert into materia values('introduccion a la programacion','inf-111');
insert into materia values('laboratorio de inf-111','lab-111');
insert into materia values('organizacion de las computadoras','inf-112');
insert into materia values('laboratorio de computacion','inf-113');

insert into materiacursada values('inf-111',111,20);
insert into materiacursada values('lab-111',111,80);
insert into materiacursada values('inf-112',111,75);
insert into materiacursada values('inf-113',111,65);
insert into materiacursada values('inf-111',222,70);
insert into materiacursada values('lab-111',222,90);
insert into materiacursada values('inf-112',222,100);
insert into materiacursada values('inf-113',333,70);
insert into materiacursada values('inf-111',333,90);
insert into materiacursada values('lab-111',444,80);
insert into materiacursada values('inf-112',444,60);
insert into materiacursada values('inf-113',444,55);



'''