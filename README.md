# Auto Typer from Clipboard

## Descripción

Esta es una sencilla aplicación de escritorio para Windows que escribe automáticamente el texto que se encuentra en el portapapeles. Al activarse mediante una combinación de teclas, inicia una cuenta atrás y luego simula la escritura del texto, caracter por caracter, en la ventana que esté activa.

## Características

- **Activación por Tecla Rápida:** Se activa presionando `Ctrl+Alt+V`.
- **Cuenta Atrás:** Muestra una cuenta atrás de 3 segundos en la consola antes de empezar a escribir, dándote tiempo a cambiar a la ventana deseada.
- **Escritura Simulada:** Escribe el texto del portapapeles con una pequeña pausa entre cada caracter para un efecto más natural.
- **Personalizable:** Puedes cambiar fácilmente la combinación de teclas, la duración de la cuenta atrás y la velocidad de escritura modificando el archivo `app.py`.
- **Salida Segura:** Puedes detener el script en cualquier momento presionando la tecla `Esc`.

## Requisitos

Para ejecutar el script de Python directamente, necesitarás:

- Python 3
- Las siguientes librerías de Python:
  - `keyboard`
  - `pyperclip`

Puedes instalarlas con el siguiente comando:
```bash
pip install -r requirements.txt
```

## ¿Cómo usar el script?

1.  Clona o descarga este repositorio.
2.  Abre una terminal en la carpeta del proyecto.
3.  Instala las dependencias: `pip install -r requirements.txt`.
4.  Ejecuta el script: `python app.py`.
5.  Copia cualquier texto a tu portapapeles.
6.  Cambia a la aplicación donde quieres escribir (un editor de texto, un navegador, etc.).
7.  Presiona `Ctrl+Alt+V`.

## ¿Cómo crear el archivo `.exe`?

Si quieres compilar el programa en un archivo ejecutable (`.exe`) para usarlo sin necesidad de tener Python instalado, sigue estos pasos:

1.  Asegúrate de tener `pyinstaller` instalado:
    ```bash
    pip install pyinstaller
    ```
2.  (Opcional) Si quieres añadir un icono personalizado, asegúrate de que el archivo `.ico` (por ejemplo, `icono.ico`) esté en la misma carpeta que `app.py`.
3.  Ejecuta el siguiente comando en la terminal:
    ```bash
    pyinstaller --onefile --icon=icono.ico app.py
    ```
4.  El archivo `app.exe` final se encontrará en la carpeta `dist`.
