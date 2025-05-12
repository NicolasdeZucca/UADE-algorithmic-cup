"""ChatBot python"""
# Functions
def escribir_preguntas (question):
    """
    Escribe preguntas faltantes de usuarios en un archivo 'preguntas.txt'
    Parametros: Una pregunta del usuario 
    Sin return, solo escribe preguntas faltantes 
    """
    with open('preguntas.txt', 'w', newline='', encoding='UTF-8') as archivo:
        archivo.write(question)

def leer_preguntas_respuestas ():
    """
    Funcion que lee preguntas del archivo 'preguntas.txt'
    No recibe parametros.
    retorna las preguntas del archivo 'preguntas.txt'
    """
    preguntas_respuestas = []
    with open('preguntas.txt', 'r', encoding='UTF-8') as archivo:

        for line in archivo: # Lee linea por linea el archivo

            # Limpia cada linea y las separa entre preguntas y respuestas
            tupla = tuple(line.strip().replace('\n','').split(':'))
            preguntas_respuestas.append(tupla)


    return preguntas_respuestas



def app ():

    print("\n¡Bienvenido a Catbot! 😺 \nSoy tu asistente virtual inspirado en los gatos de la universidad.\nTe ayudaré con información útil sobre la UADE.\n")

    print("Elije una personalidad para el gato de UADE con el que interactuarás")
    print("1- Nala (Amigable)")
    print("2- Luigi (Curioso)")
    print("3- Otto (Cariñoso)")

# Validacion de personalidad
    while True:
        try:
            personalidad = int(input("Ingresa el número del Catbot que deseas: "))
            if 1 <= personalidad <= 3:
                break

            print("Debes elegir una opción válida.")
            print("Por favor ingresa un numero de Catbot disponible (1 - 2 - 3): ")

        except ValueError:
            print("Error: debes ingresar un número.")



    # personalidades posibles
    if personalidad == 1: #Amigable
        print("\nHola soy Nalaa! Temas para solucionar:\n")
        
        
        preguntas = leer_preguntas_respuestas()

        # Mostrar preguntas enumeradas al usuario
        while True:
            for i, pregunta in enumerate(preguntas):
                print(f"{i+1}- {pregunta[0]}")

            print("0- Salir")

        
            try:
                opcion = int(input("¿Que necesitas resolver?(Indica el número de pregunta - 0 para salir): "))
                if opcion == 0:
                    print("Hasta luego!")
                    break
                elif 0 < opcion < len(preguntas) + 1:
                    respuesta = preguntas[opcion-1]
                    print(f"\nLa respuesta a esa pregunta es: {respuesta[1]}\n")

                else:
                    print(f"\nDebes ingresar un número válido del 1 al {len(preguntas)}\n")
            except ValueError:
                print("\nError: debes ingresar un número.\n")

            



    elif personalidad == 2: # Curioso
        print("Soy Luigi! Actualmente estammos trabajando en esta version.")

    else: # Cariñoso
        print("Soy Otto! ¿Cómo estas? Actualmente estammos trabajando en esta version.")
        
app()
