from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.form.get('data')
    processed_data = f"You sent: {data}"
    return processed_data

if __name__ == '__main__':
    app.run(debug=True)
