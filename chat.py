from flask import Flask, render_template, request, session
import os

app = Flask(__name__)

#TODO: Configuración secreta para sesiones
app.config['SECRET_KEY'] = os.urandom(24)

mensajes = []

@app.route('/', methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        nuevo_mensaje = request.form.get('nuevo_mensaje')

        if nombre and nuevo_mensaje:
            mensaje_formateado = f"{nombre} : {nuevo_mensaje}"
            mensajes.append(mensaje_formateado)
            session['nombre'] = nombre

    return render_template('chat.html',mensajes = mensajes, nombre=session.get('nombre'))

if __name__ == '__main__':
    app.run(debug=True)