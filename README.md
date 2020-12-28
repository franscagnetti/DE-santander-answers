# Data Engineer Programming Test

### Python 
(Para hacerlo interesante, usar Python 2.7)

Se deberá escribir un script que transforme el archivo datos_data_engineer.tsv en un archivo CSV que pueda ser insertado en una base de datos, y/o interpretado por cualquier parser estándar de archivos delimitados, de la manera más sencilla posible.

El archivo resultante debe tener las siguientes características:
* Cada row contiene la misma cantidad de campos
* Los campos se separan con un pipe |
* Se deben poder leer correctamente los caracteres especiales que estén presentes en los campos actuales del archivo. 
* El encoding del archivo final debe ser UTF-8 (datos_de_santander.tsv es un archivo UTF-16LE)

Preguntas y respuestas
* En qué requerimiento implementarías una cola de mensajes en una solución orientada a datos?  Que lenguaje utilizarías y porque?

Implementaria una cola de mensajes en el caso que me pidan interaccion entre distintos microservicios, y que a su vez, necesiten trabajar de manera asincrona. 
Esto a su vez permite mejorar la escalabilidad en el caso de agregar mas microservicios.
Tambien en el caso que me pidan redundancia, ya que se puede dejar el mensaje hasta "confirmar"  que se recibio.


* Que experiencia posees sobre py spark o spark scala? Contar breves experiencias, en caso de contar experiencia con otro framework de procesamiento distribuido, dar detalles también.
No poseo experiencia ni con pyspark ni con spark scala. No tengo tampoco experiencia laboral con frameworks de procesamiento distribuido. 

* Qué funcionalidad podrías expandir desde el area de ingeniería de datos con una API y arquitectónicamente como lo modelarías?

Algunas de las funcionalidades que podría expandir desde el area de ingenieria serian:
	- Brindar servicios de procesamiento al resto de las areas de la empresa. Un ejemplo seria brindar un servicio de geolocalizacion dada una direccion, 
		o un servicio de categorizacion de clientes.
	- Otorgarles datos a algun cliente interno/externo de los ya procesados, permitiendoles un acceso rapido y eficiente como intermediario entre 
		la base de datos y el cliente final.

Para modelar la API, primero buscaria los actores que van a interactuar con la misma, y que necesidad poseen con la API.
A partir de alli se podria ver si, de ser necesario, se necesitan balanceadores de carga, que este hosteado en cloud o no, y en caso que si en 
que lugar geograficamente es conveniente, que manera de escalar es la mas conveniente (vertical u horizontalmente), de donde debera consumir/producir, 
que debera realizar, de que manera, las politicas de seguridad y autenticacion, el resultado de la operacion (si devuelve por ejemplo un JSON o un XML), 