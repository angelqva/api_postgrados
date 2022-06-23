# POSTGRADOS APIREST

## EJERCICIO

Se desea realizar un sistema para el control de los postgrados de la Universidad de

Camagüey. Se conoce que los postgrados pueden ser nacionales o internacionales. De los

postgrados nacionales se registra el código del postgrado, el tema, la fecha de inicio, la fecha

de terminación, el profesor principal, si fue impartido en la universidad, la cantidad de horas y

los datos de los estudiantes matriculados. De los postgrados internacionales se registra

además el país donde fue impartido, y si es primera vez que se imparte. De los profesores se

registra el carné de identidad, el nombre completo, la edad, la especialidad, la categoría

docente (Titular, Auxiliar, Asistente o Instructor) y la categoría científica (Doctor en Ciencias,

Master en Ciencias o Ninguna). De los estudiantes se registra el número de identificación, el

nombre completo, la edad, la especialidad, el sexo, el año de graduación, el país de residencia

y el país de su nacionalidad. Se conoce que en la universidad se imparten una serie de

postgrados, los cuales son almacenados en una lista, así como una lista de todos los

profesores que imparten postgrados.

El sistema debe permitir las siguientes funcionalidades:

a) Implemente la funcionalidad necesaria para gestionar (insertar, actualizar, eliminar y listar)

los datos de los postgrados de forma independiente (nacionales e internacionales) y de los

profesores.

b) Implemente la funcionalidad necesaria para determinar la colegiatura (precio de inscripción)

de un postgrado dado su código, si se conoce que se calcula de la siguiente forma:

• Los postgrados nacionales se calculan multiplicando $10 por cada crédito, más $15 si

se imparte fuera de la universidad.

• A los postgrados internacionales se le añade $50 si se imparte en el extranjero y $20

si es primera vez que se imparte.

• Los postgrados impartidos por Doctores cobran $17 más de inscripción, mientras que

los impartidos por Masters sólo cobran $9 más de inscripción.

c) Implemente la funcionalidad necesaria para determinar la cantidad de horas de postgrados

internacionales impartidos fuera del país en un curso escolar dado su fecha de inicio y

culminación.

d) Implemente la funcionalidad necesaria para determinar los datos del profesor principal del

postgrado internacional de menor cantidad de créditos impartido en la universidad en lo que

va de año de una especialidad dada, si se sabe que cada crédito equivale a 12 horas clase.

e) Implemente la funcionalidad necesaria para determinar la cantidad de postgrados

empezados el pasado año que no han terminado todavía.

f) Implemente la funcionalidad necesaria para determinar una lista de los postgrados

impartidos en la universidad de una especialidad dada, y que esté ordenado por la cantidad

de créditos de mayor a menor.
