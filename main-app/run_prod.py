if __name__ == '__main__':
    from waitress import serve
    from app import app

    serve(app, listen='*:8080')

