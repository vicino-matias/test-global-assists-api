# Customer API with Flask
## Se utilizo POSTMAN para las pruebas y se recomienda lo mismo para sus pruebas. En caso de necesitar un deploy del mismo, se recomienda el uso de Heroku CLI o Vercel.
### Este es un servicio API simple basado en Python y Flask que maneja una lista de clientes utilizando un archivo JSON como base de datos. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los clientes.

## Descripción del Proyecto
La API proporciona los siguientes endpoints para interactuar con los datos de los clientes:

### GET /customer/
Retorna la lista completa de clientes.

### GET /customer/<id>
Retorna un cliente específico identificado por su id.

### POST /customer/
Crea un nuevo cliente. El cuerpo de la solicitud debe incluir el id y el first_name del cliente.

### PUT /customer/<id>
Actualiza los datos de un cliente específico identificado por su id.

### DELETE /customer/<id>
Elimina un cliente específico identificado por su id.

## Los datos se almacenan en un archivo JSON en el sistema de archivos, lo que permite mantener los datos persistentes entre reinicios del servidor.

# Archivo app.py
## Este es el archivo principal de la API.

### DATA_FILE: Define la ruta del archivo JSON donde se almacenan los datos de los clientes.

### La función "load_data" carga los datos de los clientes desde el archivo JSON si existe. Si el archivo no existe, devuelve una lista vacía.
### La función "save_data" guarda los datos de los clientes en el archivo JSON con una estructura indentada para legibilidad.

# Rutas de la API
## Cada una de las rutas de la API está asociada a una de las operaciones CRUD:
### La ruta "GET /customer/" devuelve la lista completa de clientes en formato JSON.
### La ruta "GET /customer/<id>" busca un cliente por su id y lo devuelve. Si no se encuentra el cliente, responde con un error 404.
### La ruta "POST /customer/" crea un nuevo cliente. Requiere que el cuerpo de la solicitud contenga un id y un first_name. Si el cliente ya existe, responde con un error 400.
### La ruta "PUT /customer/<id" permite actualizar los datos de un cliente específico.
### La ruta "DELETE /customer/<id>" elimina un cliente por su id.

# Requisitos

## Para ejecutar esta API, necesitas tener Python y las siguientes dependencias instaladas:

### Flask: Framework web para Python.
### JSON: Para manejar los datos de los clientes en formato JSON.

### Puedes instalar las dependencias utilizando pip:
pip install -r requirements.txt

