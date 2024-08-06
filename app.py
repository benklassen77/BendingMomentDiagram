import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    try:
        P = float(request.form['P'])
        l = float(request.form['l'])
        x = np.linspace(0, 1, int(request.form['x_points']))

        # Calculate M and V
        M = P * x**2 / l
        V = P * x / l

        # Create a plot
        plt.figure()
        plt.plot(x, M, label='M = P * x^2 / l')
        plt.plot(x, V, label='V = P * x / l')
        plt.legend()
        
        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        return send_file(img, mimetype='image/png')

    except ValueError:
        return "Invalid input. Please enter numeric values for P, l, and x_points.", 400

if __name__ == '__main__':
    app.run(debug=True)
