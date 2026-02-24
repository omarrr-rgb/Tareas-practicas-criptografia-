def cifrar_vigenere(mensaje, clave):
    texto_cifrado = ""
    j = 0  # Índice para recorrer la clave

    for i in range(len(mensaje)):
        if mensaje[i].isalpha():
            desplazamiento = ord(clave[j % len(clave)].lower()) - ord('a')

            if mensaje[i].islower():
                valor = (ord(mensaje[i]) - ord('a') + desplazamiento) % 26
                texto_cifrado += chr(valor + ord('a'))
            else:
                valor = (ord(mensaje[i]) - ord('A') + desplazamiento) % 26
                texto_cifrado += chr(valor + ord('A'))

            j += 1
        else:
            texto_cifrado += mensaje[i]

    return texto_cifrado


def descifrar_vigenere(mensaje, clave):
    texto_descifrado = ""
    j = 0

    for i in range(len(mensaje)):
        if mensaje[i].isalpha():
            desplazamiento = ord(clave[j % len(clave)].lower()) - ord('a')

            if mensaje[i].islower():
                valor = (ord(mensaje[i]) - ord('a') - desplazamiento) % 26
                texto_descifrado += chr(valor + ord('a'))
            else:
                valor = (ord(mensaje[i]) - ord('A') - desplazamiento) % 26
                texto_descifrado += chr(valor + ord('A'))

            j += 1
        else:
            texto_descifrado += mensaje[i]

    return texto_descifrado


def menu():
    while True:
        print("\n==============================")
        print("     CIFRADO VIGENÈRE")
        print("==============================")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            mensaje = input("Ingresa el mensaje a cifrar: ")
            clave = input("Ingresa la clave: ")

            if clave.isalpha():
                resultado = cifrar_vigenere(mensaje, clave)
                print("\nMensaje cifrado:")
                print(resultado)
            else:
                print("Error: La clave solo debe contener letras.")

        elif opcion == "2":
            mensaje = input("Ingresa el mensaje a descifrar: ")
            clave = input("Ingresa la clave: ")

            if clave.isalpha():
                resultado = descifrar_vigenere(mensaje, clave)
                print("\nMensaje descifrado:")
                print(resultado)
            else:
                print("Error: La clave solo debe contener letras.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")



if __name__ == "__main__":
    menu()