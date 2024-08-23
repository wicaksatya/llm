from http.server import BaseHTTPRequestHandler, HTTPServer
from src.inference.chat_handler import reply
from config.config import PORT
import os
import threading

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/shutdown":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Shutting down...")
            threading.Thread(target=self.server.shutdown).start()
        elif self.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            index_file_path = os.path.join(os.path.dirname(__file__), 'static', 'index.html')
            with open(index_file_path, "rb") as file:
                self.wfile.write(file.read())
        elif self.path.startswith("/chat"):
            query = self.path.split("?", 1)[-1] if "?" in self.path else ""
            inquiry = query.split("=", 1)[-1] if "=" in query else ""
            print(f"    Human: {inquiry}")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            def stream(part):
                self.wfile.write(part.encode())

            context = {"inquiry": inquiry, "history": history, "stream": stream}
            result = reply(context)
            answer = result["answer"]
            self.wfile.write(answer.encode())
            print(f"Assistant: {answer}")
            history.append({"inquiry": inquiry, "answer": answer})
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == "__main__":
    history = []
    server = HTTPServer(("localhost", PORT), RequestHandler)
    print(f"Listening on port {PORT}")
    server.serve_forever()
