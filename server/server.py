from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    area_type = request.form['area_type']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    if area_type == 'Super built-up Area':
        area_type = 3
    elif area_type == 'Built-up Area':
        area_type = 0
    elif area_type == 'Plot Area':
        area_type = 2
    else:
        area_type = 1

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, area_type, total_sqft, bath, balcony, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
