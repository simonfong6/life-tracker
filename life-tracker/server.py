from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Allow CORS (Cross Origin Requests)
CORS(app)


@app.route('/')
def index():
    return "Hello World!!!"


def main(args):
    app.run(
        host='0.0.0.0',
        port=args.port,
        threaded=False,
        debug=args.debug,
        ssl_context=args.ssl)


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--port',
        help="Port that the server will run on.",
        type=int,
        default=8008)
    parser.add_argument(
        '-d',
        '--debug',
        help="Whether or not to run in debug mode.",
        default=True,
        action='store_true')
    parser.add_argument(
        '-s',
        '--ssl',
        help="Whether or not to run with HTTPS",
        default=None,
        action='store_const',
        const='adhoc')

    args = parser.parse_args()
    main(args)
