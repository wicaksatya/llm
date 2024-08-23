from flask import Flask, request, send_from_directory
from src.inference.chat_handler import reply
from config.config import PORT
import os

app = Flask(__name__)
history = []

@app.route('/')
@app.route('/index.html')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['GET'])
def chat():
    inquiry = request.args.get('inquiry', '')
    print(f"    Human: {inquiry}")

    # Check for duplicate inquiry
    if history and history[-1]['inquiry'] == inquiry:
        answer = "Your inquiry is the same as before, please change the inquiry."
    else:
        def stream(part):
            yield part

        context = {"inquiry": inquiry, "history": history, "stream": stream}
        answer = reply(context) 
        print(f"Assistant: {answer}")
        history.append({"inquiry": inquiry, "answer": answer})
    
    return answer

@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
