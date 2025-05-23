from flask import Flask, request, jsonify
from cross_solver import solve_white_cross

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.get_json()
        scramble = data.get('scramble', '')
        solution = solve_white_cross(scramble)
        return jsonify({'solution': solution})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
