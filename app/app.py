"""
Plant Disease Detection — Flask Web App
Run locally or on Codespaces / Hugging Face Spaces
"""
import os
import sys
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Add parent dir to path so we can import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.inference import load_model, predict, model_loaded
from utils.disease_info import get_disease_info, SEVERITY_COLORS, SEVERITY_LABELS

app = Flask(__name__)

# ── Config ─────────────────────────────────────────────────────────────────────
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp', 'bmp'}
MODEL_DIR = os.environ.get('MODEL_DIR', os.path.join(os.path.dirname(__file__), '..', 'model'))

app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_MB * 1024 * 1024


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'model_loaded': model_loaded(),
    })


@app.route('/predict', methods=['POST'])
def predict_route():
    # ── Validate input ──────────────────────────────────────────────────────
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    lang = request.form.get('lang', 'en')  # 'en', 'hi', 'mr'

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Use: {", ".join(ALLOWED_EXTENSIONS)}'}), 400

    if not model_loaded():
        return jsonify({'error': 'Model not loaded. Place model files in the /model directory.'}), 503

    # ── Run inference ────────────────────────────────────────────────────────
    try:
        image_bytes = file.read()
        predictions = predict(image_bytes)
    except Exception as e:
        return jsonify({'error': f'Inference failed: {str(e)}'}), 500

    # ── Build response ───────────────────────────────────────────────────────
    top = predictions[0]
    disease_info = get_disease_info(top['class_name'])
    severity = disease_info.get('severity', 'unknown')

    # Localized disease name
    name_key = f'name_{lang}' if lang != 'en' else 'name'
    disease_name = disease_info.get(name_key, disease_info.get('name', top['class_name']))

    # Localized treatment
    treatment_key = f'treatment_{lang}' if lang != 'en' else 'treatment_en'
    treatment = disease_info.get(treatment_key, disease_info.get('treatment_en', 'No treatment info available.'))

    # Localized severity label
    severity_label = SEVERITY_LABELS.get(severity, SEVERITY_LABELS['unknown']).get(lang, '')

    response = {
        'success': True,
        'top_prediction': {
            'class_name': top['class_name'],
            'disease_name': disease_name,
            'confidence': round(top['confidence'] * 100, 1),
            'severity': severity,
            'severity_label': severity_label,
            'severity_color': SEVERITY_COLORS.get(severity, '#6b7280'),
            'treatment': treatment,
        },
        'alternatives': [
            {
                'class_name': p['class_name'],
                'disease_name': get_disease_info(p['class_name']).get(name_key, p['class_name']),
                'confidence': round(p['confidence'] * 100, 1),
            }
            for p in predictions[1:]  # 2nd and 3rd predictions
        ],
        'language': lang,
    }

    return jsonify(response)


# ── Error handlers ─────────────────────────────────────────────────────────────

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': f'File too large. Max size: {MAX_FILE_SIZE_MB}MB'}), 413


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server error. Check logs.'}), 500


# ── Startup ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print(f"\nLooking for model in: {os.path.abspath(MODEL_DIR)}")
    
    try:
        load_model(MODEL_DIR)
        print("Model loaded successfully!\n")
    except FileNotFoundError as e:
        print(f"\n⚠️  WARNING: {e}")
        print("App will start but /predict will return 503 until model files are added.\n")

    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'
    
    print(f"Starting app on http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
