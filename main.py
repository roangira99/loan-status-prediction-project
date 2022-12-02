# File that is run when we want to start our website
from website import create_app

app = create_app()


if __name__ == '__main__': # Only run the web server if you run this file directly
    app.run(debug=True)     