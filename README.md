# Movies
## Ejecución
~~~
pip install -r requirements.txt
fastapi dev app/main.py
~~~
## Objetivo
Construir una API Restful con las siguientes características:

Procesar el archivo con datos de 5000 películas extraídas de IMDB.

Exponer los servicios que contestan las siguientes preguntas:

- ¿Cuántas películas a "color" y "blanco y negro" hay en la lista?
- ¿Cuántas películas produjo cada director?
- ¿Cuáles son las 10 películas menos criticadas?
- ¿Cuáles son las 20 películas con mayor duración?
- ¿Cuáles son las 5 películas que recaudaron más dinero?
- ¿Cuáles son las 5 películas que recaudaron menos dinero?
- ¿Cuáles son las 3 películas que gastaron mayor cantidad de dinero para producirse?
- ¿Cuáles son las 3 películas que gastaron menor cantidad de dinero para producirse?
- ¿En qué año se lanzaron más películas?
- ¿En qué año se lanzaron menos películas?
- Mostrar el ranking de actores ordenado por actuaciones y popularidad.
    -  Crear un ranking de actores donde aparezca:
        - La cantidad de películas en las que participó el actor
        - Su influencia en las redes sociales
        - Su mejor película
        - Ordenado por cantidad de actuaciones
- Crear un tag cloud usando los tags o keywords de las películas. Para hacer esto solo basta con crear y mostrarun ranking de palabras y su peso (cantidad de apariciones de la palabra), ordenado de mayor a menor.
- ¿Qué género de películas recaudó más dinero para cada año?
- ¿Qué género de películas recaudó menos dinero para cada año?
- ¿Qué género les gusta más a las personas?
- ¿Cuáles son los 5 directores con mejor reputación?

Consideraciones:

- No utilizar el paquete pandas para realizar esta implementación. Solo usar el Standard Library.
- Considerar performance a la hora de exponer los servicios y procesar el archivo
- Implementar test unitario