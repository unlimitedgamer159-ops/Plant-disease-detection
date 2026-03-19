"""
Model inference module.
Supports both .keras (full model) and .tflite (offline/mobile) formats.
"""
import numpy as np
import json
import os
from PIL import Image, ImageOps
import io

# ── Constants ──────────────────────────────────────────────────────────────────
IMG_SIZE = 224
TOP_K = 3          # Return top-3 predictions

# ── Model loader ───────────────────────────────────────────────────────────────
_model = None
_interpreter = None  # TFLite interpreter
_class_names = None
_use_tflite = False


def load_model(model_dir: str):
    """Load model and class names from a directory. Call once at startup."""
    global _model, _interpreter, _class_names, _use_tflite

    # Load class names
    class_names_path = os.path.join(model_dir, 'class_names.json')
    if not os.path.exists(class_names_path):
        raise FileNotFoundError(f"class_names.json not found in {model_dir}")
    with open(class_names_path) as f:
        _class_names = json.load(f)

    # Prefer TFLite (faster, offline-friendly)
    tflite_path = os.path.join(model_dir, 'plant_disease_model.tflite')
    keras_path = os.path.join(model_dir, 'best_model_final.keras')

    if os.path.exists(tflite_path):
        import tensorflow as tf
        _interpreter = tf.lite.Interpreter(model_path=tflite_path)
        _interpreter.allocate_tensors()
        _use_tflite = True
        print(f"Loaded TFLite model: {tflite_path}")
    elif os.path.exists(keras_path):
        import tensorflow as tf
        _model = tf.keras.models.load_model(keras_path)
        _use_tflite = False
        print(f"Loaded Keras model: {keras_path}")
    else:
        raise FileNotFoundError(
            f"No model found in {model_dir}.\n"
            "Expected: plant_disease_model.tflite OR best_model_final.keras"
        )

    print(f"Classes loaded: {len(_class_names)}")


# ── Image preprocessing ────────────────────────────────────────────────────────

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """
    Preprocess raw image bytes for inference.
    Handles: different sizes, RGBA, grayscale, EXIF rotation.
    Returns: float32 numpy array of shape (1, 224, 224, 3), values in [0, 1].
    """
    img = Image.open(io.BytesIO(image_bytes))
    
    # Handle EXIF rotation (very common in phone photos)
    img = ImageOps.exif_transpose(img)
    
    # Convert to RGB (handles RGBA, grayscale, palette mode)
    img = img.convert('RGB')
    
    # Resize with high-quality resampling
    img = img.resize((IMG_SIZE, IMG_SIZE), Image.LANCZOS)
    
    # Normalize to [0, 1]
    arr = np.array(img, dtype=np.float32) / 255.0
    
    # Add batch dimension
    return np.expand_dims(arr, axis=0)


# ── Inference ──────────────────────────────────────────────────────────────────

def predict(image_bytes: bytes) -> list[dict]:
    """
    Run inference on image bytes.
    
    Returns top-K predictions as list of dicts:
    [
        {
            "class_name": "Tomato___Late_blight",
            "confidence": 0.9234,
            "rank": 1
        },
        ...
    ]
    """
    if _class_names is None:
        raise RuntimeError("Model not loaded. Call load_model() first.")

    input_arr = preprocess_image(image_bytes)

    if _use_tflite:
        predictions = _predict_tflite(input_arr)
    else:
        predictions = _predict_keras(input_arr)

    # Get top-K indices
    top_k_indices = np.argsort(predictions[0])[::-1][:TOP_K]

    results = []
    for rank, idx in enumerate(top_k_indices, start=1):
        results.append({
            "class_name": _class_names[idx],
            "confidence": float(predictions[0][idx]),
            "rank": rank
        })

    return results


def _predict_keras(input_arr: np.ndarray) -> np.ndarray:
    return _model.predict(input_arr, verbose=0)


def _predict_tflite(input_arr: np.ndarray) -> np.ndarray:
    input_details = _interpreter.get_input_details()
    output_details = _interpreter.get_output_details()

    _interpreter.set_tensor(input_details[0]['index'], input_arr)
    _interpreter.invoke()

    return _interpreter.get_tensor(output_details[0]['index'])


# ── Health check ───────────────────────────────────────────────────────────────

def model_loaded() -> bool:
    return _class_names is not None


def get_num_classes() -> int:
    return len(_class_names) if _class_names else 0
