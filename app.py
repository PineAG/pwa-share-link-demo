from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def _index():
    return send_from_directory('view', 'index.html')

@app.route('/manifest.json', methods=['GET'])
def _manifest():
    return send_from_directory('view', 'manifest.json', mimetype='application/manifest+json')

@app.route('/icon.png', methods=['GET'])
def _icon():
    return send_from_directory('view', 'icon.png', mimetype='image/png')

@app.route('/pwa/sw.js', methods=['GET'])
def _service_worker():
    return send_from_directory('view', 'sw.js')

@app.route('/pwa/index.html', methods=['GET'])
def _pwa_index():
    return send_from_directory('view', 'index.html')

@app.route('/pwa/share', methods=['POST'])
def _share():
    url = request.form['url']
    print(url)
    return send_from_directory('view', 'share.html')

if __name__ == '__main__':
    app.run(port=8000)