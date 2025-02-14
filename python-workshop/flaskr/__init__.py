import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def homepage():
        return render_template('./home.html')
    
    @app.route('/python-setup')
    def python_setup():
        return render_template('./python-setup.html')

    @app.route('/concepts')
    def python_concepts():
        return render_template('./python-concepts.html')
    
    @app.route('/advanced-topics')
    def python_advanced_topics():
        return render_template('./advanced-topics.html')
    
    @app.route('/python-api')
    def python_api():
        return render_template('./python-api.html')

    return app