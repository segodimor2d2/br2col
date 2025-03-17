# BR2COL GODIMARKET

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
- `sold_num = (número de vendidos)`
- `seller = (nombre del vendedor)` 

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
---

## NEW VERSIÓN

- el programa busca en la pag1, los links de las pags que la búsqueda generó
- el programa colecta los datos de los productos de la pag1
- si existe la pag10 existe, el programa abre la pag10 donde ML va general el link y el numero de la última pag disponible
- asi captura conseguí capturar el numero máximo de paginas que ML tiene disponible
- `aún no estoy capturando los links de las pags que hacen falta, AQUI HAY UN BUG pq si quermos buscar en otras paginas ej. pag11-pag20`
- la funcionalidad esta creada para capturar el numero total de pags como un indicador de volumen de productos publicados en ML
- el programa colecta los datos de los productos de la pag10
- el programa va a pasar por las pags hasta el paramento topage y si topage es mayor a la lista de links, va a colectar los datos hasta el numero máximo

---

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

# ESTRATEGIA

- pedir para la IA que genere una lista de productos de acuerdo con la secuencia de preguntas

- crear un programa para automatizar una lista de searchs para buscar con 02mlanalitics.py (`si es necesario`)

- programa para analizar el csv definiendo los productos mas vendidos 
    - analizar precios mas caros de producto y marca
    - analizar los mas vendidos / pedidos
    - analizar mas vendidos con menor precio
    - analizar mas publicados, analizar si son los mismos vendedores
    - analizar analizar quienes son los  vendedores e ver si ellos usan un punto de distribución
    - analizar qué productos en Brasil `MUY USADOS NO ESTÁN` siendo vendidos en Col con la posibilidad a abrir un mercado en Col

- en qué momento es útil entrar dentro del link del producto para ver cuantos vendidos y cual es el vendedor?

- Qué quiero saber encontrando los productos de Br que son mas vendidos en Col?
    - Saber si puedo competir por precio
    - Saber si es un indicador para encontrar los CDs en Col
    - Saber si es un indicador para entender la logística de enviar para Col
    - Saber que productos de Br pueden competir contra los productos en Col

- *DESCUBRIR QUÉ PRODUCTOS PUEDEN SER COMPETITIVOS EN COL, QUE SON VENDIDOS EN BR PERO NO EN COL*
    - Validar los productos mas vendidos en Col
    - Validar los productos similares pero mas usando en Br
    - Validar precios
    - podemos encontrar un producto para competir que sea un buen negocio vender

- saber marca mas usadas br/col
- productos mas vendidos br/col
- marcas mas vendidas en br/col
- marcas de Br mas vendidas e usadas en Col 
- Encontrar el nicho de los productos en Col
 
---

# Secuencia de preguntas deepseek
- ¿cuáles son las marcas para cabello más usadas en los salones de belleza en Colombia?
- ¿cuáles son las marcas para cabello más usadas en los salones de belleza en Brasil?
- ¿cuáles son los productos más vendidos en los salones de belleza en Colombia?
- ¿cuáles son los productos más vendidos en los salones de belleza en Brasil?
- Qué marcas brasileras han sido vendidas en los salones de belleza en Colombia?
- ¿cuáles son las marcas más usadas en los salones de belleza en Colombia que son importados de Brasil?
- ¿cuáles son los productos más usados en los salones de belleza en Colombia que son importados de Brasil?

---
## COLOMBIA
### marcas más usadas
- L'Oréal Professionnel: Cuidado y coloración profesional.
- Wella Professionals: Coloración y styling.
- Schwarzkopf Professional: Alta calidad para salones.
- Matrix: Accesible y popular.
- Revlon Professional: Cuidado y coloración.
- Kérastase: Lujo y tratamientos.
- Redken: Innovación en cuidado.
- Joico: Reparación intensiva.
- Nioxin: Tratamientos para caída.
- TIGI: Styling profesional.
- Nativa Spa: Ingredientes naturales.
- Creaciones Gloria: Cuidado capilar y belleza.

