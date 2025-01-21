from flask import Flask, abort, request, send_file
import os

app = Flask(__name__)

@app.route("/")
def main():
    return "This is Boyuan @ UCI. Zot. Zot. Zot."

@app.route("/transcript/<path:path>")

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
def test_edge_cases(path):
    try:
        return file_processing("edge", path)
    except FileNotFoundError:
        abort(404)

@app.route('/plurality.zip')
def plurality_zip():
    return send_file(os.path.join("distributions", "plurality.zip"), as_attachment=True)


def file_processing(directory, path):
    with open(os.path.join(directory, path)) as f:
        data = f.read()
        if not request.headers.get("Accept"):
            return data
        else:
            return f"<pre>{data}</pre>"

if __name__ == "__main__":
    app.run()
