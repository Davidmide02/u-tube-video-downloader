from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os


app = Flask(__name__)


def download(url):
    if url :
        try:
            yt = YouTube(url)
            title = yt.title
            stream = yt.streams.filter(only_video=True).first()
            stream.download(output_path='static')
            print('title',title)
            print(f'{title}.mp4')
            return send_file(f'{title}.mp4', mimetype='video/mp4', as_attachment=True )
        except Exception as e:
            return f'error message :{e}'
        
        
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method =='POST':
        url = request.form.get('url')
        
        if url :
            try:
                yt = YouTube(url)
                title = yt.title
                stream = yt.streams.filter(only_video=True).first()
                stream.download(output_path='static')
                return send_file(f'static/{title}.mp4', mimetype='video/mp4', as_attachment=True )
            except Exception as e:
                return f'Error message :{e}'

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)