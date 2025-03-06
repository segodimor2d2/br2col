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

- organizar las info de google drive en github

- crear un nombre para el proyecto (no es nombre de la empresa)
    - el nombre de la empresa es la ultima cosa que se hace ya que vamos a tener la visión de todo el panorama
        - br2col
        - godimarcket

- mlanalitics features backlog
    - organizar el código
    - tener una noción de los mas vendidos con: analizar total_reviews de varias paginas sin entrar en el producto
    - observa si hay productos con alta rotación o que estén agotados frecuentemente
    - corregir error cuando la búsqueda no tiene resultados
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
- Refinar las preguntas y datos retornados por DeepSeek y ChatGPT

## Sebastián
- secuencia de preguntas deepseek
- mlanalitics

---

# done

## Maria Fernanda
- mlanalitics
    - logística discovery

## Santiago

## Sebastián
- mlanalitics
    - va imprimiendo el numero da la linea procesada
    - organizar el df por mas vendidos después de capturar los vendidos y el seller
    - imprime cuantos productos son diferentes de 0 calificados total_reviews
    - el numero de lineas de entrada puede ser automático
        - se es < 10 va automatico
    - info.md logs ex: 20250303192220_co, numprod = 49, pags = 3, coment = 8, search = esp32s3

---

# Programa para buscar productos en ML y generar un archivo CSV

Creé un programa que captura los datos mediante scraping de los resultados de cada producto con los siguientes atributos:

- 'title'
- 'price'
- 'permalink' (url)
- 'rating_average' (nota general)
- 'total_reviews' (número de evaluaciones)
- 'sold_num' (número de vendidos)
- 'seller' (nombre del vendedor)

Para mejorar la ejecución del programa la llamada del programa contiene los siguientes parámetros:
- country: país (br/co)
- search_query: cadena de búsqueda, en vez de espacio se usaría coma (,)

Ejemplo:
```bash
python 00mlanalitics.py country pags search_query
python 00mlanalitics.py co 10 esp32,cam
```
- Después de analizar la búsqueda, va a generar una lista ordenada por el número de opiniones/comentarios en pandas.
- A continuación, si el número de total_reviews > 10 va a pedir hasta qué línea se quieren obtener los datos de vendidos e imprime uno a uno los productos consultados
- el programa va a generar un archivo CSV en la carpeta outcsv con los datos colectados ej. 20250226110058_co.csv
- e adiciona en el archivo info.md la consulta e el nombre de archivo así: 20250226110058_co, res: 61: search: esp32s3


