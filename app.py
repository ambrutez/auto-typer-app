import pyperclip
import keyboard
import time

# --- Configuración ---
# La combinación de teclas que activará el proceso de escritura.
# Puedes cambiarla a tu combinación preferida.
# Ejemplos: 'ctrl+alt+p', 'f10', 'ctrl+shift+k'
HOTKEY = 'ctrl+alt+v'

# Pausa entre cada caracter escrito, en segundos.
DELAY_BETWEEN_CHARS = 0.3

# Tiempo de la cuenta atrás antes de empezar a escribir, in segundos.
COUNTDOWN_SECONDS = 3

def type_clipboard_content():
    """
    Obtiene texto del portapapeles, realiza una cuenta atrás y luego escribe el texto
    caracter por caracter.
    """
    try:
        # 1. Obtener contenido del portapapeles
        clipboard_content = pyperclip.paste()

        if not clipboard_content:
            print("El portapapeles está vacío. No hay nada que escribir.")
            return

        print(f"¡Contenido del portapapeles listo! Comenzando cuenta atrás de {COUNTDOWN_SECONDS} segundos...")
        print("Cambia a la ventana donde quieres que escriba.")

        # 2. Cuenta atrás
        for i in range(COUNTDOWN_SECONDS, 0, -1):
            print(f"{i}...")
            time.sleep(1)

        print("\n¡Escribiendo!")

        # 3. Escribir caracter por caracter
        for char in clipboard_content:
            keyboard.write(char)
            time.sleep(DELAY_BETWEEN_CHARS)

        print("\n¡Proceso completado!")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    """
    Función principal para configurar el atajo de teclado y esperar.
    """
    print(f"Programa iniciado. Presiona '{HOTKEY}' para empezar a escribir el contenido de tu portapapeles.")
    print("Presiona 'esc' para salir del programa.")

    # Configura el atajo de teclado. Cuando se presione, llamará a nuestra función.
    keyboard.add_hotkey(HOTKEY, type_clipboard_content)

    # Mantiene el script en ejecución para escuchar el atajo.
    # Esperará hasta que se presione la tecla 'esc'.
    keyboard.wait('esc')

    print("\nSaliendo del programa.")

if __name__ == "__main__":
    main()
