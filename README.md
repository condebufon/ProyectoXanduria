<h1 align="center">Proyecto Web</h1>
<p align="center"> 
  <a href="" rel="noopener">
 <img width=300px height=200px src=Principalapp/static/img/1.png
</p>

"Proyecto Xanduria es una aplicación web desarrollada en Django que permite a los usuarios gestionar las noticias y eventos y actualizaciones del juego xanduria por la web oficial."

<h1>⏩⏩ Instalación y Ejecución </h1>
- Python (versión 3.6 o superior)
- pip (gestor de paquetes de Python)

<h1>⏩⏩ Clonación y Ejecución <div id="clonar-y-ejecytar"></div> </h1>

1. Para clonar el repositorio se puede hacer de la siguiente forma:
	Ve a la página del proyecto en GitHub y haz clic en el botón "Code", luego selecciona "Download ZIP" para descargar el proyecto como un archivo comprimido. Alternativamente, puedes usar el siguiente enlace:
	
```batch
	https://github.com/condebufon/ProyectoXanduria/archive/refs/heads/base.zip
```

2. Descomprimir el Archivo 
	* Extrae el contenido del archivo ZIP descargado en una carpeta de tu elección.
	
3. Navegar al Directorio del Proyecto
	*Accede al directorio del proyecto descomprimido:
	cd ProyectoXanduria

4. Generar un entorno virtual de python e instalar las dependencias de este proyecto:

> Sistemas basados en GNU/Linux
```batch
python3 -m venv virtual
source virtual/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
> Sistemas Windows
```batch
python -m venv virtual
virtual\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```
5. Crear un Superusuario 
	*Para acceder al panel administrativo, puedes crear un superusuario con el siguiente comando:
	python manage.py createsuperuser
6. Ejecutar el Servidor
	Finalmente, ejecuta el servidor de desarrollo:
	```batch
	python manage.py runserver
	Ahora puedes acceder a la aplicación en tu navegador en http://127.0.0.1:8000.	
	```
<h1>⏩⏩Trabajo futuro <div id="trabajo-futuro"></div></h1>

* [ ] Subirlo a un hostin o Dockerizar la aplicación
* [ ] Sincronizar actualizaciones con la aplicaciones
* [ ] Adaptarlo con javascrips 
* [ ] generar noticias y eventos
<h1>⏩⏩extra o datos adicionales: <div id="extra"></div></h1>
Paso a Paso para Configurar un Archivo.env
1. Crear el archivo.env
Dirígete a la raíz de tu
Crea un archivo llamado .env.
En Linux/MacOS:
```
 .env
```
En Windows: Puedes usar un editor de texto para crear un archivo vacío y guardarlo como .env.
2. Definir tus variables de entorno
Abre el archivo .envy escribe
NOMBRE_VARIABLE=valor
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=mi-contraseña-secreta
API_KEY=tu-api-key
```
3. Ignorar el archivo .enven Git
Para evitar que este archivo sensible se suba a tu repositorio, debes asegurarte de que esté incluido en el archivo .gitignore.

Abre o crea un archivo .gitignoreen la raíz del proyecto.
Añade la siguiente:

```
# Ignorar archivo .env
.env
```
Si ya habías añadido accidentalmente el archivo .enval repositorio, eliminalo del historial de Git:
```
git rm --cached .env
```

4. Proporcionar un archivo de ejemplo ( .env.example)
Para que otros desarrolladores sepan qué variables deben configurar, cree un archivo llamado .env.example.

Incluye solo los nombres de las variables y valores genéricos o ejemplos:
```
DB_HOST=tu-servidor
DB_USER=tu-usuario
DB_PASSWORD=tu-contraseña
API_KEY=tu-api-key
```

cualquier duda o observacion contactar a: https://api.whatsapp.com/send/?phone=573157511161


 
