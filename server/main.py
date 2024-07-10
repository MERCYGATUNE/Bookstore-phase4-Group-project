from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/books", methods=['GET'])
def books():
    return jsonify (
        {
            "books":[
                'red riding',
                'snow white'
                
            ]
        }
    )
if__name__=="__main__":
    app.run(debug=True, port=8000)    