from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

@app.route("/")
def main():
    return "This is Boyuan @ UCI. Zot. Zot. Zot."

@app.route('/ics-h32/pset5/roads/<path:path>')
def roads_adventure(path):
    with open(os.path.join("roads", path)) as f:
        data = f.read()

        if not request.headers.get("Accept"):
            return data
        else:
            return f"<pre>{data}</pre>"
    return send_from_directory('roads', path)


if __name__ == "__main__":
    app.run()
