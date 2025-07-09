# print("-----------------------------------------------------------------------------")
# user_text = input("                            Heyy!, what's your name? ")
# print("-----------------------------------------------------------------------------")
# print()

# greeting = "Nice to meet you " + user_text
# print(greeting)


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["username"]
        return redirect(url_for("greet", name=name))
    return render_template("index.html")

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

