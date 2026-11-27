from flask import Flask, render_template
app= Flask(__name__)

@app.route("/home")
def homepage():
    return "home"

@app.route("/eventi")
def eventi():
    return render_template("eventi.html")

@app.route("/musei")
def musei():
    return render_template("musei.html")

@app.route("/ristoranti")
def ristoranti():
    return render_template("ristoranti.html")

@app.route("/citta")
def selezione_citta():
    return render_template("selezione_citta.html")

@app.route("/paesi")
def selezione_paesi():
    return render_template("selezione_paesi.html")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)