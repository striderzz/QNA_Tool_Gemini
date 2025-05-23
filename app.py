from google import genai
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

client = genai.Client(api_key="yourapikey")

@app.route('/', methods =["GET", "POST"])
def index():
    question = ""
    if request.method == "POST":
      
        question = request.form.get("question")

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=question
     )
    print(response.text)
    return render_template("index.html", answer = response)    

if __name__ == '__main__':
    app.run(debug=True)
