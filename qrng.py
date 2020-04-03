import quantis
from flask import Flask, jsonify, render_template


rd = quantis.QUANTIS()

#rd.start()

#print(rd.read(1000))

#print(rd.get_bits(1000))
#rd.close()

print(rd.get_double())

print(rd.get_float())

app = Flask(__name__)

@app.route("/randfloat/<int:n>")
def randfloat(n):
    return jsonify(rd.get_float(n))

@app.route("/randdouble/<int:n>")
def randdouble(n):
    return jsonify(rd.get_double(n))
    
@app.route("/",methods=["GET","POST"])
def form():
    return """<H1>Quantum Random Number Generator API Quantis ID USB</H1>

    <H2><b>/randfloat/</b><i>numbers</i></H2>

    <H2><b>/randdouble/</b><i>numbers</i></H2>
    """



if __name__ == "__main__":
    app.run("0.0.0.0",8080)
