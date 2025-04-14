from flask import Flask
from api import bp  # Importa apenas as rotas definidas

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
