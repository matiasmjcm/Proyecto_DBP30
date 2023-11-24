# A book for you

## Integrantes

- Nicolas Mateo Arroyo Chavez
- Josue Mauricio Arriaga Colchado
- Francisco Escalante Farje
- Matias Jose Castro Mendoza

## Descripcion
El presente proyecto del curso de Desarrollo basado en plataformas, es la página web de una biblioteca virtual (A book for you) en la cual se puede almacenar, rentar y distribuir libros de diferentes categorias para cualquier tipo de usuario. Se puede tener una cuenta personal que te brindara un entorno más personalizado y único.

## Objetivos principales
El principal objetivo de esta entorno es poder adquirir un libro que te guste de las diferentes categorias que contamos y poder nutrirte con su información.

## Mision
Satisfacer íntegramente las necesidades de nuestros clientes, ofreciendo el mayor surtido de libros de texto, lectura e innovación digital.  Satisfaciendo las necesidades de la comunidad educativa con una amplia gama de editoriales para garantizar el aprendizaje y fomentar el amor a la lectura en el público en general.

## Vision
Ser la librería líder en el Perú en la venta y distribución de libros de textos, libros de lectura en general, tanto de editoriales nacionales como extranjeras, reconocida por la calidad de nuestro servicio y la contribución a la comunidad educativa.

## Librerias
- flask
- flask_sqlalchemy
- flask_bcrypt
- flask_cors
- sys
- pytest

## Frameworks
Se utilizo el framework VUE.

## Main Dependencies
- axios
- core-js
- vue
- vue-router

## Development dependencies
- @babel/core
- @babel/eslint-parser
- eslint
- eslint-plugin-prettier
- eslint-config-prettier
- esliner-plugin-vue
- prettier

## Plugins
- @vue/cli-service
- @vue/cli-plugin-babel
- @vue/cli-plugin-eslint
- @vue/cli-plugin-router

## Endpoints
- '/login', methods=['POST']: Inicar sesion

- '/accounts', methods=['GET']: Retorna el account elejido
- '/accounts', methods=['POST']: Crea un account
- '/accounts', methods=['PATCH']: Actualiza un account
- '/accounts', methods=['DELETE']: Borra un account

- '/books', methods=['GET']: Retorna el book elejido
- '/books', methods=['POST']: Crea un book
- '/books', methods=['PATCH']: Actualiza un book
- '/books', methods=['DELETE'] Borra un book

- '/authors', methods=['GET']: Retorna el author elejido
- '/authors', methods=['POST']: Crea un author
- '/authors', methods=['PATCH']: Actualiza un author
- '/authors', methods=['DELETE']: Borra un author

## Host
- Vue  : localhost:8080 
- Flask: http://127.0.0.1:5001/
- localhost: 5432
- port: 5001

## Manejo de errores
- 401: Unauthorized (informacion entregada invalida)
- 403: Forbidden (falta de permisos para acceder a la pagina)
- 404: Not found (pagina no encontrada)
- 500: Internal server error (Error de servidor)

## Ejecutar el archivo 
- FLASK_ENV=development
- FLASK_APP=server
- flask run
- vue ui

## Autores

|                     <a target="_blank">**Francisco Escalante**</a>                  |                           <a target="_blank">**Matias Castro**</a>                            |                   <a target="_blank">**Josué Arriaga**</a>                    |                    <a target="_blank">**Nicolás Arroyo**</a>                             |
|:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
|           ![Francisco](https://avatars.githubusercontent.com/u/83974266)            |                   ![Matias](https://avatars.githubusercontent.com/u/83974266)                 |          ![Josué](https://avatars.githubusercontent.com/u/83974555)           |       ![Nicolás](https://avatars.githubusercontent.com/u/83975293)              
| <a href="https://github.com/bluuemeany" target="_blank">`github.com/bluuemeany`</a> | <a href="https://github.com/matiasmjcm" target="_blank">`github.com/matiasmjcm`</a>           | <a href="https://github.com/jmac-94" target="_blank">`github.com/jmac94`</a>  | <a href="https://github.com/NicolasArroyo" target="_blank">`github.com/NicolasArroyo`</a>|