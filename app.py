from flask import Flask, request, jsonify, render_template
from password_utils import check_password_strength

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'error': 'Password is required'}), 400

    is_strong, feedback = check_password_strength(password)

    response = {
        'is_strong': is_strong,
        'feedback': feedback
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
