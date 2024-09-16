from flask import Flask, jsonify

app = Flask(__name__) 

@app.route('/')
def roll():
    
    return jsonify({"roll": 0})


if __name__ == '__main__':
    app.run(debug=True)
