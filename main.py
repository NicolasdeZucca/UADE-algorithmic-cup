"""ChatBot python"""
#Functions
def escribir_preguntas ():
    """
    Escribe preguntas faltantes de usuarios en un archivo 'preguntas.TODO: FORMATO??
    TODO: parametros
    Sin return, solo escribe preguntas faltantes 
    """
    with open('preguntas.txt', 'w', encoding='UTF-8') as archivo:
        archivo.write()

def leer_preguntas_respuestas ():
    """
    Funcion que lee preguntas del archivo 'preguntas.txt'
    TODO: parametros
    retorna las preguntas del archivo 'preguntas.txt'
    """
    preguntas_respuestas = []
    with open('preguntas.txt', 'r', encoding='UTF-8') as archivo:

        for line in archivo: # Lee linea por linea el archivo
            
            # Limpia cada linea y las separa entre preguntas y respuestas
            tupla = tuple(line.strip().replace('\n','').split(':')) 
            preguntas_respuestas.append(tupla)


    return preguntas_respuestas




# Seleccion de lenguaje
language = print("Select a language")
print("1- Español")
print("2- Ingles")
print("3- Portugues")


# Validacion elección de lenguaje
while True:
    try:
        language = int(input("\nLanguage (1 - 2 - 3): "))
        if 1 <= language <= 3:
            break

        print("You must enter a valid language.")
        print("Please, select a valid option (1 - 2 - 3): ")

    except ValueError:
        print("Error: you must enter a number. Try again.")



if language == 1: #Español
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
    #TODO: Si vamos a hacer distintas preguntas segun la personalidad dejar "leer_preguntas"
    #      sino no repetir codigo "leer_preguntas"

    if personalidad == 1: #Amigable
        print("\nHola soy Nalaa! Temas para solucionar:\n") #TODO: Reemplazar el texto del print

        preguntas = leer_preguntas_respuestas()

        # Mostrar preguntas enumeradas al usuario
        #TODO: Si lo personalizamos en 3 personalidades = reutilizar el for y validacion -> function
        for i, pregunta in enumerate(preguntas):
            print(f"{i+1}- {pregunta[0]}")

        while True:
            try:
                opcion = int(input("¿Que necesitas resolver?(Indica el número de pregunta): "))
                if 0 < opcion < len(preguntas) + 1:
                    break

                print(f"Debes ingresar un número válido del 1 al {len(preguntas)} ")
            except ValueError:
                print("Error: debes ingresar un número.")

        respuesta = preguntas[opcion-1]
        print(f"\nLa respuesta a esa pregunta es: {respuesta[1]}")



    elif personalidad == 2: # Curioso
        print("Soy Luigi! ¿Para que quieres usar esta herramienta hoy?")
        leer_preguntas_respuestas()

    else: # Cariñoso
        print("Soy Otto! ¿Cómo estas?")
        leer_preguntas_respuestas()








elif language == 2: #Ingles
    print("TODO: bienvenido en ingles")

elif language == 3: #Portugues
    print("TODO: bienvenido en portugues")

else:
    print("Hubo un error en la seleccion de lenguajes.")
