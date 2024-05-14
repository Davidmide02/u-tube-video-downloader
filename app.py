from flask import Flask, render_template, request
from pytube import YouTube


app = Flask(__name__)

def download(url):
    if url :
        try:
            yt = YouTube(url)
            return f'{yt.title} Downloaded successfully'
        except Exception as e:
            return f'error message :{e}'
        
        
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method =='POST':
        url = request.form.get('url')
        print(url)
        vid = download(url)
        print(vid)
        return f'loader here: {url}'
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)