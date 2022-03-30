from flask import Flask, render_template, url_for, request
import model
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Predict')
def predict():
    return render_template('input.html')

@app.route('/Reasult', methods = ["GET", "POST"])
def reasult():
    if request.method == "POST":
        v1 = request.form.get("var1")
        v2 = request.form.get("var2")
        v3 = request.form.get("var3")
        v4 = request.form.get("var4")
        v5 = request.form.get("var5")
        v6 = request.form.get("var6")
        
        input = np.array([v1, v2, v3, v4, v5, v6])
        value = input.astype(np.float_)
        print(value)
        pred = model.lr_model.predict([value])[0]

        # res = -2.482+(-0.060)*float(v1)+(0.11)*float(v2)+(3.851)*float(v3)+(5.214)*float(v4)+(-0.007)*float(v5)+(-0.561)*float(v6)
        # value = in_function.float_to_text(res)
        
    return render_template('reasult.html', output = f"Current House Price is : ${pred}")
if __name__ == '__main__':
    app.run(debug=True)