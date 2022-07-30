from flask import Flask
import requests, json 

app = Flask(__name__)
        
@app.route("/", methods=["GET"])
def message():
    resp = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    x = json.loads(resp.text)
    return x["joke"]

if __name__=='__main__':
    app.run(debug=True)
