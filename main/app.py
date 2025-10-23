from flask import Flask, jsonify, request, render_template

# Compatibility shim: some werkzeug packages (newer/packaging) may not expose
# __version__ which Flask's test client expects. If it's missing, try to
# populate it from importlib.metadata or fall back to a sensible default.
try:
    import werkzeug
    if not hasattr(werkzeug, "__version__"):
        try:
            # Python 3.8+
            from importlib.metadata import version as _get_version
        except Exception:
            try:
                # pkg_resources as a fallback if importlib.metadata isn't available
                from pkg_resources import get_distribution as _get_version
            except Exception:
                _get_version = None
        try:
            if _get_version:
                werkzeug.__version__ = _get_version("werkzeug")
            else:
                werkzeug.__version__ = "unknown"
        except Exception:
            # Last-resort fallback
            werkzeug.__version__ = "0"
except Exception:
    # If importing werkzeug fails for some reason, ignore — Flask will raise a
    # helpful error later when actually used.
    pass

app = Flask(__name__)

@app.route('/')
def home():
    # Render the HTML template
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    payload = request.get_json(silent=True)
    return jsonify({"received": payload}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)