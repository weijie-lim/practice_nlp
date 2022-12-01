from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin
import ktrain
import json

app = Flask(__name__)
model = ktrain.load_predictor('distilbert')

@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        para = None
        if request.method == 'POST':
            para = request.form['data']
            predicted = model.predict(para)
            probabilities = model.predict(para, return_proba=True)
            probabilities = list(probabilities)
            
            result = {}
            result["response"] = "200"
            result["prediction"] = predicted
            cat = model.get_classes()
            #cat = ["waivers", "governing laws", "amendments", "counterparts", "warranties", "terminations", "valid issuances", "government regulations", "trade relations", "trading activities"]
            for i in range(len(probabilities)):
                result[cat[i]] = "{:.5f}".format(probabilities[i])
            
            return json.dumps(result)
    except:
        return('Error 500: Service is currently down. We are currently looking into it!', 400)


if __name__ == '__main__':
    app.run()
