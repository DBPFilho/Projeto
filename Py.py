from flask import Flask, render_template, request

app = Flask(__name__)

def main():
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            primer_forward = request.form["primer_forward"]
            primer_reverse = request.form["primer_reverse"]
            quantidade_amostras = int(request.form["quantidade_amostras"])
            sequencias = [request.form[f"sequencia_amostra_{i}"] for i in range(1, quantidade_amostras + 1)]

            # Realize a análise da sequência aqui com base nas entradas do usuário
            resultados = []

            for sequencia in sequencias:
                resultado = analisar_sequencia(sequencia, primer_forward, primer_reverse)
                resultados.append(resultado)

            return render_template("index.html", resultados=resultados)

        return render_template("index.html")

    def analisar_sequencia(sequencia, primer_forward, primer_reverse):
        # Adicione a lógica de análise da sequência aqui
        # Retorne o resultado como uma string
        return "Resultado da análise para a sequência: " + sequencia

    if __name__ == "__main__":
        app.run(debug=True)

if __name__ == "__main__":
    main()
