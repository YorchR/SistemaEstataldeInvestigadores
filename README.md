# Sistema Estatal de Investigadores

Este repositorio contiene el proyecto del SEI el cual debera ir en el dominio https://secyt.cozcyt.gob.mx/SDHJKssd283764/usuarios/login

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos Windows o Linux 🖥🐧️📋

```
Docker V24.0.6  superior
Docker Compose V2.15.1 o suprior
```

### Instalación 🔧

_Clonar el repositorio en una ruta de facil acceso con el siguiente comando:_

```console
root@pc:~$ git clone https://labsol.cozcyt.gob.mx/gitlab/devops-lab/sistema-estatal-de-investigadores.git
```

_Una vez descargado ingresaremos a la carpeta del proyecto con:_

```console
root@pc:~$ cd sistema-estatal-de-investigadores
```

_Dentro de la carpeta del proyecto haremos un:_

```console
root@pc:~$ docker compose up -d
```

_Este comando realizara la instalación de todas las dependencias necesarias para el fincionamiento del proyecto._

_Una vez terminado este proceso podremos ver los nuevos contenedores con el comando:_
```console
root@pc:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED       STATUS         PORTS                            NAMES
95389a82be47   sei-app   "fish"                   8 weeks ago   Up 6 seconds   80/tcp, 0.0.0.0:8000->8000/tcp   curso
b0de61d29f76   mariadb   "docker-entrypoint.s…"   8 weeks ago   Up 6 seconds   0.0.0.0:3310->3306/tcp           db-vinculacion
```


## Despliegue 📦

_Para hacer deploy a nuestro proyecto debemos entrar al contenedor de la aplicación y ejecutar los siguientes comandos:_
```console
root@pc:~$ docker exec -it CONTAINER_ID bash
root@CONTAINER_ID:/app# python3 manage.py makemigrations
root@CONTAINER_ID:/app# python3 manage.py migrate
root@CONTAINER_ID:/app# mkdir -p media/ZIPs
root@CONTAINER_ID:/app# mkdir -p media/usuarios/investigadores/Constancias/Word
```

