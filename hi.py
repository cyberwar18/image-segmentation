from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activate_function', methods=['POST'])
def activate_function():
    # Perform the desired Python function here
    result = perform_python_function()

    return jsonify({'message': 'Python function activated successfully.'})

def perform_python_function():
    # Your Python logic here
    return "Python function executed."

if __name__ == '__main__':
    app.run(debug=True)
