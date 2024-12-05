
# Kommo API test

Este proyecto utiliza un servidor local en Python, expuesto públicamente a través de Ngrok, para recibir webhooks enviados por Kommo. Los datos recibidos se utilizan para recuperar información de una hoja de cálculo de Google Sheets mediante la API de Google Sheets. Con esa información, se actualiza un campo específico de un lead en Kommo utilizando la API de Kommo.


## Dependencias -python 3.13

```bash
  pip install flask

```
```bash
  pip install requests

```
```bash
  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

```
```bash
  pip install python-dotenv

```



## Variables de entorno y credenciales

Para ejecutar este proyecto, deberás añadir las siguientes variables de entorno a tu archivo .env

`KOMMO_ACCES_TOKEN`

Tambien necesitaras las credenciales de una cuenta de servicio para el proyecto de GCP (Google Cloud Platform). En formato JSON.

`kommo.json`


## Ejecuta el proyecto

```bash
  python webhookReceiver.py
```
El servidor se levantará por defecto en el puerto 5000
```python
  if __name__ == "__main__":
    app.run(port=5000)
```
## Exponer el servidor local

Para que Kommo pueda enviar webhooks al servidor, necesitas exponer el puerto local a una URL pública. Esto se puede conseguir con [Ngrok](https://ngrok.com/).

Configurar Ngrok:

Antes de usarlo, debes autenticar Ngrok con tu token personal:
```bash
  ngrok config add-authtoken TU_TOKEN
```
Ejecutar el túnel:

Una vez autenticado, inicia un túnel para el puerto 5000:

```bash
  ngrok http 5000
```
Esto generará una URL pública, como:

```bash
  Forwarding      https://abcd1234.ngrok-free.app -> http://localhost:5000

```
La ruta definida en el servidor para recibir webhooks es "/webhook". Esto significa que el endpoint para recibir las solicitudes sería:

https://abcd1234.ngrok-free.app/webhook