_Ahora debemos entrar al conteneder de nuestra base de datos de la misma manera que entramos al contenedor anterior y realizar las siguientes inserciones en esta:_
```console
root@pc:~$ docker exec -it CONTAINER_ID bash
root@CONTAINER_ID:/app# mariadb -u root -D vinculacion -pvinculacion_root_password

MariaDB [vinculacion]> INSERT INTO vinculacion.investigadores_nivelinvestigador (id,nivel,descripcion)
    VALUES (1,0,'No');
INSERT INTO vinculacion.investigadores_nivelinvestigador (id,nivel,descripcion)
    VALUES (2,1,'Nivel 1');
INSERT INTO vinculacion.investigadores_nivelinvestigador (id,nivel,descripcion)
    VALUES (3,2,'Nivel 2');
INSERT INTO vinculacion.investigadores_nivelinvestigador (id,nivel,descripcion)
    VALUES (4,3,'Nivel 3');
INSERT INTO vinculacion.investigadores_nivelinvestigador (id,nivel,descripcion)
    VALUES (5,4,'Candidato');

MariaDB [vinculacion]> INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (1,'Apozol');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (2,'Apulco');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (3,'Atolinga');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (4,'Benito Juárez');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (5,'Calera');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (6,'Cañitas de Felipe Pescador');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (7,'Concepción del Oro');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (8,'Cuauhtémoc');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (9,'Chalchihuites');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (10,'Fresnillo');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (11,'Trinidad García de la Cadena');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (12,'Genaro Codina');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (13,'General Enrique Estrada');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (14,'General Francisco R. Murguía');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (15,'El Plateado de Joaquín Amaro');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (16,'General Pánfilo Natera');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (17,'Guadalupe');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (18,'Huanusco');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (19,'Jalpa');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (20,'Jerez');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (21,'Jiménez del Teul');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (22,'Juan Aldama');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (23,'Juchipila');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (24,'Loreto');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (25,'Luis Moya');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (26,'Mazapil');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (27,'Melchor Ocampo');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (28,'Mezquital del Oro');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (29,'Miguel Auza');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (30,'Momax');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (31,'Monte Escobedo');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (32,'Morelos');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (33,'Moyahua de Estrada');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (34,'Nochistlán de Mejía');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (35,'Noria de Ángeles');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (36,'Ojocaliente');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (37,'Pánuco');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (38,'Pinos');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (39,'Río Grande');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (40,'Sain Alto');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (41,'El Salvador');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (42,'Sombrerete');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (43,'Susticacán');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (44,'Tabasco');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (45,'Tepechitlán');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (46,'Tepetongo');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (47,'Teúl de González Ortega');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (48,'Tlaltenango de Sánchez Román');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (49,'Valparaíso');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (50,'Vetagrande');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (51,'Villa de Cos');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (52,'Villa García');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (53,'Villa González Ortega');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (54,'Villa Hidalgo');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (55,'Villanueva');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (56,'Zacatecas');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (57,'Trancoso');
INSERT INTO vinculacion.usuarios_municipio (id,nombre)
	VALUES (58,'Santa María de la Paz');

MariaDB [vinculacion]> INSERT INTO vinculacion.vinculacion_areaconocimiento (nombre,descripcion) VALUES
	 ('Físico-Matemáticas y Ciencias de la Tierra','Propuestas formuladas en aspectos básicos de astronomía, física, matemáticas, óptica
y disciplinas afines; aspectos básicos de geología, geofísica, geoquímica, geografía
física, oceanografía, limnología, hidrología, ciencias de la atmósfera y contaminación
de agua, aire y suelos y disciplinas afines.'),
	 ('Biología y Química','Propuestas formuladas en aspectos básicos de bioquímica, biofísica, biología,
fisiología, biología celular y molecular, neurociencias, genética, ecología, evolución y
sistemática de organismos terrestres y acuáticos (marinos y de aguas
epicontinentales) tanto vegetales como animales, hongos y microorganismos, así
como en disciplinas afines; aspectos básicos de química inorgánica, orgánica o
analítica, aislamiento, identificación y síntesis de productos naturales, química
farmacológica y disciplinas afines.'),
	 ('Medicina y Ciencias de la Salud','Propuestas formuladas en aspectos básicos de las ciencias biomédicas, salud pública,
epidemiología y disciplinas afines.'),
	 ('Ciencias de la Conducta y la Educación','Propuestas formuladas en aspectos básicos de educación, antropología física,
arqueología, estética, etnohistoria, filología, filosofía, historia, arquitectura y urbanismo,
psicología, literatura, lingüística y disciplinas afines.'),
	 ('Humanidades','Propuestas formuladas en aspectos básicos de cultura, museología, artes, diseño,
historia del arte, estudios de género, ética, y disciplinas afines.'),
	 ('Ciencias Sociales','Propuestas formuladas en aspectos básicos de sociología, antropología social,
demografía, comunicación, derecho, etnología, economía, administración y políticas
públicas y administración privada, ciencias políticas, relaciones internacionales y
disciplinas afines.'),
	 ('Ciencias de la Agricultura, Agropecuarias, Forestales y de Ecosistemas','Propuestas formuladas en aspectos básicos de biotecnología, acuacultura y
pesquerías; ciencias agronómicas y forestales; medicina veterinaria y zootecnia;
alimentos; microbiología, biorremediación ambiental, sanidad y fisiología animal y
vegetal, y disciplinas afines.'),
	 ('Ingenierias y Desarrollo Tecnológico','Propuestas formuladas en aspectos básicos de las ciencias de la ingeniería industrial,
química, electrónica, eléctrica, instrumentación, informática de sistemas, cómputo, en
telecomunicaciones, aeronáutica, de control, robótica, mecatrónica, nuclear, civil,
ambiental, mecánica, hidráulica, metalúrgica, cerámica, de materiales, de polímeros,
corrosión y disciplinas afines.'),
	 ('Investigación Multidisciplinaria','Propuestas formuladas en aspectos básicos de más de una disciplina en donde se
note claramente la participación y división de las diferentes áreas o disciplinas del
conocimiento en la solución de un proyecto de investigación que, por su complejidad,
no pueda resolverlo una disciplina individualmente. Utilizar una herramienta o técnica
de otra área del conocimiento diferente a la de la propuesta, no implica que ésta sea
considerada multidisciplinaria.');

```
_Con esto tendremos nuestra base de datos con los elementos necesarios para funcionar, volvemos al contenedor anterior finalmente ejecutamos los siguientes comandos:_
```console
root@pc:~$ docker exec -it CONTAINER_ID bash
root@CONTAINER_ID:/app# python3 manage.py runserver 0:8000

```

_Y tendremos nuestra aplicación funcionando a la perfeccion:_

## Construido con 🛠

* [Docker](https://www.docker.com/) - Programa para desarrollo y despliegue.
* [Django](https://www.djangoproject.com/) - Framework de desarrollo.
* [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Usado para los estilos de las vistas.

## Autores ✒️

* **Juventino Aguilar Correo.** - *Trabajo Inicial*
* **Elías Emiliano Beltrán González** - *Trabajo Inicial*
* **Román Guzmán Valles** - *Trabajo Inicial*

* **Jorge Luis Díaz Serna** - *Mantenimiento y Correción de Errores*
* **Omar Alejandro De la Cruz Razo** - *Mantenimiento y Correción de Errores*

## Licencia 📄

Este proyecto está bajo la Licencia (GPL3.0) - mira el archivo [LICENSE.md](https://labsol.cozcyt.gob.mx/gitlab/devops-lab/sistema-estatal-de-investigadores/-/blob/main/LICENSE) para más detalles.

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.
