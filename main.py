"""
Crea un programa en Python que funcione como un bot en la consola. El bot debe:

Mostrar un mensaje de bienvenida al iniciar, indicando su nombre y cómo usar los comandos básicos.

Permitir al usuario escribir comandos y responder en consecuencia:

hola → el bot responde con un saludo.

hora → el bot muestra la hora actual en formato HH:MM.

ayuda → el bot muestra una lista de comandos disponibles y su descripción.

salir → el bot muestra un mensaje de despedida y finaliza el programa.

Cualquier otro texto → el bot responde indicando que no entiende el comando y sugiere escribir ayuda.

Usar un bucle para que el bot siga funcionando hasta que el usuario escriba salir.

(Opcional) Mostrar siempre el texto en minúsculas, aunque el usuario lo escriba en mayúsculas o mezclado.
"""
from funciones import mostrar_ayuda, mostrar_hora, saludar_usuario, mostrar_hora, despedida

print("Bot Sara")
print("Escribe la palabra ayuda para ver las opciones disponibles")
print("Si escribes salir se sale del programa")



saludar_usuario()

while True:
    comando = input("Elige un comando: ")
    comando = comando.strip().lower()
    if comando == "salir":
        despedida()
        break
    elif comando == "ayuda":
        mostrar_ayuda()
    elif comando == "hola":
        saludar_usuario()
    elif comando == "hora":
        mostrar_hora()
    else:
        print("No te he entendido. Escribe 'ayuda' para ver los comandos")
