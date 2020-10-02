from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://img.buzzfeed.com/buzzfeed-static/static/2017-10/11/20/asset/buzzfeed-prod-fastlane-03/sub-buzz-16782-1507767085-2.jpg?crop=1600%3A1887%3B0%2C0&resize=720%3A720"
    ]

@app.route('/app2')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")