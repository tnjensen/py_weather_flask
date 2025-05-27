from flask_frozen import Freezer
from main import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
    # This will generate static files in the 'build' directory
    # You can specify a different directory by passing the 'dest' argument to Freezer
    # freezer = Freezer(app, dest='static')
    # freezer.freeze()