import joblib
from flask import Flask, render_template, request
from process import preparation, generate_response

# Download nltk
preparation()

# Start Chatbot
app = Flask(__name__)


# Load the model and other necessary files
chat_model = joblib.load('model/chat_model.h5')
classes = joblib.load('model/classess.pkl')
label_encoder = joblib.load('model/le.pkl')
tokenizers = joblib.load('model/tokenizers.pkl')
words = joblib.load('model/words.pkl')


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
    try:
        user_input = str(request.args.get('msg'))
        # Add input validation and sanitization if needed
        result = generate_response(user_input)
        return result
    except Exception as e:
        # Return an error message with status code 400 for bad request
        return str(e), 400


if __name__ == "__main__":
    app.run(debug=False)  # Set debug=False when deploying the app publicly
