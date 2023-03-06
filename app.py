from flask import Flask


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return "starting machine learning project"

if __name__=="__main__":
    app.run(debug=True)
   # app.run(host="0.0.0.0", port=8010)