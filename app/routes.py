from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/predict', methods=['POST'])
def predict():
    # Placeholder for prediction logic
    data = request.json
    prediction = 0  # Replace with model prediction
    return jsonify({'prediction': prediction})