GPT
- Henkel: Líder en ventas.  
- Recamier: Tinturas reconocidas.  
- L'Oréal Professionnel: Alta calidad en cuidado y coloración.  
- Schwarzkopf Professional: Innovación en tintes y cuidado.  
- Wella Professionals: Amplia gama de tintes y cuidado capilar.  
- Univital: Ingredientes naturales.  
- María Salomé: Cuidado natural sin químicos.  

### productos más vendidos

- L'Oréal Professionnel, Tratamientos de keratina, clima tropical de Colombia.  
- Cadiveu, Tratamientos de keratina, tecnología avanzada y calidad premium.  
- Schwarzkopf Professional, Tratamientos de keratina, control de frizz y alisado duradero.  
- Niasi, Alisado progresivo, fórmulas innovadoras y efectivas.  
- Embelleze, Alisado progresivo, resultados duraderos y cabello manejable.  
- Wella Professionals, Tintes profesionales, colores vibrantes y técnicas modernas.  
- Matrix, Tintes y decolorantes, variedad de tonos y calidad profesional.  
- Revlon Professional, Productos para mechas, reflejos y técnicas como balayage.  
- Kérastase, Mascarillas capilares, reparación y nutrición profunda.  
- Joico, Mascarillas y tratamientos, recuperación de cabello dañado.  
- Redken, Aceites nutritivos, brillo y suavidad duraderos.  
- Moroccanoil, Aceites nutritivos, hidratación intensa y aroma premium.  
- L'Oréal Professionnel, Aceites nutritivos, protección y reparación capilar.  
- Dercos (L'Oréal), Shampoos anticaspa, tratamiento efectivo para problemas comunes.  
- Nioxin, Productos para fortalecimiento capilar, crecimiento y reducción de caída.  
- TIGI, Spray termoprotector, protección contra herramientas de calor.  
- Redken, Cremas para definición de rizos, estilo y cuidado simultáneo.  
- L'Oréal Professionnel, Geles y ceras, fijación y estilo duradero.  
- Boticário Professional, Productos para styling, versatilidad y acabados profesionales.  
- Niasi, Shampoos y cremas para rizos, definición y hidratación.  
- Lola Cosmetics, Productos para rizos, ingredientes naturales y veganos.  
- Beauty Hair, Cremas para rizos, brillo y control de frizz.  
- Extensiones de pestañas, Kits profesionales, look impactante y duradero.  
- Tinturas para cejas y pestañas, Coloración intensa y natural.  
- Colorama, Esmaltes semipermanentes, durabilidad y variedad de colores.  
- Risqué, Esmaltes y tratamientos, tendencias y acabados creativos.  
- Cadiveu, Tratamientos de keratina premium, resultados visibles y duraderos.  
- Kérastase, Aceites y serums, nutrición y brillo intenso.  
- Moroccanoil, Aceites y serums, hidratación profunda y aroma exclusivo.  
- Hombre, Pomadas y ceras, estilo y fijación para hombres.  
- Boticário Professional, Shampoos y acondicionadores, cuidado específico masculino.  
- Niasi, Cuidado natural y vegano, ingredientes libres de crueldad animal.  
- Lola Cosmetics, Productos personalizados, adaptados a cada tipo de cabello.  




---
## BRASIL
### marcas más usadas br
#### Marcas Internacionales:
- L'Oréal Professionnel: Coloración y cuidado profesional.
- Wella Professionals: Coloración y styling.
- Schwarzkopf Professional: Coloración y cuidado.
- Matrix: Coloración accesible.
- Kérastase: Tratamientos de lujo.
- Redken: Innovación en cuidado.
- Joico: Reparación intensiva.
- TIGI: Styling creativo.

#### Marcas Locales y Regionales:
- Niasi: Cuidado completo.
- Embelleze: Alisado y coloración.
- Cadiveu: Tratamientos de keratina.
- Boticário Professional: Cuidado y styling.
- Lola Cosmetics: Innovación y calidad.
- Soukai: Alisado y tratamientos.
- Hombre: Cuidado masculino.

#### Marcas de Tratamientos Específicos:
- Kérastase: Cuidado intensivo.
- Moroccanoil: Hidratación con aceite de argán.

GPT
- L'Oréal: Líder em salões de beleza.  
- Wella Professionals: Tradicional em cuidados e coloração.  
- Inoar: Produtos orgânicos e veganos.  
- Cadiveu: Alta qualidade e tecnologia avançada.  
- Ybera Paris: Excelência em cuidados capilares.  
- Alfaparf: Reconhecido por produtos profissionais.  
- Agilise Cosméticos: Queratina vegetal e brilho natural.

### productos más vendidos br

- Cadiveu, Tratamientos de keratina, control de frizz y cabello liso en clima tropical.  
- Embelleze, Tratamientos de keratina líquida, resultados duraderos y manejabilidad.  
- Soukai, Alisados progresivos, fórmulas innovadoras y cuidado del cabello.  
- Lola Cosmetics, Productos para alisado progresivo, adaptados a diferentes tipos de cabello.  
- Niasi, Alisados progresivos, ingredientes naturales y efectividad comprobada.  
- L'Oréal Professionnel, Tintes profesionales, colores vibrantes y duraderos.  
- Wella Professionals, Tintes y decolorantes, técnicas modernas como balayage.  
- Schwarzkopf Professional, Productos para mechas y reflejos, resultados profesionales.  
- Kérastase, Mascarillas capilares, reparación profunda y nutrición intensa.  
- Joico, Mascarillas y tratamientos, recuperación de cabello dañado.  
- Niasi, Aceites nutritivos, hidratación y brillo natural.  
- Moroccanoil, Aceites nutritivos, hidratación intensa y aroma premium.  
- Cadiveu, Aceites y serums, reparación y protección capilar.  
- Dercos (L'Oréal), Shampoos anticaspa, tratamiento efectivo para problemas comunes.  
- Nioxin, Productos para fortalecimiento capilar, crecimiento y reducción de caída.  
- TIGI, Spray termoprotector, protección contra herramientas de calor.  
- Redken, Cremas para definición de rizos, estilo y cuidado simultáneo.  
- L'Oréal Professionnel, Geles y ceras, fijación y estilo duradero.  
- Boticário Professional, Productos para styling, versatilidad y acabados profesionales.  
- Lola Cosmetics, Shampoos y cremas para rizos, definición y control de frizz.  
- Niasi, Productos para rizos, ingredientes naturales y veganos.  
- Beauty Hair, Cremas para rizos, brillo y hidratación intensa.  
- Colorama, Esmaltes semipermanentes, durabilidad y variedad de colores.  
- Risqué, Esmaltes y tratamientos, tendencias y acabados creativos.  
- Cadiveu, Tratamientos de keratina premium, resultados visibles y duraderos.  
- Kérastase, Aceites y serums, nutrición y brillo intenso.  
- Moroccanoil, Aceites y serums, hidratación profunda y aroma exclusivo.  
- Hombre, Pomadas y ceras para styling, estilo y fijación para hombres.  
- Boticário Professional, Shampoos y acondicionadores, cuidado específico masculino.  
- Niasi, Cuidado natural y vegano, ingredientes libres de crueldad animal.  
- Lola Cosmetics, Tratamientos personalizados, adaptados a cada tipo de cabello.  


### productos más usados br

- Embelleze, Tratamientos de keratina líquida, capacidad para controlar el frizz y dejar el cabello liso y manejable.  
- Cadiveu, Tratamientos de keratina, tecnología avanzada y calidad premium.  
- Soukai, Alisados progresivos y selladores de cutícula, resultados duraderos y cabello saludable.  
- Niasi, Mascarillas capilares intensivas, hidratación profunda y reparación para cabello dañado.  
- Lola Cosmetics, Aceites nutritivos (argán o coco), nutrición y brillo intenso.  
- Beauty Hair, Ampollas de reparación, recuperación rápida del cabello maltratado.  
- Lola Cosmetics, Tintes profesionales, colores vibrantes y duraderos.  
- Mahogany, Decolorantes y polvos voluminizadores, resultados profesionales y modernos.  
- Niasi, Cremas para definición de rizos, control de frizz y rizos definidos.  
- Beauty Hair, Shampoos y acondicionadores sin sulfatos, cuidado suave y efectivo.  
- Lola Cosmetics, Aceites y serums para brillo, hidratación y brillo natural.  
- Boticário Professional, Sprays termoprotectores, protección contra herramientas de calor.  
- Salon Line, Cremas para peinado, estilo duradero y acabados profesionales.  
- Niasi, Ampollas para crecimiento capilar, fortalecimiento y reducción de caída.  
- Cadiveu, Shampoos y acondicionadores fortalecedores, cabello resistente y saludable.  
- Hombre, Pomadas y ceras para styling, estilo y fijación para hombres.  
- Boticário Professional, Shampoos y acondicionadores específicos, cuidado personalizado masculino.  
- Niasi, Shampoos y acondicionadores orgánicos, ingredientes naturales y libres de crueldad animal.  
- Lola Cosmetics, Mascarillas con ingredientes naturales, hidratación y cuidado sostenible.  
- Boticário Professional, Kits para laminado de cejas, cejas definidas y naturales.  
- Lola Cosmetics, Tinturas para pestañas y cejas, coloración intensa y duradera.  
- Boticário Professional, Esmaltes semipermanentes, durabilidad y variedad de colores.  
- Salon Line, Cremas hidratantes para manos y pies, hidratación profunda y suavidad.  
- Cadiveu, Tratamientos de alta gama, resultados profesionales y duraderos.  
- Lola Cosmetics, Enfoque en cabello rizado y crespo, productos específicos y efectivos.  
- Niasi, Cuidado natural y vegano, ingredientes saludables y sostenibles.  

---


# Qué marcas brasileras han sido vendidas en los salones de belleza en Colombia?

- Niasi
- Embelleze
- Cadiveu
- Lola Cosmetics
- Boticário Professional
- Hombre
- Soukai
- Beauty Hair
- Salon Line
- Mahogany


## marcas más usadas co importadas de br
- Niasi, Shampoos  
- Niasi, Acondicionadores  
- Niasi, Mascarillas  
- Niasi, Tratamientos para hidratación  
- Niasi, Reparación capilar  
- Embelleze, Tratamientos de alisado  
- Embelleze, Keratina  
- Embelleze, Productos para cuidado capilar  
- Cadiveu, Tratamientos de keratina  
- Cadiveu, Aceites capilares  
- Cadiveu, Productos para hidratación profunda  
- Lola Cosmetics, Productos para coloración  
- Lola Cosmetics, Hidratación  
- Lola Cosmetics, Cuidado del cabello rizado  
- Boticário Professional, Cuidado capilar  
- Boticário Professional, Styling  
- Boticário Professional, Tratamientos específicos  
- Hombre, Pomadas  
- Hombre, Ceras  
- Hombre, Shampoos para cabello masculino  
- Soukai, Tratamientos de alisado  
- Soukai, Productos para cuidado capilar  
- Beauty Hair, Productos para cabello rizado  
- Beauty Hair, Hidratación  
- Beauty Hair, Reparación  
- Salon Line, Productos para styling  
- Salon Line, Hidratación  
- Salon Line, Cuidado diario del cabello  
- Mahogany, Tintes  
- Mahogany, Decolorantes  
- Mahogany, Productos para coloración profesional  


## productos más usadas co importadas de br

- Embelleze, Tratamientos de keratina líquida.  
- Embelleze, Alisados progresivos.  
- Embelleze, Selladores de cutícula.  
- Cadiveu, Tratamientos de keratina líquida.  
- Cadiveu, Alisados progresivos.  
- Cadiveu, Selladores de cutícula.  
- Soukai, Tratamientos de keratina líquida.  
- Soukai, Alisados progresivos.  
- Soukai, Selladores de cutícula.  
- Niasi, Mascarillas capilares intensivas.  
- Niasi, Aceites nutritivos (argán o coco).  
- Niasi, Ampollas de reparación.  
- Lola Cosmetics, Mascarillas capilares intensivas.  
- Lola Cosmetics, Aceites nutritivos (argán o coco).  
- Lola Cosmetics, Ampollas de reparación.  
- Beauty Hair, Mascarillas capilares intensivas.  
- Beauty Hair, Aceites nutritivos (argán o coco).  
- Beauty Hair, Ampollas de reparación.  
- Lola Cosmetics, Tintes profesionales.  
- Lola Cosmetics, Decolorantes y polvos voluminizadores.  
- Lola Cosmetics, Productos para reflejos y balayage.  
- Mahogany, Tintes profesionales.  
- Mahogany, Decolorantes y polvos voluminizadores.  
- Mahogany, Productos para reflejos y balayage.  
- Niasi, Cremas para definición de rizos.  
- Niasi, Shampoos y acondicionadores sin sulfatos.  
- Niasi, Aceites y serums para brillo.  
- Beauty Hair, Cremas para definición de rizos.  
- Beauty Hair, Shampoos y acondicionadores sin sulfatos.  
- Beauty Hair, Aceites y serums para brillo.  
- Lola Cosmetics, Cremas para definición de rizos.  
- Lola Cosmetics, Shampoos y acondicionadores sin sulfatos.  
- Boticário Professional, Sprays termoprotectores.  
- Boticário Professional, Cremas para peinado.  
- Boticário Professional, Geles y ceras moldeadoras.  
- Salon Line, Sprays termoprotectores.  
- Salon Line, Cremas para peinado.  
- Salon Line, Geles y ceras moldeadoras.  
- Niasi, Ampollas para crecimiento capilar.  
- Niasi, Shampoos y acondicionadores fortalecedores.  
- Niasi, Sueros para cuero cabelludo.  
- Cadiveu, Ampollas para crecimiento capilar.  
- Cadiveu, Shampoos y acondicionadores fortalecedores.  
- Cadiveu, Sueros para cuero cabelludo.  
- Hombre, Pomadas y ceras para styling.  
- Hombre, Shampoos y acondicionadores específicos para hombres.  
- Hombre, Tratamientos para barba y bigote.  
- Boticário Professional, Pomadas y ceras para styling.  
- Boticário Professional, Shampoos y acondicionadores específicos para hombres.  
- Boticário Professional, Tratamientos para barba y bigote.  
- Niasi, Shampoos y acondicionadores orgánicos.  
- Niasi, Mascarillas con ingredientes naturales.  
- Niasi, Aceites esenciales.  
- Lola Cosmetics, Shampoos y acondicionadores orgánicos.  
- Lola Cosmetics, Mascarillas con ingredientes naturales.  
- Lola Cosmetics, Aceites esenciales.  
- Boticário Professional, Kits para laminado de cejas.  
- Boticário Professional, Tinturas para pestañas y cejas.  
- Boticário Professional, Extensiones de pestañas.  
- Lola Cosmetics, Kits para laminado de cejas.  
- Lola Cosmetics, Tinturas para pestañas y cejas.  
- Lola Cosmetics, Extensiones de pestañas.  
- Boticário Professional, Esmaltes semipermanentes.  
- Boticário Professional, Cremas hidratantes para manos y pies.  
- Boticário Professional, Tratamientos para cutículas.  
- Salon Line, Esmaltes semipermanentes.  
- Salon Line, Cremas hidratantes para manos y pies.  
- Salon Line, Tratamientos para cutículas.  



## ¿CUÁLES SON LOS PRODUCTOS QUE NORMALMENTE SON MÁS CAROS?  


1. Mascarillas de Tratamiento Profundo:  
   - Mascarillas Reconstrucción: Contienen ingredientes como queratina, proteínas y aminoácidos que ayudan a reparar la fibra capilar.  
   - Mascarillas con Ingredientes Naturales u Orgánicos: Usan ingredientes de alta calidad, como aceites vegetales puros, extractos botánicos y mantecas naturales.  

2. Aceites Capilares Premium:  
   - Aceites con Ingredientes Exóticos: Como aceite de argán, marula, macadamia y jojoba, conocidos por sus propiedades nutritivas y regenerativas.  

3. Sérum Capilar de Lujo:  
   - Sérum con Protección Térmica y Brillo Intenso: Productos que combinan protección térmica, brillo y tratamiento en una sola fórmula, con ingredientes como siliconas orgánicas y vitaminas.  

4. Productos para Alisado y Relajación:  
   - Cremas Alisadoras de Alta Calidad: Garantizan alisado duradero sin dañar el cabello, con fórmulas que incluyen queratina y otros agentes reparadores.  
   - Kits de Alisado Japonés o Brasileño: Tratamientos profesionales de alisado permanente realizados en salones de belleza.  

5. Tintes y Decolorantes Profesionales:  
   - Tintes Permanentes de Marcas Reconocidas: Ofrecen amplia gama de colores, cobertura de canas y durabilidad.  
   - Decolorantes de Alta Calidad: Minimiza los daños al cabello durante el proceso de aclarado.  

6. Productos para Protección Térmica:  
   - Sprays y Cremas Termoprotectores de Lujo: Brindan protección avanzada contra el calor, además de hidratación y brillo.  

7. Líneas de Tratamiento Completo:  
   - Kits de Tratamiento Capilar: Incluyen shampoo, acondicionador, mascarilla y sérum de una misma línea, diseñados para problemas específicos como daño, resequedad o caída del cabello.  

8. Productos para Cuidados Específicos:  
   - Tratamientos Anticaída: Contienen ingredientes como minoxidil, vitaminas y minerales para estimular el crecimiento capilar y reducir la caída.  
   - Tratamientos para Cuero Cabelludo Sensible: Ayudan a calmar y equilibrar el cuero cabelludo con ingredientes como aloe vera, manzanilla y aceites esenciales.  

9. Productos para Rizos de Lujo:  
   - Activadores de Rizos y Cremas Definidoras: Brindan definición, hidratación y control del frizz, con fórmulas ricas en mantecas y aceites naturales.  

10. Productos de Marcas de Lujo:  
   - Marcas Reconocidas: Como Kérastase, Oribe, Moroccanoil, Aveda y Shu Uemura, que ofrecen productos de alto rendimiento con empaques sofisticados e ingredientes premium.  

---

Esta organización sigue el formato que solicitaste, destacando la marca y el tipo de producto.

---

## Brainstorm

- revisar filtro en la url mejores vendedores (en la url de ML la requisición puede contener un filtro tipo #D[A:rating_average])
    - Ex. https://listado.mercadolibre.com.co/esp32#D[A:rating_average]

- encontrar productos agotados en ML 
- hacer una encuesta sobre productos de brasil en las peluquerías para saber la vos de cliente

---

## OLD VERSIÓN (referencia)

- Después de analizar la búsqueda, va a generar una lista ordenada por el número de opiniones/comentarios en pandas.
- A continuación, si el número de total_reviews > 10 va a pedir hasta qué línea se quieren obtener los datos de vendidos e imprime uno a uno los productos consultados
- el programa va a generar un archivo CSV en la carpeta outcsv con los datos colectados ej. 20250226110058_co.csv
- e adiciona en el archivo info.md la consulta e el nombre de archivo así: 20250226110058_co, res: 61: search: esp32s3



