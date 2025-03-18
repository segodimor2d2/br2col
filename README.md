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

Validar las marcas mas vendidas y ver los productos mas vendidos en col 
    Definir productos en col mas relevantes filtrándolos por calificaciones/nota e precio
    (cuales son los productos mas vendidos según ML?)
Después de definir los productos a estudiar revisar quien es el vendedor
    para intentar saber su logística de tener el producto en col
Revisar los productos mas caros y mas vendidos en col
    Los mas caros significa menor estoque e mayor dinero


- Creaciones Gloria, Cuidado capilar y belleza
- Henkel, Líder en ventas  
- Joico, Reparación intensiva
- Kérastase, Lujo y tratamientos
- L'Oréal Professionnel, Alta calidad en cuidado y coloración  
- L'Oréal Professionnel, Cuidado y coloración profesional
- María Salomé, Cuidado natural sin químicos  
- Matrix, Accesible y popular
- Nativa Spa, Ingredientes naturales
- Nioxin, Tratamientos para caída
- Recamier, Tinturas reconocidas  
- Redken, Innovación en cuidado
- Revlon Professional, Cuidado y coloración
- Schwarzkopf Professional, Alta calidad para salones
- Schwarzkopf Professional, Innovación en tintes y cuidado  
- TIGI, Styling profesional
- Univital, Ingredientes naturales  
- Wella Professionals, Amplia gama de tintes y cuidado capilar  
- Wella Professionals, Coloración y styling

Validar las marcas mas vendidas en br
Definir productos en br mas relevantes filtrándolos por calificaciones/nota e precio (cuales son los productos mas vendidos según ML?)

- Agilise Cosméticos: Queratina vegetal e brilho natural.
- Alfaparf: Reconhecido por produtos profissionais.  
- Boticário Professional: Cuidado y styling.
- Cadiveu: Alta qualidade e tecnologia avançada.  
- Cadiveu: Tratamientos de keratina.
- Embelleze: Alisado y coloración.
- Hombre: Cuidado masculino.
- Inoar: Produtos orgânicos e veganos.  
- Joico: Reparación intensiva.
- Kérastase: Cuidado intensivo.
- Kérastase: Tratamientos de lujo.
- L'Oréal Professionnel: Coloración y cuidado profesional.
- L'Oréal: Líder em salões de beleza.  
- Lola Cosmetics: Innovación y calidad.
- Matrix: Coloración accesible.
- Moroccanoil: Hidratación con aceite de argán.
- Niasi: Cuidado completo.
- Redken: Innovación en cuidado.
- Schwarzkopf Professional: Coloración y cuidado.
- Soukai: Alisado y tratamientos.
- TIGI: Styling creativo.
- Wella Professionals: Coloración y styling.
- Wella Professionals: Tradicional em cuidados e coloração.  
- Ybera Paris: Excelência em cuidados capilares.  

---

- Extraer datos sobre el mercado
    - Buscar en ML
    - Buscar en Google
    - ChatGPT
    - Deepseek
    - `DE DONDE PUEDO SACAR MAS DATOS?`

- pedir para la IA que genere una lista de productos de acuerdo con la secuencia de preguntas
    - saber marca mas usadas br/col
    - productos mas vendidos br/col
    - marcas mas vendidas en br/col
    - marcas de Br mas vendidas e usadas en Col 
    - Encontrar el nicho de los productos en Col

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
- Creaciones Gloria: Cuidado capilar y belleza.
- Joico: Reparación intensiva.
- Kérastase: Lujo y tratamientos.
- L'Oréal Professionnel: Cuidado y coloración profesional.
- Matrix: Accesible y popular.
- Nativa Spa: Ingredientes naturales.
- Nioxin: Tratamientos para caída.
- Redken: Innovación en cuidado.
- Revlon Professional: Cuidado y coloración.
- Schwarzkopf Professional: Alta calidad para salones.
- TIGI: Styling profesional.
- Wella Professionals: Coloración y styling.

#### GPT
- Henkel: Líder en ventas.  
- L'Oréal Professionnel: Alta calidad en cuidado y coloración.  
- María Salomé: Cuidado natural sin químicos.  
- Recamier: Tinturas reconocidas.  
- Schwarzkopf Professional: Innovación en tintes y cuidado.  
- Univital: Ingredientes naturales.  
- Wella Professionals: Amplia gama de tintes y cuidado capilar.  

### productos más vendidos col

