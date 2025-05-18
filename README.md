<h1 align="center"> FlaskInventory </h1>
<div align="center">
  <image src="./resources/Logo.png" align="center" width="300" height="300" />
</div>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="empty" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

Para más información sobre el requisitado del proyecto, consulte el archivo [REQUISITADO](docs/requirements/README.md)

Para más información sobre las respuestas a las preguntas del proyecto, consulte el archivo [RESPUESTAS](docs/answers/README.md)

## Descripción

FlaskInventory es una aplicación web que realizar compras de productos de una tienda ficticia. La aplicación fue desarrollada con Flask y GraphQL como API. La aplicación consume la API de [Fake Store API](https://fakestoreapi.com) para obtener los productos que se muestran en la tienda.

## Instalación

El proyecto esta dockerizado, por lo que para correrlo solo es necesario tener instalado Docker y Docker Compose en su máquina. Para correr el proyecto, siga los siguientes pasos:

1. Clone el repositorio en su máquina local
2. Navegue a la carpeta del proyecto
3. Cree un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```sh
APP_PORT=8080
```

4. Ejecute el siguiente comando para construir y correr los contenedores de Docker:

```sh
docker-compose up -d
```

5. El proyecto es una API RESTful, por lo que no tiene una interfaz gráfica. Para probar la API, puede usar herramientas como Postman o Insomnia. La API estará disponible en la siguiente URL:

```sh
http://localhost:8080/graphql/
```

