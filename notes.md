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
la carpeta \_\_pycache\_\_, esta carpeta contiene el Byte Code de los 
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
- *paquetes\_proyecto/
	Paquete que nos permite unir y usar modulos
	- \_\_init\_\_.py
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

my\_list: List[int] = [0, 0, 0]
my\_tuple: Tuple[int, float, str] = (16, 1.76, "Martín")
my\_dict: Dict[str, str] = {"key": "value"}

Estos tipos de datos no son obligatorios, solo son recomendaciones, 
si hacemos o llegamos a tener un error con el tipo de la variable, aun asi 
hayamos definido su tipo correctamente con :. Python no nos 
va a dar o soltar error. Para hacer que esto ocurra debemos 
instalar el modulo de mypy con pip

Lo usaremos con su binario en la terminal, el cual nos va a pedir el archivo a verificar y alguna que otra flag para su uso.

mypy archivo.py

Una flag importante es:
	--check\_untyped\_defs

Que va a verificar que cada function si se le pase y devuelva el tipo de valor correcto.

## Scopes en Python

El scope es el alcance que una variable puede llegar a tener dentro de nuestro programa, siendo el alcance, que esta se 
pueda usar y utilizar. Algunas veces se puede cambiar dentro de un nivel y cambiar, o no, su valor en otro nivel.
Los Scopes generalmente van a estar dentro de las funciones.

Generalmente:
	Las Variables solo estaran disponibles dentro de la región que fue creada

Exiten diferentes tipos de scopes en Python:

- Local:
	El scope base de una function
- global:
	El scope en el que esta una function, generalmente la base del programa y del archivo

## Closures

Los closures son una forma de usar nested functions

- Nested Functions:
	Son funciones, que estan dentro de otra function, estas toman o recuerdan una o mas variable de la function en 
	la que estan. Aun así esta se elimine.

Para tener un closure debemos seguir con minimo 3 reglas.
- Debemos usar una nested function
- La nested function debe tener uno o varios valores de la function padre o base
- La nested function debe ser retornada por la function base, para que se pueda usar.

Los clousures son una muy buena alternativa a objetos hechos con clases que son bastante sencillos, 
generalmente solo un metodo y el numero de atributos no importa.

## Decorators

Los Decorators son una forma en la que podemos hacer que nuestro codigo se vea mucho mas bonito al momento 
de hacer un tipo de closure. Este tipo debe agregar una funcionalidad a nuestra funcion, generalmente usada 
para testing de funciones, y alguna que otra cosa rara con string. 

Se usa @, el nombre del decorador y si este necesita parametros, agregarlos con (args). Poniendo todo esto encima de 
la function que vayamos a decorar.

Si nuestra function necesita argumentos por orden o por key word, vamos a tener que usar el operador de 
constructor simple y para dicts. * y * *.

## \_\_Iter\_\_ 

\_\_iter\_\_ y \_\_next\_\_ es un method de los objetos iterables, que lo hacen iterable, duh.
Estos metodos tienen un protocolo el cual es:
- Creamos un iterable con iter(), generalmente listas de datos
- vamos a ir a cada elemento usando next()
- hasta que de un error de StopIteration.

Teniendo en cuenta esta estructura podemos crear una clase que tenga los metodos, en los cuales
vamos a tener que seguir tambien unos protocolos.

- \_\_iter\_\_
	va a ser lo que necesita para funcionar el iterador, como los parametros y argumentos de las funciones,
	pero estos ya deben estar definidos, principalmente en el self del mismo objeto. Un \_\_init\_\_ pero del 
	iterador
- \_\_next\_\_
	va a ser la forma en que se va a avanzar hasta cada elemento que necesitemos. DEBE tener un final en 
	el que vamos a hacer un raise de StopIteration para terminar de forma adecuada la iteracion.

Lo bueno de los iteradores es que son bastantes optimizados ahorrando tiempo y memoria, dado a que la forma de 
obtener cada elemento es una funcion o operacion matematica, si no es así o no lo diseñaste así, lo mejor es 
quedarse con el iterador comun de las agrupaciones de datos.

## Generadores

Los generadores son una forma de sintetic sugar para los iteradores, usando solo una funcion, y una variable.
Usando Yield podemos hacer un generador en python, es una palabra reservada con las mismas funciones que 
return, pero que lo especial es que puede devolver un valor, sin parar o terminar la funcion. 
Es decir esta queda en un estado de pausa.

Esto lo podemos aprovechar para usar un loop dentro de la function para hacer un iterador, 
practicamente usando el mismo codigo con el que usariamos un iterador normal, solo que 
ahorrandose la parte de class, \_\_init\_\_, \_\_iter\_\_ y \_\_next\_\_.

Haciendo una prueba, al parecer, no se necesita hacer un raise de StopIteration, solo una forma 
de romper el flujo de datos.

## Sets

Son una estructura de datos en python built-in, que nos permite guardar los datos de una forma desordenada, inmutable, y que no tienen 
valores repetidos, extremadamente importante para datos que se necesitan rápidamente, ya que es extremadamente eficiente.

Para crealo, vamos a tener que usar la clase set() sin datos, o crearlo con datos usando {}, ya que 
si creamos un "set" vacio, python lo entendera como si fuera un diccionario.

Metodos:
- add(valor): agrega un valor y elimina el mismo valor si se encontraba antes en el set
- update(*valores): actualiza agregando datos al set. Puede recibir listas, tuplas, sets y todos los que quieran.

- delete(valor): elimina un valor dentro del set, si no esta, da error
- discard(valor): elimina al valor dentro del set, si no esta, no pasa nada

- pop(): eliminar un valor random
- clear(): elimina todos los valoresa

Operaciones:
Usan operadores especiales para hacer todos los tipos de join
- fulljoin: set\_1 | set\_2: Se unen totalmente
- innerjoin: set\_1 & set\_2: Se unen solo los valores que estan en ambos sets
- outerjoin: set\_1 - set\_2: Se eliminan los valores del set\_1 que esten en el set\_2
- differencejoin: set\_1 ^ set\_2: Se unen solo los valores que no tienen corelacion entre los sets

## Modulo DateTime

Es un modulo que nos permite usar fechas y horas en python. 

Tiene 3 principales modulos, 
- date
- time
- datetime

Podemos acceder a los valores del tiempo que hayamos requerido usando el metodo now(), aunque 
esto va a dar el tiempo del computador o el local, mas no el tiempo verdadero o horario, 
para esto vamos a tener que usar el metodo utcnow()

Podemos hacer diferentes formatos de fechas usando el meotodo strftime, en el que usaremos la tabla 
de valores de cada dato de la fecha:
- %d: dia
- %m: mes
- %Y: año
- %H: hora
- %M: minuto
- %S: segundo

## TimeZones

Podemos complementar DateTime con el modulo TimeZones, que debemos intalar. 
Que nos permitira usar Zonas Horarias

Simplemente vamos a tener que usar el metodo timezone con un código de la ciudad o 
zona horaria que necesitemos, esto lo debemos buscar nosotros mismos. 

Vamos a usar el return del timezone como argumento para usar now o utcnow de 
datetime.

## Hemos terminado el curso

Tenemos un desafío el cual podemos hacer cualquier cosa de lo que queramos haciendo lo que 
aprendimos.

Podemos tomar una ruta de algoritmos, datascience o web backend con python partiendo desde 
este punto.


