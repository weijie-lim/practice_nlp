from flask import Flask, request, jsonify, render_template
#from flask_cors import cross_origin
#import ktrain

app = Flask(__name__)
#model = ktrain.load_predictor('distilbert')


@app.route("/")
#@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
#@cross_origin()
def predict():
    pass


if __name__ == '__main__':
    app.run()
