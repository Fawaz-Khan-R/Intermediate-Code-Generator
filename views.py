# views.py

from flask import Flask, render_template, request, jsonify
from main import process_expression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    expression = request.form['expression']
    output_type = request.form.get('output_type', 'T_A_C')  # Default to 'T_A_C'
    try:
        output = process_expression(expression, output_type)
        return jsonify({'success': True, 'output': output})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
