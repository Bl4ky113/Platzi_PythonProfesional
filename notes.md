# Curso de Python Profesional

## Que necestamos?
- Saber:
	- Básico de Python
	- Git y GitHub
	- Intermedio de Python
	- OOP

## Como funciona Python

Python es un lenguaje interpretado, el cual va a generar 
un Byte code en el cual estara nuestro programa, para ser 
pasado y ejecutado por nuestro computador a travez de una 
maquina virtual de python. 

Permitiendonos usar Python en cualquier computador, siempre 
que tenga el interprete, o el byte code, y la maquina virtual 
de python.

Algunas veces, generalmente cuando importamos archivos, se creara 
la carpeta __pycache__, esta carpeta contiene el Byte Code de los 
archivos de Python. Permitiendonos ejecutar los archivos de una forma más 
rápida, ya que nos pasamos el paso de interpretar los archivos.

Cuando estamos ejecutando un script de python, algunas veces no volveremos a 
usar alguna que otra variable o datos, esto puede hacer que se tenga mayor 
uso de memoria si no se borran estas variable. Para eso Python tiene un 
Garbage Collector que va eliminando variables inutilizadas en el script de Python, 
ahorrando y despejando memoria.

## Como organizar los programas de python

Para organizar un proyecto de python, deberiamos seguir la siguiente estructura:

/proyecto/
- README.md
- .gitignore
- venv/
- requirements.txt
	Lista de modulos para el venv
- *paquetes_proyecto/
	Paquete que nos permite unir y usar modulos
	- __init__.py
		Modulo de un paquete que nos permite usar los 
		modulos del paquete para una funcionalidad 
		especifica
	- *modulos.py
		Codigo de python que se puede reutilizar, y que 
		vamos a usar en el paquete

## Tipado en Lenguajes de Programación

El tipado se puede dividir en dos categorias, su fuerza y su restricción. Teniendo un 
rango de dos valores cada uno. 

- Restricción:
	- Dinamico:
		Se puede declarar una variable con un tipo de valor, y este tipo de 
		valor puede variar a lo largo del script.
		Si llega a dar error, el error ocurre mientras se corre el programa
	- Estatico:
		Se declara una variable y esta debe siempre tener el mismo tipo de valor
		si se llega a cambiar, da un error.
		Si llega a ocurrir un error, ocurre en el copliado del programa

- Fuerza:
	Esta categoria no esta bien definida y puede variar mucho dependiendo de 
	como se use.
	- Fuerte
		Los tipos de valores son repetados dentro del programa, evitando operaciones con 
		otros tipos de valores. 
		"2" + 2 = Error
	- Debil
		Los tipos de valores no son tan importantes como el dato como tal.
		"2" + 2 = 4
		"2" + 2 = "22"

Python es un lenguaje Dinamico y Fuerte

## Python Tipado Estatico

En python 3.6> se puede usar decoradores de nuestras variables para 
verificar el tipo de cada una. Solo vamos a agregar : y el tipo de 
la variable antes del =

variable: int = 12

Se puede aplicar tambien a estructuras de datos, como las listas.
Pero en Python 3.9< hasta 3.6< debemos importar el modulo de 
typing y los tipos de datos que necesitemos. 

Con estas estructuras, vamos a tener que definir que tipo de dato van 
a contener, dato general en las listas y sets, el tipo de la key y el value en dicts,
y dato general o el tipo de dato de cada valor en una tupla, ya que estos no se pueden modificar

my_list: List[int] = [0, 0, 0]
my_tuple: Tuple[int, float, str] = (16, 1.76, "Martín")
my_dict: Dict[str, str] = {"key": "value"}

Estos tipos de datos no son obligatorios, solo son recomendaciones, 
si hacemos o llegamos a tener un error con el tipo de la variable, aun asi 
hayamos definido su tipo correctamente con :. Python no nos 
va a dar o soltar error. Para hacer que esto ocurra debemos 
instalar el modulo de mypy con pip

Lo usaremos con su binario en la terminal, el cual nos va a pedir el archivo a verificar y alguna que otra flag para su uso.

mypy archivo.py

Una flag importante es:
	--check_untyped_defs

Que va a verificar que cada function si se le pase y devuelva el tipo de valor correcto.
