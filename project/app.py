from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/materiald')
def helloMaterial():
    return render_template('hello_material.html')

@app.route("/tables")
def show_tables():
    data = pd.read_excel('C:\\Users\\oulloa\\Documents\\code\\python\\flask_pandas\\project\\dummydata.xlsx')
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    females = data.loc[data.Gender=='f']
    males = data.loc[data.Gender=='m']
    return render_template('pandas.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
    titles = ['na', 'Female surfers', 'Male surfers'])


if __name__ == '__main__':
    app.run(debug=True)
