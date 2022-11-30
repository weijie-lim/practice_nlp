from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin
import sys
import ktrain

app = Flask(__name__)
#model = ktrain.load_predictor('distilbert')


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/prediction/", methods=["POST"])
@cross_origin()
def predict():
    para = None
    if request.method == "POST":
        para = request.json['data']
    #print('Hello world!', file=sys.stderr)
    # return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.1' , port=5000)
