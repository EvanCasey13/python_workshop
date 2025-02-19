from flask import Flask, render_template

# Create and configure the app
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')  # No need for './'

@app.route('/python-syntax')
def python_syntax():
    return render_template('syntax.html')

@app.route('/python-setup')
def python_setup():
    return render_template('python-setup.html')

@app.route('/advanced-topics')
def python_advanced_topics():
    return render_template('advanced-topics.html')

@app.route('/python-api')
def python_api():
    return render_template('python-api.html')

if __name__ == "__main__":
    app.run(debug=True)  # To run the app with debugging enabled
