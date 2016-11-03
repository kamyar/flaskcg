from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, dunya!"

@app.route("/asdf", methods=["GET", "POST"])
def o_da_asdf_olsun():
    if request.method == "POST":
        print(request.form)
        if "byk" in request.form:
            print(request.form["byk"])
        else:
            print("by gelmedi")

        return "tamam aldik"
    else:
        print(request.args)
        if "byk" in request.args:
            byk = request.args["byk"]
        else:
            byk = "YOK"

        return "hosgeldin abi " + byk

app.run(debug=True)
