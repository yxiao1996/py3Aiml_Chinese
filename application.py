from flask import Flask, render_template, send_from_directory, request
from waitress import serve
import Kernel


app = Flask(__name__)
one_piece = Kernel.Kernel()
one_piece.learn("rules/one-piece.aiml")
one_piece.learn("rules/one-piece-food.aiml")
one_piece.learn("rules/one-piece-life-story.aiml")


@app.route('/', methods=['GET'])
def main():
    if "question" not in request.args.keys():
        question = "开始"
    else:
        question = request.args.get("question")
        if question == "":
            question = "开始"
    message = one_piece.respond(question)
    return render_template('index.html', one_piece_message=message)


@app.route('/js/<path:path>')
def static_js(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    print("Starting server")
    serve(app, host='0.0.0.0', port=80)