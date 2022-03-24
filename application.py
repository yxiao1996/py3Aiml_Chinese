from flask import Flask, render_template, send_from_directory, request
from waitress import serve
import Kernel


app = Flask(__name__)
one_piece = Kernel.Kernel()
one_piece.learn("rules/one-piece.aiml")


@app.route('/', methods=['GET'])
def main():
    if "question" not in request.args.keys():
        message = "喵喵"
    else:
        question = request.args.get("question")
        message = one_piece.respond(question)
    return render_template('index.html', one_piece_message=message)


@app.route('/js/<path:path>')
def static_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    print("Starting server")
    serve(app, host='0.0.0.0', port=80)