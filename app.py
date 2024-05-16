from process import preparation, generate_response
from flask import Flask, render_template, request

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Main.html")

@app.route("/Artikel")
def artikel():
    return render_template("Artikel.html")

@app.route("/About")
def bio():
    return render_template("About.html")

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)