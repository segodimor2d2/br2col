# BR2COL GODIMARKET


---

# reunión daily

- `[x] Mar 07:30 am col / 09:30 br`
- `[x] Mie 07:30 pm col / 21:30 br`
- `[x] Vie 07:30 am col / 09:30 br`

---

# backlog (lista de tareas por hacer)

- crear un checklist de todos los pasos que se vamos hacer
    - `[x] Definir el producto que vamos a trabajar`
    - `[x] Definir la empresa por la que vamos a mandar el producto`
    - `[x] Poner en el papel los costos de todo`
    - `[x] Ejecutar`
    - <!--`[x] `-->

- mlanalitics features backlog
    - observa si hay productos con alta rotación o que estén agotados frecuentemente
    - tener la opción de todas las paginas
    - tener la opción de imprimir la lista hasta un numero de lineas para poder ver la tabla
    - programa para analizar resultados
    - construir programa que compara precios entre dos listas de productos
    - graficar resultados de python en plotly
    - crear un Docker para instalar fácilmente en otras maquinas

- GitHub para todos, aprender a subir archivos en git y control de versiones

- Documento, planeamiento de, trabajo/forma U

---

# in progress

## Maria Fernanda

## Santiago

## Sebastián
- secuencia de preguntas deepseek
- mlanalitics
    - tener una noción de los mas vendidos con: analizar total_reviews de varias paginas sin entrar en el producto

---

# done



## Maria Fernanda
- mlanalitics
    - logística discovery

## Santiago

## Sebastián
- mlanalitics
    - organizar el código
    - corregir error cuando la búsqueda no tiene resultados
    - va imprimiendo el numero da la linea procesada
    - organizar el df por mas vendidos después de capturar los vendidos y el seller
    - imprime cuantos productos son diferentes de 0 calificados total_reviews
    - el numero de lineas de entrada puede ser automático
        - se es < 10 va automatico
    - info.md logs ex: 20250303192220_co, numprod = 49, pags = 3, coment = 8, search = esp32s3

- organizar las info de google drive en github

- crear un nombre para el proyecto (no es nombre de la empresa)
    - el nombre de la empresa es la ultima cosa que se hace ya que vamos a tener la visión de todo el panorama
        - br2col
        - godimarcket
---

# Programa para buscar productos en ML y generar un archivo CSV

mlanaliser es un programa que genera un csv con la captura los datos mediante scraping
de los resultados de cada producto
con los siguientes atributos:

- title = titulo del producto
- price = precio del producto
- rating_average = calificación general del producto
- total_reviews = numero de evaluaciones
- pagnum = numero de la pagina donde se encuentra el producto
- permalink = link del producto
* sold_num = (número de vendidos)
* seller = (nombre del vendedor) 

Para mejorar la ejecución del programa la llamada del programa contiene los siguientes parámetros:
- country: país (br/co)
- numero de paginas donde va a buscar productos
- search_query: cadena de búsqueda, en vez de espacio se usaría coma (,)

Ejemplo:
```bash
# python 00mlanalitics.py country pags search_query
python 02mlanalitics.py co 5 esp32
python 02mlanalitics.py co 5 crema
python 02mlanalitics.py co 5 shampoo
python 02mlanalitics.py co 5 carro,control,remoto

```
### info.md

- fileName = nombre del archivo
- toPage = hasta cuántos páginas se va a buscar
- maxPages = numero de páginas disponibles
- numProd = productos encontrados hasta la pagina toPage
- nonZeroReviews = productos que tienen total_reviews > 0
- search = busqueda realizada

Log tiene como formato de salida:

filename = 20250316103504_co, topage = 5, maxpages = 9, numProd = 204, nonzeroReviews = 200, search = shampoo

---

## NEW VERSIÓN

- el programa busca en la pag1, los links de las pags que la búsqueda generó
- el programa colecta los datos de los productos de la pag1
- si existe la pag10 existe, el programa abre la pag10 donde ML va general el link y el numero de la última pag disponible
- asi captura conseguí capturar el numero máximo de paginas que ML tiene disponible
- `aún no estoy capturando los links de las pags que hacen falta hay que resolver eso por quermos buscar en dados en el resto de las paginas`
- la funcionalidad esta creada para capturar el numero total de pag como un indicador de que el producto esta publicando en varias páginas 
- el programa colecta los datos de los productos de la pag10
- el programa va a pasar por las pags hasta el paramento topage y si topage es mayor a la lista de links, va a colectar los datos hasta el numero máximo

---

## OLD VERSIÓN

- Después de analizar la búsqueda, va a generar una lista ordenada por el número de opiniones/comentarios en pandas.
- A continuación, si el número de total_reviews > 10 va a pedir hasta qué línea se quieren obtener los datos de vendidos e imprime uno a uno los productos consultados
- el programa va a generar un archivo CSV en la carpeta outcsv con los datos colectados ej. 20250226110058_co.csv
- e adiciona en el archivo info.md la consulta e el nombre de archivo así: 20250226110058_co, res: 61: search: esp32s3

---

- pedir para la IA que genere una lista de productos de acuerdo con la secuencia de preguntas

- revisar la cantidad de paginas que encontró por producto en la primera pagina

- revisar la cantidad de paginas para buscar max_pages = all

- filtrar la búsqueda por total_reviews en mercado libre e parar de buscar si el total_reviews es 0 en una pagina

- revisar filtro en la url mejores vendedores

- saber cuantos total_reviews != 0

- automatizar una lista de searchs para buscar

---


