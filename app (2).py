from flask import Flask, request, render_template_string
import openai

OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Jarvis (GPT)</title>
</head>
<body>
    <h2>Jarvis (GPT Assistant)</h2>
    <form method="post">
        <input type="text" name="prompt" style="width:400px;" autofocus>
        <input type="submit" value="Ask">
    </form>
    {% if response %}
        <p><b>Jarvis:</b> {{ response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        response = result['choices'][0]['message']['content']
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)