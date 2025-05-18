# PREGUNTAS A RESPONDER

en este apartado se encuentran las preguntas que se deben responder sobre el proyecto.

## Pregunta 1

**¿Qué ventajas ofrece GraphQL sobre REST en este contexto?**

- **Consultas precisas:** El cliente puede pedir solo los datos que necesita, evitando el exceso o falta de información.
- **Menos endpoints:** Todo se maneja desde un único punto de entrada (`/graphql`), lo que simplifica el diseño del backend.
- **Reducción de llamadas a la red:** Se pueden solicitar múltiples recursos en una sola consulta, mejorando la eficiencia.
- **Tipado fuerte:** GraphQL obliga a definir un esquema, lo que facilita el desarrollo, depuración y documentación.
- **Adaptabilidad:** Si el frontend necesita nuevos campos, no se necesita modificar los endpoints, solo ajustar la consulta.

## Pregunta 2

**¿Cómo se definen los tipos y resolvers en una API con GraphQL?**

- **Tipos (Types):** Definen la estructura de los datos.
  ```python
  class ProductType(graphene.ObjectType):
      id = graphene.Int()
      title = graphene.String()
      price = graphene.Float()
      stock = graphene.Int()
      disponible = graphene.Boolean()
  ```

- **Consultas (Query):** Definen qué datos pueden pedirse y cómo obtenerlos.
  ```python
  class Query(graphene.ObjectType):
      all_products = graphene.List(ProductType)

      def resolve_all_products(root, info):
          return ProductService.get_all()
  ```

- **Mutaciones (Mutation):** Permiten modificar datos en el backend.
  ```python
  class UpdateStock(graphene.Mutation):
      class Arguments:
          product_id = graphene.Int()
          change = graphene.Int()

      product = graphene.Field(ProductType)

      def mutate(root, info, product_id, change):
          updated = ProductService.update_stock(product_id, change)
          return UpdateStock(product=updated)
  ```

## Pregunta 3

**¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?**

- **Evita inconsistencias:** El estado de disponibilidad depende del stock y debe ser coherente.
- **Mayor seguridad:** El backend es la fuente de verdad; el frontend puede ser manipulado.
- **Escalabilidad:** Si otros clientes (apps, integraciones) acceden al backend, deben recibir datos correctos.
- **Fácil mantenimiento:** La lógica se centraliza en un único lugar, evitando duplicación o errores.

## Pregunta 4

**¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?**

- **Encapsular la lógica** en un único método de servicio, como `update_stock`, que actualice stock y `disponible`.
- **No permitir que `disponible` se modifique directamente** desde el frontend.
- **Crear tests unitarios** para validar que al modificar el stock, el campo `disponible` se actualice correctamente.
- **Evitar duplicación** de lógica en distintas capas o archivos del sistema.