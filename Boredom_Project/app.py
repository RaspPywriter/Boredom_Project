from flask import Flask, render_template

app = Flask(__name__)

#page to go home
@app.route('/')
def home():
    return render_template('home.html')

#page that goes to type
@app.route("/type")
def type():
  return render_template("type.html")

@app.route("/participants")
def participants():
    return render_template("participants.html")

@app.route("/random")
def random():
    return render_template("random.html")

if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)
