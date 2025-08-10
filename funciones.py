from datetime import datetime

def mostrar_ayuda():
    print("lista de comanos disponibles: ")
    print("hola: saludo")
    print("hora: hora actual")
    print("ayuda: lista de comandos")
    print("salir: salir del bot")

def mostrar_hora():
    hora_actual = datetime.now().strftime("%H:%M")
    print("Hora actual: ", hora_actual)

def saludar_usuario():
    print("¡Hola! Encantado de saludarte")


def despedida():
    print("Hasta luego, gracias por usar el bot")
