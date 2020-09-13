# Boilerplate code to serve a web app

from flask import Flask, request, jsonify
from src.inference import get_prediction, initialize, LemmaTokenizer

app = Flask(__name__)


@app.route('/')
def status():
    # Health check endpoint
    return 'Ok'


@app.route('/train')
def train():
    # Implement method to train
    return 'Training...'


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Implement method to train
#         return 'Predicting...'
        orig_texts, real, fake, undecided, histo = get_prediction("is this real?", 50, initialize())
        return jsonify({'orig_texts': orig_texts[0], 'real': str(round(real, 2)),
                       'fake': str(round(fake, 2)), 'undecided': str(undecided),
                       'histo': str(histo)})



if __name__ == "__main__":
    app.run(debug=True, port=8000)
    # Use gunicorn for serving in production
