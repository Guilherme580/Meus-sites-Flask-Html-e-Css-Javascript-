import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    db_url = os.getenv("DATABASE_URL")
    return f"<p>conectado ao banco <span style='color: Blue;'>{db_url}</span></p>"

if __name__ == "__main__":
    app.run(debug=True)