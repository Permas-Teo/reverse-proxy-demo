from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://img.buzzfeed.com/buzzfeed-static/static/2019-12/4/19/tmp/b0aa9a66093a/tmp-name-2-310-1575488871-7_dblbig.jpg?output-format=jpg&output-quality=auto"
    ]

@app.route('/app1')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")