from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "name": "Teoria",
        "url": "https://teoria.g1orga.dev",
        "tagline": "Theory & ideas",
        "description": "Explorations in concepts, frameworks, and the thinking behind the work.",
        "accent": "#7c6cff",
    },
    {
        "name": "Litera",
        "url": "https://litera.g1orga.dev",
        "tagline": "Writing & literature",
        "description": "Essays, notes, and literary projects — words given room to breathe.",
        "accent": "#ff8a65",
    },
    {
        "name": "ProofLab",
        "url": "https://prooflab.g1orga.dev",
        "tagline": "Experiments & proofs",
        "description": "A lab for prototypes, demos, and things worth trying before they ship.",
        "accent": "#4dd0a8",
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
