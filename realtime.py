from flask import Flask, render_template
from flask_socketio import SocketIO

#TODO: Crear la aplicacion Flask
app = Flask(__name__)

#TODO: Configuracion de la clave secreta para sessiones
app.config['SECRET_KEY'] = 'tu_clave_secreta_segura'

#TODO: Inicializar SocketIO con la aplicacion de FLASK
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('realtime.html')

@socketio.on('mensaje')
def manejar_mensaje(data):
    #TODO: Obtener el nombre y el nuevo mensaje del diccionario 'data'
    nombre = data['nombre']
    nuevo_mensaje = data['mensaje']

    #TODO: Emitir un evento actualizar_mensajes a todos los clientes conectados
    socketio.emit('actualizar_mensajes',{'nombre':  nombre,'mensaje': nuevo_mensaje})

#TODO: Ejecutar la aplicación Flask con el servidor SocketIO en modo de depuración
if __name__ == '__main__':
    socketio.run(app, debug=True)