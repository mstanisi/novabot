from flask import Flask, request, jsonify, render_template_string
from collections import defaultdict
import random
import re

app = Flask(__name__)

# --- Build Markov chain on startup ---
valid_words = set(line.strip().lower() for line in open("hoard.txt"))

transitions = defaultdict(list)
with open("naked_lunch.txt", "r") as f:
    text = f.read().lower()
    words = re.findall(r"\w+", text)
    for i in range(len(words) - 1):
        if words[i] in valid_words and words[i+1] in valid_words:
            transitions[words[i]].append(words[i+1])

def generate_text(start_word, length=50):
    current = start_word.lower()
    if current not in transitions:
        return None
    output = [current]
    for _ in range(length - 1):
        next_words = transitions.get(current, [])
        if not next_words:
            next_words = list(valid_words)
        current = random.choice(next_words)
        output.append(current)
    return " ".join(output)

# --- HTML template ---
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nova Bot</title>
  <style>
    body { font-family: Georgia, serif; max-width: 700px; margin: 60px auto; padding: 0 20px; background: #f9f6f1; color: #222; }
    h1 { font-size: 2rem; margin-bottom: 4px; }
    p.sub { color: #666; margin-bottom: 32px; font-style: italic; }
    input[type="text"] { padding: 10px 14px; font-size: 1rem; border: 1px solid #ccc; border-radius: 4px; width: 260px; }
    button { padding: 10px 20px; font-size: 1rem; background: #222; color: #fff; border: none; border-radius: 4px; cursor: pointer; margin-left: 8px; }
    button:hover { background: #444; }
    #output { margin-top: 36px; line-height: 1.8; font-size: 1.1rem; min-height: 60px; }
    #error { color: #c0392b; margin-top: 16px; }
  </style>
</head>
<body>
  <h1>Nova Bot</h1>
  <p class="sub">Markov chain text generator seeded from <em>Naked Lunch</em></p>
  <input type="text" id="startWord" placeholder="Enter a start word..." />
  <button onclick="generate()">Generate</button>
  <div id="error"></div>
  <div id="output"></div>

  <script>
    async function generate() {
      const word = document.getElementById("startWord").value.trim();
      document.getElementById("error").textContent = "";
      document.getElementById("output").textContent = "";
      if (!word) { document.getElementById("error").textContent = "Please enter a start word."; return; }

      const res = await fetch(`/generate?start=${encodeURIComponent(word)}`);
      const data = await res.json();
      if (data.error) {
        document.getElementById("error").textContent = data.error;
      } else {
        document.getElementById("output").textContent = data.text;
      }
    }

    document.getElementById("startWord").addEventListener("keydown", e => {
      if (e.key === "Enter") generate();
    });

    async function loadRandomWord() {
      const res = await fetch("/random");
      const data = await res.json();
      document.getElementById("startWord").value = data.word;
    }

    loadRandomWord();
  </script>
</body>
</html>
"""

# --- Routes ---
@app.route("/random")
def random_word():
    word = random.choice(list(transitions.keys()))
    return jsonify({"word": word})

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/generate")
def generate():
    start = request.args.get("start", "").strip().lower()
    if not start:
        return jsonify({"error": "Please provide a start word."})
    result = generate_text(start)
    if result is None:
        return jsonify({"error": f"'{start}' wasn't found in the text. Try a different word."})
    return jsonify({"text": result})

if __name__ == "__main__":
    app.run(debug=True)