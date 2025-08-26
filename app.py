from flask import Flask, render_template, jsonify
import time 

app = Flask(__name__)

start_time = time.time()

@app.route("/time")
def get_time():
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    return jsonify({"minutes": minutes, "seconds": seconds})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
