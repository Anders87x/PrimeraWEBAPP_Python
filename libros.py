from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
db = SQLAlchemy(app)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(50), nullable=False)

@app.route('/')
def mostrar_libros():
    libros = Libro.query.all()
    return render_template('libros.html', libros=libros)

@app.route('/agregar_libro', methods=['POST'])
def agregar_libro():
    nuevo_titulo = request.form['titulo']
    nuevo_autor = request.form['autor']

    nuevo_libro = Libro(titulo=nuevo_titulo,autor=nuevo_autor)
    db.session.add(nuevo_libro)
    db.session.commit()

    return redirect(url_for('mostrar_libros'))

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)