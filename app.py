from flask import Flask, render_template, request, redirect, url_for
from elmap import ElMap

app = Flask(__name__)

@app.route('/')
def index():
    elmap = ElMap()
    elmap.make_plot()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 