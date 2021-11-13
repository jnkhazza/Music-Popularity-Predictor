from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('app.pkl', 'rb'))
scaler = pickle.load(open('scale.pkl','rb'))

app = Flask(__name__)

genres = {
    'Acoustic/Folk':13,
    'Alternate':14, 
    'Blues':15, 
    'Bollywood':16, 
    'Country':17,
    'Hip-Hop':18, 
    'Indie':19, 
    'Instrumental':20, 
    'Metal':21,
    'Pop':22, 
    'Rock':23,
}

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    if data14 in genres:
        arr[0, genres[data14] ] = 1
    else:
        print("The genre doesnt exist")
    scale_array = scaler.transform(arr)
    pred = model.predict(scale_array)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)


