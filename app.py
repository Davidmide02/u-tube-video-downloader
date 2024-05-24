from flask import Flask, render_template, request, send_file, send_from_directory
from pytube import YouTube


app = Flask(__name__)


@app.route('/download/title')
def download(url):
    if url :
        try:
            yt = YouTube(url)
            title = yt.title
            stream = yt.streams.filter(only_video=True).first()
            stream.download(output_path='downloads')
            return f'{yt.title} {send_from_directory('downloads',title)} Downloaded successfully'
        except Exception as e:
            return f'error message :{e}'
        
        
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method =='POST':
        url = request.form.get('url')
        print(url)
        download(url)
        return f'loader here: {url}'
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
    
    # download progress indicator
    # send file to browser
    #  https://youtu.be/YERdEaEoy5E