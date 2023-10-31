![Henry](HENRRSS_Chicacongato.jpg)

# Proyecto-SteamGames-FastAPI

##

## Flujo de trabajo

El proyecto de MLOps para Steam Games se centra en el desarrollo de un sistema de Machine Learning destinado a analizar y predecir los precios de los videojuegos disponibles en la plataforma Steam. Este sistema se basa en un riguroso proceso de transformación y preprocesamiento de los datos, que es el primer paso en el flujo de trabajo del proyecto.

El preprocesamiento de los datos es una etapa crucial en el flujo de trabajo del proyecto. Durante esta etapa, se analizan y procesan los datos disponibles, que incluyen diversas características de los videojuegos. Estas características pueden incluir, pero no se limitan a, el género del juego, la fecha de su lanzamiento,entre otros.

Una vez que los datos han sido preprocesados, se utilizan para formar un conjunto de funciones. Estas funciones son fundamentales para el análisis y la predicción.
Las funciones se detallarán más adelante en el proyecto.

El uso de técnicas de Ciencia de Datos en este proyecto permite un análisis detallado de los datos, lo que a su vez facilita la creación de un sistema de Machine Learning preciso y eficiente. Este sistema de Machine Learning es esencial para el proyecto.

Una vez que se ha completado la fase de transformación y preprocesamiento de los datos, el proyecto de MLOps para Steam Games se adentra en la etapa del modelo de Machine Learning. Esta etapa es fundamental para el desarrollo del sistema de recomendación de juegos que se propone.

En esta etapa, el proyecto comienza con una exhaustiva exploración de los datos (EDA, por sus siglas en inglés). El EDA es un proceso esencial que implica analizar los datos para entender su estructura, distribución y cualquier relación entre las variables. A través del EDA, se pueden identificar posibles problemas con los datos, como valores faltantes o fuera de rango, y se puede obtener una comprensión más profunda de los datos que se utilizarán para entrenar el modelo de Machine Learning.

Una vez que se ha realizado el EDA, el proyecto pasa a la construcción del modelo de Machine Learning. En esta etapa, se selecciona un algoritmo de Machine Learning adecuado para el problema, se configuran los parámetros del modelo y se preparan los datos para el entrenamiento del modelo.

Después de la construcción del modelo, el proyecto se adentra en la etapa de entrenamiento del modelo. Durante el entrenamiento, el modelo aprende de los datos utilizando un algoritmo que se ajusta los parámetros del modelo para minimizar el error en las predicciones del modelo.

Finalmente, después de que el modelo ha sido entrenado y optimizado, el proyecto pasa a la etapa de despliegue del modelo. En esta etapa, el modelo entrenado se implementa en un entorno de producción, donde puede comenzar a hacer recomendaciones de juegos basadas en los gustos de los usuarios.

En resumen, la etapa del modelo de Machine Learning del proyecto de MLOps para Steam Games es una fase crucial que implica una serie de pasos, desde el EDA hasta la construcción, entrenamiento y despliegue de un modelo de Machine Learning. Este modelo de Machine Learning es esencial para el proyecto, ya que permite hacer recomendaciones de juegos basadas en los gustos de los usuarios de una manera precisa y eficiente.

#

#

El sistema de MLOps para Steam Games se despliega como una API utilizando FastAPI, una biblioteca moderna y rápida para construir APIs con Python. Esta decisión de despliegue permite a los usuarios interactuar con el modelo de Machine Learning a través de solicitudes HTTP, proporcionando una interfaz fácil de usar para acceder a las funcionalidades del sistema.

Una de las funcionalidades clave ofrecidas por esta API es la capacidad de obtener información detallada sobre la cantidad de ítems y el porcentaje de contenido gratuito proporcionado por las empresas desarrolladoras en un determinado año. Esta funcionalidad es esencial para entender la oferta de los desarrolladores y para tener una idea de la competencia en el mercado.

