class Enigma:

    def __init__(self, alfabeto):
        self.alfabeto = alfabeto
        self.tamano = len(alfabeto)

        self.rotor1 = alfabeto
        self.rotor2 = alfabeto[::-1]
        self.rotor3 = alfabeto[1:] + alfabeto[0]
        self.reflector = alfabeto[::-1]

        self.notch1 = "Q"
        self.notch2 = "E"
        self.notch3 = "V"

        self.pos1 = 0
        self.pos2 = 0
        self.pos3 = 0

    def validar_config(self, cadena):
        if len(cadena) != self.tamano:
            return False
        return len(set(cadena)) == self.tamano

    def configurar(self, r1, r2, r3, reflector):
        if (self.validar_config(r1) and
            self.validar_config(r2) and
            self.validar_config(r3) and
            self.validar_config(reflector)):

            self.rotor1 = r1
            self.rotor2 = r2
            self.rotor3 = r3
            self.reflector = reflector
            print("Configuración aplicada correctamente.\n")
        else:
            print("Error: configuración inválida.\n")

    def avanzar_rotores(self):
        self.pos1 = (self.pos1 + 1) % self.tamano

        if self.alfabeto[self.pos1] == self.notch1:
            self.pos2 = (self.pos2 + 1) % self.tamano

            if self.alfabeto[self.pos2] == self.notch2:
                self.pos3 = (self.pos3 + 1) % self.tamano

    def procesar(self, mensaje, clave):

        if len(clave) < 4:
            print("La clave debe tener al menos 4 caracteres.")
            return ""

        self.pos1 = self.alfabeto.index(clave[0])
        self.pos2 = self.alfabeto.index(clave[1])
        self.pos3 = self.alfabeto.index(clave[2])

        resultado = ""

        for letra in mensaje:

            if letra not in self.alfabeto:
                resultado += letra
                continue

            self.avanzar_rotores()

            i = (self.alfabeto.index(letra) + self.pos1) % self.tamano
            l1 = self.rotor1[i]

            i = (self.alfabeto.index(l1) + self.pos2) % self.tamano
            l2 = self.rotor2[i]

            i = (self.alfabeto.index(l2) + self.pos3) % self.tamano
            l3 = self.rotor3[i]

            i = self.alfabeto.index(l3)
            l4 = self.reflector[i]

            i = (self.rotor3.index(l4) - self.pos3) % self.tamano
            l5 = self.alfabeto[i]

            i = (self.rotor2.index(l5) - self.pos2) % self.tamano
            l6 = self.alfabeto[i]

            i = (self.rotor1.index(l6) - self.pos1) % self.tamano
            letra_final = self.alfabeto[i]

            resultado += letra_final

        return resultado


def main():
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    maquina = Enigma(alfabeto)

    while True:
        print("=== MAQUINA ENIGMA ===")
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Configuración")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mensaje = input("Mensaje: ").upper()
            clave = input("Clave (mínimo 4 letras): ").upper()
            resultado = maquina.procesar(mensaje, clave)
            print("Resultado:", resultado, "\n")

        elif opcion == "2":
            mensaje = input("Mensaje cifrado: ").upper()
            clave = input("Clave (mínimo 4 letras): ").upper()
            resultado = maquina.procesar(mensaje, clave)
            print("Resultado:", resultado, "\n")

        elif opcion == "3":
            print("Introduce nuevas configuraciones")
            r1 = input("Rotor I: ").upper()
            r2 = input("Rotor II: ").upper()
            r3 = input("Rotor III: ").upper()
            ref = input("Reflector: ").upper()
            maquina.configurar(r1, r2, r3, ref)

        elif opcion == "4":
            break

        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    main()