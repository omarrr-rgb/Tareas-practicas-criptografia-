## 🔹 Función `cifrar_vigenere(mensaje, clave)`

- Recorre cada letra del mensaje.
- Calcula el desplazamiento usando la letra correspondiente de la clave.
- Aplica la fórmula:

  C = (M + K) mod 26

- Solo cifra letras.
- Mantiene espacios y signos.
- Respeta mayúsculas y minúsculas.
- Repite la clave automáticamente cuando es necesario.

---

## 🔹 Función `descifrar_vigenere(mensaje, clave)`

Descifra el mensaje aplicando la fórmula:

  M = (C - K) mod 26

Conserva el formato original del texto.

---

## 🔹 Variable `j`

Controla la posición de la clave.  
Solo avanza cuando se procesa una letra, evitando que los espacios afecten el cifrado.

---

## 🔹 Función `menu()`

Permite al usuario:

1. Cifrar un mensaje  
2. Descifrar un mensaje  
3. Salir  

Solicita el mensaje y la clave, valida que la clave contenga solo letras y muestra el resultado.

---

## 🔹 Bloque principal

```python
if __name__ == "__main__":
    menu()