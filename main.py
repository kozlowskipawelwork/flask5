from waitress import serve
from view import app


if __name__ == '__main__':
    serve(app, host=("localhost"), port=8080,threads=20)