- Beauty Hair, Cremas para rizos, brillo y control de frizz.  
- Boticário Professional, Productos para styling, versatilidad y acabados profesionales.  
- Boticário Professional, Shampoos y acondicionadores, cuidado específico masculino.  
- Cadiveu, Tratamientos de keratina premium, resultados visibles y duraderos.  
- Cadiveu, Tratamientos de keratina, tecnología avanzada y calidad premium.  
- Colorama, Esmaltes semipermanentes, durabilidad y variedad de colores.  
- Dercos (L'Oréal), Shampoos anticaspa, tratamiento efectivo para problemas comunes.  
- Embelleze, Alisado progresivo, resultados duraderos y cabello manejable.  
- Extensiones de pestañas, Kits profesionales, look impactante y duradero.  
- Hombre, Pomadas y ceras, estilo y fijación para hombres.  
- Joico, Mascarillas y tratamientos, recuperación de cabello dañado.  
- Kérastase, Aceites y serums, nutrición y brillo intenso.  
- Kérastase, Mascarillas capilares, reparación y nutrición profunda.  
- L'Oréal Professionnel, Aceites nutritivos, protección y reparación capilar.  
- L'Oréal Professionnel, Geles y ceras, fijación y estilo duradero.  
- L'Oréal Professionnel, Tratamientos de keratina, clima tropical de Colombia.  
- Lola Cosmetics, Productos para rizos, ingredientes naturales y veganos.  
- Lola Cosmetics, Productos personalizados, adaptados a cada tipo de cabello.  
- Matrix, Tintes y decolorantes, variedad de tonos y calidad profesional.  
- Moroccanoil, Aceites nutritivos, hidratación intensa y aroma premium.  
- Moroccanoil, Aceites y serums, hidratación profunda y aroma exclusivo.  
- Niasi, Alisado progresivo, fórmulas innovadoras y efectivas.  
- Niasi, Cuidado natural y vegano, ingredientes libres de crueldad animal.  
- Niasi, Shampoos y cremas para rizos, definición y hidratación.  
- Nioxin, Productos para fortalecimiento capilar, crecimiento y reducción de caída.  
- Redken, Aceites nutritivos, brillo y suavidad duraderos.  
- Redken, Cremas para definición de rizos, estilo y cuidado simultáneo.  
- Revlon Professional, Productos para mechas, reflejos y técnicas como balayage.  
- Risqué, Esmaltes y tratamientos, tendencias y acabados creativos.  
- Schwarzkopf Professional, Tratamientos de keratina, control de frizz y alisado duradero.  
- TIGI, Spray termoprotector, protección contra herramientas de calor.  
- Tinturas para cejas y pestañas, Coloración intensa y natural.  
- Wella Professionals, Tintes profesionales, colores vibrantes y técnicas modernas.  




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

##### GPT
- L'Oréal: Líder em salões de beleza.  
- Wella Professionals: Tradicional em cuidados e coloração.  
- Inoar: Produtos orgânicos e veganos.  
- Cadiveu: Alta qualidade e tecnologia avançada.  
- Ybera Paris: Excelência em cuidados capilares.  
- Alfaparf: Reconhecido por produtos profissionais.  
- Agilise Cosméticos: Queratina vegetal e brilho natural.

### productos más vendidos br

- Beauty Hair, Cremas para rizos, brillo y hidratación intensa.  
- Boticário Professional, Productos para styling, versatilidad y acabados profesionales.  
- Boticário Professional, Shampoos y acondicionadores, cuidado específico masculino.  
- Cadiveu, Aceites y serums, reparación y protección capilar.  
- Cadiveu, Tratamientos de keratina premium, resultados visibles y duraderos.  
- Cadiveu, Tratamientos de keratina, control de frizz y cabello liso en clima tropical.  
- Colorama, Esmaltes semipermanentes, durabilidad y variedad de colores.  
- Dercos (L'Oréal), Shampoos anticaspa, tratamiento efectivo para problemas comunes.  
- Embelleze, Tratamientos de keratina líquida, resultados duraderos y manejabilidad.  
- Hombre, Pomadas y ceras para styling, estilo y fijación para hombres.  
- Joico, Mascarillas y tratamientos, recuperación de cabello dañado.  
- Kérastase, Aceites y serums, nutrición y brillo intenso.  
- Kérastase, Mascarillas capilares, reparación profunda y nutrición intensa.  
- L'Oréal Professionnel, Geles y ceras, fijación y estilo duradero.  
- L'Oréal Professionnel, Tintes profesionales, colores vibrantes y duraderos.  
- Lola Cosmetics, Productos para alisado progresivo, adaptados a diferentes tipos de cabello.  
- Lola Cosmetics, Shampoos y cremas para rizos, definición y control de frizz.  
- Lola Cosmetics, Tratamientos personalizados, adaptados a cada tipo de cabello.  
- Moroccanoil, Aceites nutritivos, hidratación intensa y aroma premium.  
- Moroccanoil, Aceites y serums, hidratación profunda y aroma exclusivo.  
- Niasi, Aceites nutritivos, hidratación y brillo natural.  
- Niasi, Alisados progresivos, ingredientes naturales y efectividad comprobada.  
- Niasi, Cuidado natural y vegano, ingredientes libres de crueldad animal.  
- Niasi, Productos para rizos, ingredientes naturales y veganos.  
- Nioxin, Productos para fortalecimiento capilar, crecimiento y reducción de caída.  
- Redken, Cremas para definición de rizos, estilo y cuidado simultáneo.  
- Risqué, Esmaltes y tratamientos, tendencias y acabados creativos.  
- Schwarzkopf Professional, Productos para mechas y reflejos, resultados profesionales.  
- Soukai, Alisados progresivos, fórmulas innovadoras y cuidado del cabello.  
- TIGI, Spray termoprotector, protección contra herramientas de calor.  
- Wella Professionals, Tintes y decolorantes, técnicas modernas como balayage.  

### productos más usados br

- Beauty Hair, Ampollas de reparación, recuperación rápida del cabello maltratado.  
- Beauty Hair, Shampoos y acondicionadores sin sulfatos, cuidado suave y efectivo.  
- Boticário Professional, Esmaltes semipermanentes, durabilidad y variedad de colores.  
- Boticário Professional, Kits para laminado de cejas, cejas definidas y naturales.  
- Boticário Professional, Shampoos y acondicionadores específicos, cuidado personalizado masculino.  
- Boticário Professional, Sprays termoprotectores, protección contra herramientas de calor.  
- Cadiveu, Shampoos y acondicionadores fortalecedores, cabello resistente y saludable.  
- Cadiveu, Tratamientos de alta gama, resultados profesionales y duraderos.  
- Cadiveu, Tratamientos de keratina, tecnología avanzada y calidad premium.  
- Embelleze, Tratamientos de keratina líquida, capacidad para controlar el frizz y dejar el cabello liso y manejable.  
- Hombre, Pomadas y ceras para styling, estilo y fijación para hombres.  
- Lola Cosmetics, Aceites nutritivos (argán o coco), nutrición y brillo intenso.  
- Lola Cosmetics, Aceites y serums para brillo, hidratación y brillo natural.  
- Lola Cosmetics, Enfoque en cabello rizado y crespo, productos específicos y efectivos.  
- Lola Cosmetics, Mascarillas con ingredientes naturales, hidratación y cuidado sostenible.  
- Lola Cosmetics, Tintes profesionales, colores vibrantes y duraderos.  
- Lola Cosmetics, Tinturas para pestañas y cejas, coloración intensa y duradera.  
- Mahogany, Decolorantes y polvos voluminizadores, resultados profesionales y modernos.  
- Niasi, Ampollas para crecimiento capilar, fortalecimiento y reducción de caída.  
- Niasi, Cremas para definición de rizos, control de frizz y rizos definidos.  
- Niasi, Cuidado natural y vegano, ingredientes saludables y sostenibles.  
- Niasi, Mascarillas capilares intensivas, hidratación profunda y reparación para cabello dañado.  
- Niasi, Shampoos y acondicionadores orgánicos, ingredientes naturales y libres de crueldad animal.  
- Salon Line, Cremas hidratantes para manos y pies, hidratación profunda y suavidad.  
- Salon Line, Cremas para peinado, estilo duradero y acabados profesionales.  
- Soukai, Alisados progresivos y selladores de cutícula, resultados duraderos y cabello saludable.  

---


# Qué marcas brasileras han sido vendidas en los salones de belleza en Colombia?

- Beauty Hair
- Boticário Professional
- Cadiveu
- Embelleze
- Hombre
- Lola Cosmetics
- Mahogany
- Niasi
- Salon Line
- Soukai


## marcas más usadas co importadas de br

- Beauty Hair, Hidratación  
- Beauty Hair, Productos para cabello rizado  
- Beauty Hair, Reparación  
- Boticário Professional, Cuidado capilar  
- Boticário Professional, Styling  
- Boticário Professional, Tratamientos específicos  
- Cadiveu, Aceites capilares  
- Cadiveu, Productos para hidratación profunda  
- Cadiveu, Tratamientos de keratina  
- Embelleze, Keratina  
- Embelleze, Productos para cuidado capilar  
- Embelleze, Tratamientos de alisado  
- Hombre, Ceras  
- Hombre, Pomadas  
- Hombre, Shampoos para cabello masculino  
- Lola Cosmetics, Cuidado del cabello rizado  
- Lola Cosmetics, Hidratación  
- Lola Cosmetics, Productos para coloración  
- Mahogany, Decolorantes  
- Mahogany, Productos para coloración profesional  
- Mahogany, Tintes  
- Niasi, Acondicionadores  
- Niasi, Mascarillas  
- Niasi, Reparación capilar  
- Niasi, Shampoos  
- Niasi, Tratamientos para hidratación  
- Salon Line, Cuidado diario del cabello  
- Salon Line, Hidratación  
- Salon Line, Productos para styling  
- Soukai, Productos para cuidado capilar  
- Soukai, Tratamientos de alisado  


## productos más usadas co importadas de br

- Beauty Hair, Aceites nutritivos (argán o coco).  
- Beauty Hair, Aceites y serums para brillo.  
- Beauty Hair, Ampollas de reparación.  
- Beauty Hair, Cremas para definición de rizos.  
- Beauty Hair, Mascarillas capilares intensivas.  
- Beauty Hair, Shampoos y acondicionadores sin sulfatos.  
- Boticário Professional, Cremas hidratantes para manos y pies.  
- Boticário Professional, Cremas para peinado.  
- Boticário Professional, Esmaltes semipermanentes.  
- Boticário Professional, Extensiones de pestañas.  
- Boticário Professional, Geles y ceras moldeadoras.  
- Boticário Professional, Kits para laminado de cejas.  
- Boticário Professional, Pomadas y ceras para styling.  
- Boticário Professional, Shampoos y acondicionadores específicos para hombres.  
- Boticário Professional, Sprays termoprotectores.  
- Boticário Professional, Tinturas para pestañas y cejas.  
- Boticário Professional, Tratamientos para barba y bigote.  
- Boticário Professional, Tratamientos para cutículas.  
- Cadiveu, Alisados progresivos.  
- Cadiveu, Ampollas para crecimiento capilar.  
- Cadiveu, Selladores de cutícula.  
- Cadiveu, Shampoos y acondicionadores fortalecedores.  
- Cadiveu, Sueros para cuero cabelludo.  
- Cadiveu, Tratamientos de keratina líquida.  
- Embelleze, Alisados progresivos.  
- Embelleze, Selladores de cutícula.  
- Embelleze, Tratamientos de keratina líquida.  
- Hombre, Pomadas y ceras para styling.  
- Hombre, Shampoos y acondicionadores específicos para hombres.  
- Hombre, Tratamientos para barba y bigote.  
- Lola Cosmetics, Aceites esenciales.  
- Lola Cosmetics, Aceites nutritivos (argán o coco).  
- Lola Cosmetics, Ampollas de reparación.  
- Lola Cosmetics, Cremas para definición de rizos.  
- Lola Cosmetics, Decolorantes y polvos voluminizadores.  
- Lola Cosmetics, Extensiones de pestañas.  
- Lola Cosmetics, Kits para laminado de cejas.  
- Lola Cosmetics, Mascarillas capilares intensivas.  
- Lola Cosmetics, Mascarillas con ingredientes naturales.  
- Lola Cosmetics, Productos para reflejos y balayage.  
- Lola Cosmetics, Shampoos y acondicionadores orgánicos.  
- Lola Cosmetics, Shampoos y acondicionadores sin sulfatos.  
- Lola Cosmetics, Tintes profesionales.  
- Lola Cosmetics, Tinturas para pestañas y cejas.  
- Mahogany, Decolorantes y polvos voluminizadores.  
- Mahogany, Productos para reflejos y balayage.  
- Mahogany, Tintes profesionales.  
- Niasi, Aceites esenciales.  
- Niasi, Aceites nutritivos (argán o coco).  
- Niasi, Aceites y serums para brillo.  
- Niasi, Ampollas de reparación.  
- Niasi, Ampollas para crecimiento capilar.  
- Niasi, Cremas para definición de rizos.  
- Niasi, Mascarillas capilares intensivas.  
- Niasi, Mascarillas con ingredientes naturales.  
- Niasi, Shampoos y acondicionadores fortalecedores.  
- Niasi, Shampoos y acondicionadores orgánicos.  
- Niasi, Shampoos y acondicionadores sin sulfatos.  
- Niasi, Sueros para cuero cabelludo.  
- Salon Line, Cremas hidratantes para manos y pies.  
- Salon Line, Cremas para peinado.  
- Salon Line, Esmaltes semipermanentes.  
- Salon Line, Geles y ceras moldeadoras.  
- Salon Line, Sprays termoprotectores.  
- Salon Line, Tratamientos para cutículas.  
- Soukai, Alisados progresivos.  
- Soukai, Selladores de cutícula.  
- Soukai, Tratamientos de keratina líquida.  


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



