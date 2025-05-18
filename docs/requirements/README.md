# REQUISITADO

En este apartado se encuentran los requerimientos necesarios para la ejecución del proyecto.

## Objetivo

Construir un backend utilizando Flask y GraphQL que permita gestionar el inventario de productos de una tienda online. Este backend se conectará al frontend ya creado en Vue en la práctica anterior, que maneja la reactividad de productos según el stock.

## Enunciado

En la práctica anterior, se ha desarrollado un frontend en Vue que permite mostrar dinámicamente productos disponibles y no disponibles según su stock. Ahora, necesitas implementar el backend de esta tienda online usando Flask y GraphQL, cumpliendo los siguientes requerimientos:

### Requisitos funcionales del backend

1. **Base de datos en memoria:**
   1. Los productos estarán almacenados en una lista de Python al arrancar la app.
   2. Cada producto es un diccionario con:
      1. id (int)
      2. nombre (str)
      3. precio (float)
      4. stock (int)
      5. disponible (bool)
2. **Esquema GraphQL:**
   1. Consulta (Query) para obtener todos los productos.
   2. Mutación (Mutation) para:
      1. Modificar el stock de un producto (incrementar o disminuir).
      2. El campo disponible debe actualizarse automáticamente en función del stock, igual que en el frontend.
3. **Lógica adicional obligatoria (importante):**
   1. Si el stock de un producto llega a 0, disponible debe ponerse en false.
   2. Si el stock de un producto aumenta desde 0, disponible debe volver a true.
   3. Esta lógica debe aplicarse en el backend (no puede depender del frontend para que se actualice).
