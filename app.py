from flask import Flask
from flask import request


app = Flask(__name__)
 

@app.route("/")
@app.route("/<nombre>")
def hola_mundo(nombre = "invitado"):
    return "Hola {}".format(nombre)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1 = 0, num2 = 0):
    return "{} mas {} es igual a {}".format(num1,num2,num1+num2)


if __name__ == "__main__":
    app.run(debug=True)
