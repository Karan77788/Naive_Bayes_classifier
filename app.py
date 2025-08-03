from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('naive_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        user_review = request.form['review']
        prediction = model.predict([user_review])[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
