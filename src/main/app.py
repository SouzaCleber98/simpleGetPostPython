from flask import Flask
from src.routes.route import routes
PORT = 5500

app = Flask(__name__)
app.register_blueprint(routes)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)



