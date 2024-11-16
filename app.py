from flask import Flask, abort, request
import os

app = Flask(__name__)

@app.route("/")
def main():
    return "This is Boyuan @ UCI. Zot. Zot. Zot."

@app.route('/ics-h32/pset5/roads/<path:path>')
def roads_adventure(path):
    try:
        return file_processing("roads", path)
    except FileNotFoundError:
        abort(404)

@app.route('/ics-h32/pset5/start/<path:path>')
def start_is_the_end_adventure(path):
    try:
        return file_processing("start", path)
    except FileNotFoundError:
        abort(404)
        
@app.route('/ics-h32/pset5/edge/<path:path>')
def start_is_the_end_adventure(path):
    try:
        return file_processing("start", path)
    except FileNotFoundError:
        abort(404)

def file_processing(directory, path):
    with open(os.path.join(directory, path)) as f:
        data = f.read()
        if not request.headers.get("Accept"):
            return data
        else:
            return f"<pre>{data}</pre>"

if __name__ == "__main__":
    app.run()
