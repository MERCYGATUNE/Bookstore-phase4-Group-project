from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors= CORS(app,origins="*")

@app.route("/api/books", methods=['GET'])
def books():
    return jsonify (
        {
            "books":[
                'red ridinghood',
                'snow white',
                'cinderella'
                
            ]
        }
    )
if __name__ == "__main__":
    app.run(debug=True, port=8000)    