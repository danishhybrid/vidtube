from flask import Flask, request, redirect, render_template
import pytube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL from the user
        url = request.form.get('url')

        # Use pytube library to download the video
        yt = pytube.YouTube(url)
        video = yt.streams.first()
        video.download('/path/to/downloads/')

        return redirect('/receive')

    return render_template('index.html')

@app.route('/receive')
def receive():
    return render_template('receive.html')

if __name__ == '__main__':
    app.run(debug=True)