El comando SELECT se utiliza para consultar información almacenada en una base de datos. Puede combinarse con cláusulas que permiten ordenar, limitar, agrupar y relacionar datos de distintas tablas.

Funcionalidad

¿Para qué sirve?

Sintaxis básica

Ejemplo

ORDER BY

Ordena las filas del resultado por una o más columnas. ASC es ascendente y DESC descendente.

SELECT ... FROM tabla ORDER BY columna ASC/DESC;

SELECT * FROM Books ORDER BY Name ASC;

LIMIT

Restringe la cantidad máxima de filas devueltas por el SELECT.

SELECT ... FROM tabla LIMIT cantidad;

SELECT * FROM Books LIMIT 3;

GROUP BY

Agrupa filas que tienen valores iguales para aplicar funciones como COUNT, SUM, AVG, MIN o MAX.

SELECT columna, COUNT(*) FROM tabla GROUP BY columna;

SELECT State, COUNT(*) FROM Rents GROUP BY State;

INNER JOIN

Devuelve únicamente las filas que tienen coincidencia en ambas tablas.

tabla1 INNER JOIN tabla2 ON condición

Libros que sí tienen un registro de renta.

LEFT JOIN

Devuelve todas las filas de la tabla izquierda y las coincidencias de la derecha. Cuando no hay coincidencia, devuelve NULL.

tabla1 LEFT JOIN tabla2 ON condición

Todos los libros, aunque no tengan autor.

RIGHT JOIN

Devuelve todas las filas de la tabla derecha y las coincidencias de la izquierda. Cuando no hay coincidencia, devuelve NULL.

tabla1 RIGHT JOIN tabla2 ON condición

Todos los autores, aunque no tengan libros.
