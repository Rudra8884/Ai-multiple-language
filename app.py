from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

@app.route("/", methods=["GET", "POST"])
def home():
    translation = ""
    if request.method == "POST":
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]
        input_text = request.form["input_text"]

        prompt = f"Translate from {source_lang} to {target_lang}: {input_text}"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[{"role": "user", "content": prompt}]
            )
            translation = response['choices'][0]['message']['content']
        except Exception as e:
            translation = f"Error: {str(e)}"

    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)