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
    
@app.route("/randbits/<int:n>")
def randbits(n):
    rd.start()
    data = rd.get_bits(n)
    rd.close()
    return jsonify(data)

@app.route("/",methods=["GET","POST"])
def form():
    return "Quantum Random Number Generator API"



if __name__ == "__main__":
    app.run("0.0.0.0",8080)
