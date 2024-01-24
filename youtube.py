from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        try:
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            stream.download()

            mensaje = f"¡Descarga Completa! Video guardado como {video.title}.mp4"
            return render_template('youtube.html',mensaje = mensaje)

        except Exception as e:
            mensaje = f"Error: {e}"
            return render_template('youtube.html',mensaje = mensaje)

    return render_template('youtube.html')

if __name__ == '__main__':
    app.run(debug=True)