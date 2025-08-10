Este proyecto es un bot básico que funciona desde la consola, permitiendo al usuario interactuar con diferentes comandos como saludar, ver la hora, obtener ayuda o salir. El código está dividido en funciones para mantener la organización.

## main.py

print("Bot Sara")
print("Escribe la palabra ayuda para ver las opciones disponibles")
print("Si escribes salir se sale del programa")

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

# funciones.py

from datetime import datetime

def mostrar_ayuda():
    print("Lista de comandos disponibles:")
    print("hola: saludo")
    print("hora: hora actual")
    print("ayuda: lista de comandos")
    print("salir: salir del bot")

def mostrar_hora():
    hora_actual = datetime.now().strftime("%H:%M")
    print("Hora actual:", hora_actual)

def saludar_usuario():
    print("¡Hola! Encantado de saludarte")

def despedida():
    print("Hasta luego, gracias por usar el bot")


