from flask import Flask
from dotenv import load_dotenv
load_dotenv()


from config import Config
from models import db
from api import bp




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Cria as tabelas no arquivo db.sqlite3

    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