Además, la API proporciona una funcionalidad para devolver los tres desarrolladores con los juegos más recomendados por los usuarios para un año dado. Esta funcionalidad es útil para identificar a los desarrolladores que tienen una mayor satisfacción del usuario y para tomar decisiones informadas sobre qué juegos promover o desarrollar.

Otra funcionalidad intrigante de la API es la capacidad de devolver un diccionario con el nombre del desarrollador como clave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo. Esta funcionalidad permite a los usuarios y a los desarrolladores entender el sentimiento general de los usuarios hacia los juegos de un desarrollador específico.

Finalmente, la API utiliza el modelo de Machine Learning entrenado para proporcionar recomendaciones de juegos a los usuarios. Los usuarios simplemente ingresan el ID de un usuario, y la API devuelve una lista de los cinco juegos más recomendados para ese usuario. Esta funcionalidad es esencial para proporcionar una experiencia de usuario personalizada y mejorar la satisfacción del usuario.

### 1) [Preprocesamiento de datos] (https://github.com/jeferson-bot/Individual_Proyect_01/tree/main/E_T_L)

En el proceso de limpieza de los datos, se tomaron varias medidas para manejar la columna 'price', que será la variable dependiente en nuestro modelo de predicción:

    - Tratamiento de la columna 'price': Se reemplazaron los juegos con precios "Free, Free to Play, etc" por un precio de 0. Esto se hizo para evitar la pérdida de datos significativos. Además, se eliminaron las filas con valores nulos en la columna 'price', ya que estos no representaban un número significativo de datos.
    - Tratamiento de la columna 'sentiment': Se agruparon los registros con pocos reviews en una sola característica llamada "pocos reviews". Los valores nulos se mantuvieron como "unknown" temporalmente para no perder información.
    - Tratamiento de la columna 'release_date': Se eliminaron las filas con valores nulos en esta columna, ya que no eran significativos y no se podía asignar una fecha específica. Además, se cambió el tipo de dato a datetime y se agregó una columna 'año' que será útil para futuras analíticas.
    - Eliminación de duplicados: Se eliminaron las filas duplicadas en las columnas 'title' e 'id', ya que no era valioso tener información repetida sobre el mismo videojuego.
    Comparación de columnas: Se hizo una comparación entre la columna 'title' vs. 'app_name' y 'publisher' vs. 'developer' para decidir cuál conservar, ya que a simple vista parecían tener información similar.
    - Eliminación de columnas innecesarias: Se eliminaron las columnas que no eran útiles para el análisis.

### 2) Funciones de recomendación

- La función userdata(User_id: str) se utiliza para obtener estadísticas detalladas sobre un usuario específico en base a su ID. Esta función devuelve tres tipos de información:

  Cantidad de dinero gastado por el usuario: Esta información se obtiene sumando el precio de todos los elementos que el usuario ha comprado. Esto proporciona una visión general del gasto total del usuario en tu plataforma.
  Porcentaje de recomendación basado en reviews.recommend: Este dato se calcula como el promedio de las puntuaciones de recomendación que el usuario ha dado a los elementos. Esto puede indicar qué tan probable es que el usuario recomiende un elemento a otros.
  Cantidad de items: Esta es simplemente el número total de elementos que el usuario ha comprado o interactuado con. Esto puede proporcionar una idea de la actividad del usuario en tu plataforma.
  En resumen, esta función proporciona una visión detallada del comportamiento del usuario en tu plataforma, incluyendo su gasto total, su tendencia a recomendar elementos y su actividad general.

- La función best_developer_year(año: int) se utiliza para analizar las estadísticas de los desarrolladores de juegos en un año específico. Esta función devuelve el top 3 de los desarrolladores cuyos juegos han sido más recomendados por los usuarios.

  La recomendación se basa en dos criterios:

  - reviews.recommend = True: Esto significa que la recomendación proviene de los usuarios que han recomendado el juego.
    Comentarios positivos: Esto indica que los usuarios que han recomendado el juego han dejado comentarios positivos sobre él.
    El resultado de esta función es una lista de los tres desarrolladores que han tenido los juegos más recomendados en el año especificado. Esto puede ser útil para identificar a los desarrolladores que han tenido un impacto significativo en la comunidad de juegos en un año dado.

