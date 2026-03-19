from flask import Flask, request, render_template
from analyser.preprocess import clean_text
from analyser.summarizer import summarize_legislation
from analyser.entities import extract_entities
from analyser.topics import topic_modeling
import nltk

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["legislation"]
        cleaned = clean_text(text)
        summary = summarize_legislation(text)
        entities = extract_entities(text)
        topics = topic_modeling([cleaned.split()])
        return render_template("index.html", summary=summary, entities=entities, topics=topics)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
