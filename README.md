# Tópicos de Telematica (HPC)
By: 	
* Mariana Narvaez Berrio - mnarvae3@eafit.edu.co 
* Mateo Murillo Penagos - mmurill5@eafit.edu.co

UltimaHora
==================

Esta es la entrega final de la tercera practica de Tópicos de Telematica (**HPC**); este proyecto tiene como finalidad solucionar 2 problemas.

- **Problema 1:** Es necesario comparar 2 documentos entre si y sacar un valor para saber que tan similares son estos documentos.
- **Problema 2:** Es necesario agrupar los documentos leídos en grupos según el tema que se trate en cada documento (Agrupar los documentos que probablemente hablen del mimo tema)

Este desarrollo esta adaptado para trabajar con muchos procesadores al mismo tiempo (Adaptado para clusters) lo cual mejora la eficiencia al leer una gran cantidad de documentos.
También se presenta una solución serial al mismo problema, el cual realiza el mismo algoritmo corriendo en un único núcleo.

----------


## Información

El código se divide en 3 secciones, la lectura y organización de los documentos, la ejecución del algoritmo de Jaccard para evaluar la similitud entre los documentos y la ejecución del algoritmo de kMeans para agrupar estos documentos según lo parecido que sean 

### Lectura de Documentos
La lectura de los documentos es un algoritmo el cual crea iterativamente un diccionario clave valor para cada palabra única encontrada en los documentos para luego indicar numericamente las palabras que existen en cada documento.

```
Documento A: La política de estos días se centra en los esclavos, pero en estos días de tragedia es primordial que la política deje de centrarse en los esclavos y se centre en el comercio y los cultivos. 
```

Documento A (Palabras únicas): 

Palabras Únicas	|	Palabras Únicas 
------------| ---------------
política 	|	primordial 
días		|	centrarse 
centra	 	|	centre		
esclavos 	|	comercio 
tragedia 	|	cultivos     

**Diccionario**

Clave		|		Valor
------------| -------------
política 	|	0
días		|	1
centra	 	|	2
esclavos 	|	3
tragedia 	|	4
primordial  |	5
centrarse 	|	6
centre		|	7
comercio 	|	8
cultivos  	|	9


Documento A (): 

Diccionario	|	Numerico 
------------| ----------
0	|	5 
1	|	6 
2 	|	7		
3 	|	8 
4 	|	9 

### Jaccard
Una vez terminado el proceso de lectura y con toda la información de palabras únicas en un arreglo numérico, se procede a comparar cada documento con todos los demás en el arreglo.
El algoritmo de Jaccard compara los conjuntos de datos para saber que tan parecidos son, primero realizando una intersección y dividiéndolo por la union de los conjuntos, de la siguiente manera: 

- Doc A: 32; 25; 120; 27; 602; 11; 201; 15; 89; 125; 563; 632; 245
- Doc B: 9; 23; 245; 256; 222; 123; 89; 25; 120

> **Jaccard**
> 
> Intersección: 245, 89, 25, 120 = 4 elementos
> 
> Unión: 22 elementos
>
>Porcentaje de similitud: 4/22 = 18%

Como resultado de este proceso queda una matriz de similitud entre documentos, la cual indica que tan parecidos son todos los documentos comparados con los demás.

Docs	| 	A	|	B	|	C	|	D
----|-------|-------|-------|------- 
A	|	1 	|  0.15	|  0.95	| 0.35	
B	| 0.15	|   1	|  0.41	| 0.06
C	| 0.95	|  0.41	|   1	| 0.75
D	| 0.35	|  0.06	|  0.75	|  1

  

### kMeans
Por ultimo, al terminar de comparar todos los documentos, se envía la matriz de similitud al algoritmo de kMeans, junto al numero de clusters esperados (Temas o categorías en los que entraran los documentos)

Separación de clusters en kMeans:
![alt text](https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/19344/versions/1/screenshot.jpg)

Al finalizar la ejecución de kMeans, este, retorna una matriz con las las proximidades por documento, y un arreglo en el que indica a que cluster pertenece que documento.

### Salida del programa 

Al finalizar la ejecución del algoritmo de kMeans, se separan en arreglos los documentos categorizados en cada cluster, y por ultimo se imprime una matriz con los nombres de los documentos, en la cual cada fila de la matriz representa un cluster.

Al presentarse una gran cantidad de documentos, esta salida, empezara a ser muy complicada para su lectura, por lo que se recomienda parsear esta salida para poder separar fácilmente los documentos por cluster.

--------------

# Ejecución

#### Serial
Para la ejecución del algoritmo serial se necesita cumplir con lo siguiente:

- Clonar el repositorio
- Tener Python 2.7 instalado

Una vez cumplidos los requisitos unicamente se debe ejecutar el siguiente comando:

```
$ sudo python ControllerSerial.py path clusters

path = Ubicación donde se encuentran los documentos a leer
clusters = Numero de clusters o conjuntos de documentos esperados
```


#### Paralelo
Para la ejecución del algoritmo paralelo se necesita cumplir con lo siguiente:

- Clonar el repositorio
- Tener Python 2.7 instalado
- Tener openmpi instalado
- Tener mpi4py instalado 
- Tener el comando mpiexec en correcto funcionamiento
- Tener como mínimo 2 cores para correr el programa
- Tener disponible al menos 20% del tamaño de todos los documentos a leer en memoria

Una vez cumplidos los requisitos unicamente se debe ejecutar el siguiente comando:
```
$ sudo mpiexec  -np cores python ./Controller.py path clusters

cores = Numero de núcleos que se asignaran para correr el programa.
path = Ubicación donde se encuentran los documentos a leer
clusters = Numero de clusters o conjuntos de documentos esperados
```

---------------

> **Notas:**

> - El archivo Controller.py no puede ser ejecutado normalmente con python ni únicamente con un núcleo, porque este puede entrar en un ciclo infinito.
> El directorio dado para leer los archivos únicamente debe contener archivos txt, de lo contrario, la salida del programa se vera comprometida y no retornara exitosamente los clusters
> - Para ejecutar Controller.py es necesario tener instalado mpi4py y ejecutarlo únicamente con el comando mpiexec.
> - En la ejecución de Controller.py cada núcleo puede llegar a necesitar máximo, 5mb de memoria, y el núcleo principal puede llegar a necesitar hasta el 20% del tamaño de los documentos a ser leídos en memoria.
