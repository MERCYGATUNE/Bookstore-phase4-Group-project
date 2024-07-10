from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors= CORS(app,origins="*")

@app.route("/api/books", methods=['GET'])
def books():
    return jsonify (
        {
            "books":[
                '40 Laws of Power',
                'Snow white',
                'Cinderella',
                'Rapunzel',
                'Think Big',
                'Rich guy',
                'Poor guy',
                'The art of manipulation'
                
            ]
        }
    )
    

if __name__ == "__main__":
    app.run(debug=True, port=8000)    