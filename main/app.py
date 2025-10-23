from flask import Flask, jsonify, request, render_template

app = Flask(_name_)

@app.route('/')
def home():
    # Render the HTML template
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    payload = request.get_json(silent=True)
    return jsonify({"received": payload}), 201

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)