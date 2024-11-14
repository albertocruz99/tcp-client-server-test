Pruebas Manuales
Prueba 1: Envío de mensaje normal

Inicie el servidor
Inicie el cliente
En el cliente, escriba un mensaje cualquiera (ejemplo: "hola servidor")
Verifique que el servidor responda con el mensaje en mayúsculas

Cómo probar el codigo:
1. Primero, necesitarás tener dos terminales o ventanas de comando abiertas. En una ejecutaremos el servidor y en la otra el cliente.
2. En la primera terminal, inicia el servidor:
    python server.py o python3 server.py
    Deberías ver un mensaje como:
        Servidor iniciado en localhost:5000
    En la segunda terminal, inicia el cliente:
    python client.py
    Conectado al servidor
    Ingrese un mensaje (o 'DESCONEXION' para salir):

En la terminal del cliente, escribe un mensaje, por ejemplo:
    Ingrese un mensaje (o 'DESCONEXION' para salir): hola servidor
Deberías ver la respuesta:
    Respuesta del servidor: HOLA SERVIDOR

En la terminal del servidor, deberías ver algo como:

Cliente conectado desde ('127.0.0.1', XXXXX)
Mensaje recibido: hola servidor

Prueba 2: Prueba de desconexión

Inicie el servidor
Inicie el cliente
En el cliente, escriba "DESCONEXION"
Verifique que:

El cliente se desconecte y termine su ejecución
El servidor permanezca activo y listo para nuevas conexiones

En la terminal del cliente, escribe:
    Ingrese un mensaje (o 'DESCONEXION' para salir): DESCONEXION
Deberías ver:
    Desconectando del servidor...

Despues de eso el cliente se cerrará
En la terminal del servidor, deberías ver:
    Cliente solicitó desconexión

***Comportamiento Esperado

***El servidor convierte cualquier mensaje recibido a mayúsculas y lo devuelve al cliente
***Al enviar "DESCONEXION", el cliente se desconecta y el servidor queda listo para nuevas conexiones