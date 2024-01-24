from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    contenido_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo con Flask</title>
    </head>
    <body>

        <h1>Hola Mundo desde Flask!</h1>

    </body>
    </html>"""

    return render_template_string(contenido_html)

if __name__ == '__main__':
    app.run(debug=True)