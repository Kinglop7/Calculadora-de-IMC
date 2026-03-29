from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""
    mensaje = ""

    if request.method == "POST":
        nombre = request.form["nombre"]
        peso = float(request.form["peso"])
        altura = float(request.form["altura"]) / 100

        imc = peso / (altura * altura)

        if imc < 18.5:
            mensaje = "Tu peso es bajo"
        elif imc < 25:
            mensaje = "Tu peso es normal"
        elif imc < 30:
            mensaje = "Tienes sobrepeso"
        else:
            mensaje = "Tienes obesidad"

        resultado = f"{nombre}, tu IMC es {imc:.2f}"

    return render_template("index.html", resultado=resultado, mensaje=mensaje)

app.run(host="0.0.0.0" , port=10000)
