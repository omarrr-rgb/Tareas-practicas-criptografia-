import string

alfabeto = string.ascii_uppercase

rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# posiciones iniciales de rotores
pos1 = 0
pos2 = 0
pos3 = 0


def enigma(mensaje, clave):

    global pos1, pos2, pos3

    o1 = (alfabeto.index(clave[0]) + pos1) % 26
    o2 = (alfabeto.index(clave[1]) + pos2) % 26
    o3 = (alfabeto.index(clave[2]) + pos3) % 26

    resultado = ""

    for letra in mensaje.upper():

        if letra not in alfabeto:
            continue

        # Rotor I
        i = (alfabeto.index(letra) + o1) % 26
        letra = rotor1[i]

        # Rotor II
        i = (alfabeto.index(letra) + o2) % 26
        letra = rotor2[i]

        # Rotor III
        i = (alfabeto.index(letra) + o3) % 26
        letra = rotor3[i]

        # Reflector
        letra = reflector[alfabeto.index(letra)]

        # Rotor III inverso
        i = rotor3.index(letra)
        letra = alfabeto[(i - o3) % 26]

        # Rotor II inverso
        i = rotor2.index(letra)
        letra = alfabeto[(i - o2) % 26]

        # Rotor I inverso
        i = rotor1.index(letra)
        letra = alfabeto[(i - o1) % 26]

        resultado += letra

    return resultado


while True:

    print("\n=== MAQUINA ENIGMA ===")
    print("1. Cifrar")
    print("2. Descifrar")
    print("3. Configurar rotores")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        mensaje = input("Mensaje: ")
        clave = input("Clave (3 letras): ").upper()

        print("Resultado:", enigma(mensaje, clave))

    elif opcion == "2":

        mensaje = input("Mensaje cifrado: ")
        clave = input("Clave (3 letras): ").upper()

        print("Resultado:", enigma(mensaje, clave))

    elif opcion == "3":

        print("\nConfigurar posiciones iniciales de rotores (0-25)")
        pos1 = int(input("Posición rotor 1: "))
        pos2 = int(input("Posición rotor 2: "))
        pos3 = int(input("Posición rotor 3: "))

    elif opcion == "4":
        break