- La función developer_reviews_analysis(desarrolladora: str) se utiliza para analizar las reseñas de los usuarios de los juegos desarrollados por un desarrollador específico. Esta función devuelve un diccionario que contiene el nombre del desarrollador como clave y una lista como valor. La lista contiene dos elementos: la cantidad total de registros de reseñas de usuarios y un análisis de sentimiento de esas reseñas.

  El análisis de sentimiento categoriza las reseñas como positivas o negativas. Esto se hace para entender la percepción general de los usuarios sobre los juegos del desarrollador. Un análisis de sentimiento positivo indica que los usuarios disfrutaron de los juegos y tuvieron una experiencia generalmente positiva. Por otro lado, un análisis de sentimiento negativo indica que los usuarios tuvieron una experiencia generalmente negativa con los juegos.

  Esta función es útil para entender cómo los usuarios perciben los juegos de un desarrollador específico y cómo esas percepciones pueden afectar las decisiones de los usuarios sobre qué juegos comprar o jugar.

# 3) MLOps: Modelo de aprendizaje automático.

El sistema de recomendación es un enfoque basado en filtrado colaborativo de usuario-ítem.
Este método se basa en la idea de que si dos usuarios son similares en términos de sus interacciones con los ítems (en este caso, los juegos), entonces es probable que ambos disfruten de los mismos ítems.

Aquí está un desglose más detallado de cómo funciona este sistema:

    - Identificar usuarios similares: El primer paso es identificar a los usuarios que son similares al usuario objetivo. Esto se puede hacer comparando las interacciones del usuario objetivo con las de otros usuarios. Por ejemplo, si dos usuarios han jugado a los mismos juegos y han dado calificaciones similares a esos juegos, entonces es probable que sean similares.
    - Recomendar ítems: Una vez que se han identificado los usuarios similares, el sistema puede recomendar los ítems que a esos usuarios similares les gustaron. Esto se hace buscando los ítems que los usuarios similares han interactuado positivamente (por ejemplo, jugando a ellos o dándoles una alta calificación) y que el usuario objetivo aún no ha interactuado.
    - Filtrar recomendaciones: Finalmente, el sistema puede filtrar las recomendaciones para eliminar los ítems que el usuario objetivo ya ha interactuado. Esto asegura que las recomendaciones sean relevantes y útiles para el usuario.
    Este sistema de recomendación es muy eficaz porque se basa en las interacciones reales de los usuarios con los ítems. Sin embargo, puede ser menos eficaz si hay muy pocos usuarios que sean similares al usuario objetivo, o si los usuarios tienen interacciones muy dispersas con los ítems. En estos casos, puede ser útil combinar el filtrado colaborativo de usuario-ítem con otros métodos de recomendación, como el basado en contenido.

- La función recomendacion_usuario(id de usuario) es una parte integral de un sistema de recomendación basado en machine learning. Esta función toma como entrada el ID de un usuario y devuelve una lista de 5 juegos recomendados para ese usuario.

  El sistema de recomendación utiliza un modelo de machine learning para analizar el comportamiento de los usuarios y hacer predicciones sobre qué juegos podrían disfrutar en base a sus interacciones anteriores con otros juegos. El modelo puede tener en cuenta una variedad de factores, como los juegos que el usuario ha comprado o jugado anteriormente, las calificaciones que ha dado a esos juegos, y las reseñas de otros usuarios que tienen comportamientos similares.

  La lista de 5 juegos recomendados que devuelve la función es una selección de los juegos que el modelo predice que el usuario disfrutará más. Estas recomendaciones pueden ayudar al usuario a descubrir nuevos juegos que le gusten y a mejorar su experiencia en la plataforma.

# Links útiles

- Repositorio (Github): https://github.com/jeferson-bot/Individual_Proyect_01
- Deploy del Proyecto (Render):
- Video explicativo (Drive):
