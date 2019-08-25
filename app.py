from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as py
import pandas as pd
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        myf = request.files['file']
        fn = secure_filename(myf.filename)
        myf.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        df = pd.read_csv(fn)
        x = df['x']
        y = df['y']
        plot = go.Scatter(x=x, y=y)
        plot = [plot]
        plotJSON = json.dumps(plot, cls = plotly.utils.PlotlyJSONEncoder)
        return render_template('home2.html', x=plotJSON)



if __name__ == '__main__':
    app.run(
        debug = True)