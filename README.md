# Qué hace esto
Esto es un BOT troll para grupos en Telegram programado para que cree una serie de situaciones aleatorias y de forma asidua:

- Responder "Me espero a la película", "¿Y el resumen?"... o lo que se defina en un fichero .json cuando alguien escribe mucho texto por el grupo.
- Responder "No clico ahí ni con tu ratón", "100% real no face 1 link mega"... si alguien ha pasado una dirección Web poco fiable.
- Meterse con una persona que escribe con faltas o se ríe.
- Llamar machista o similar al quien realiza un comentario sexista.
- Contestar "Yo siempre le echo 20€ a mi X" o "Poco me parece" cuando alguien habla de cantidades. Por ejemplo:
  
 ```
  Pepe: alguien sabe de una aspiradora buena/bonita/barata por menos de 150 pavos??
  Bot: Yo siempre le echo 20€ a mi aspiradora
 ```
  
- Contestar "El/la/los/las mejor/es X en Madrid" si alguien habla de una localización. Ejemplo:
  
  ```
  María: a ver cuando hacemos una barbacoa aquí por Valencia!
  Bot: Las mejores barbacoas en Madrid.
  ```
  
- Mantener una conversación con él tipo ChatGPT, ya sea mencionándolo o aleatoriamente en ciertos mensajes.
  
También hace cosas serias, como hacer un Webscraping para devolver el valor del Bitcoin actual con el comando /btc.


# Requisitos previos

Para hacer funcional el bot es necesario reunir dos tokens:

* OpenAI API
* Telegram token HTTP API para el BOT

En ambas es necesario registrarse. Para el segundo caso, escribirle a @BotFather y crear un nuevo Bot para Telegram.

Actualmente el Bot lo utilizo de aprendizaje, así que los token se pegan directamente en el código, aunque no es una práctica recomendable. Es mejor
guardarlo en una variable de entorno o leerlo desde un .txt (por ejemplo) separado. El de OpenAI está en la línea cuatro (4) del archivo *messages.py*
y el de Telegram en la ocho (8) del fichero *app.py*.


# Crear un DNS

Webhook de telegram necesita de una dirección HTTPS segura para establecer la conexión con nuestro bot. Hay varias formas de hacerlo. Yo lo tengo con
duckdns, aunque funciona también ngrok.

### Con Duckdns

Nos vamos a su página principal y creamos una cuenta -en mi caso, usando la mía de github-. Se nos facilitará un token, lo apuntamos y nos generamos
un dominio con el nombre que queramos.

Suponiendo que ya tenemos Docker instalado, sólo tenemos que lanzar esta línea en la terminal:

```
$ docker create \
  --name=duckdns \
  -e PUID=<puid> \
  -e PGID=<pgid> \
  -e TZ=Europe/Madrid \
  -e SUBDOMAINS=<dominio> \
  -e TOKEN=<token> \
  --restart unless-stopped \
  linuxserver/duckdns
```
      
A tener en cuenta:

* puid y pgid se consultan desde la terminal con el comando id <usuario>. Ejemplo: "id root".
* dominio es el que hayamos registrado anteriormente en la página quitando "duckdns.org".

Ahora sólo nos queda ejecutar la imagen con:

`$ docker start duckdns`


# Configurar Webhook

En [este enlace](https://core.telegram.org/bots/webhooks) se detalla la guía completa de cómo configurar nuestro servidor para que podamos establecer
un Webhook con Telegram. En mi caso voy a resumir los pasos en los siguientes:

1) Abrimos los puertos necesarios para la app con:

`$ sudo ufw allow <port>/tcp`

2) Permitir hacer POST's a las siguientes direcciones:

* 149.154.160.0/20
* 91.108.4.0/22
* 149.154.167.192/26

con el comando...

`$ sudo ufw allow in on interfacename to any port <port> proto tcp from <ip>`

donde *port* es el puerto que vamos a usar e *ip* las direcciones aportadas en la lista interior. 

3) Forzar a gunicorn a usar tráfico TLS1.2. En el fichero Dockerfile ya está añadido.

4) Crearnos un certificado SSL en la raíz de nuestros archivos con la siguiente instrucción:

`$ openssl req -newkey rsa:2048 -sha256 -nodes -keyout <keyname>.key -x509 -days 365 -out <certname>.pem -subj "/C=<country code>/ST=<province>/L=<city>/O=<company name>/CN=<domain>"`

donde...

* keyname es el nombre que queramos ponerle al fichero .key que vamos a generar. Lo mismo para certname.
* country code son las dos (2) letras de nuestro país. En mi caso, España, "ES".
* <domain> es el nombre que le pusimos al dominio entero, es decir, añadiéndole "duckdns.org".


5) Establecer el Webhook. En la documentación de la API de Telegram se nos detalla. Aunque básicamente sólo tenemos que hacer una petición POST a 
la siguiente ruta:
  
https://api.telegram.org/bot<token_id>/setWebhook
  
En *token_id* escribimos el que nos aportó Telegram. Además, pasarle un par de parámetros obligatorios. En mi caso lo hice con Postman.
  
* url: https://*domain*.duckdns.org
* certificate: el archivo .pem generado anteriormente.


# Modelo sexista

Para conseguir el dataset es necesario rellenar [este formulario](https://forms.office.com/Pages/ResponsePage.aspx?id=SHBYtXCgrUO2VCCjHpstmc1J3Gu50zdMhFmXSTrhRZJUM1FQUTlSUUNQMEZZR01SRTVMVDg3SktaSC4u). Una vez conseguido, basta con ejecutar una a una cada celda del notebook del repositorio. Guardamos el modelo creado para que el bot pueda hacer predicciones sobre él.

  
# Ejecutar la app
  
  Ya sólo nos queda poner en marcha nuestro contenedor Docker. Para ellos, debemos asegurarnos en el fichero Dockerfile que estamos exponiendo el puerto
  en el que vamos a ejecutar el servidor con gunicorn. Y también, que se vayan a lanzar el archivo .pem y .key con los nombres que designamos anteriormente.
  
  Una vez comprobado esto, lanzamos estas dos líneas en nuestra terminar en la raíz de los archivos:
  
  `$ docker build --tag <image name> .`
  
  `$ docker run -d -p 443:<port> <image name>`
  
  Y listo. Ya tendríamos nuestro bot de Telegram en nuestro servidor VPS con un Webhook.
