from flask import Flask, render_template, request, jsonify
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from pathlib import Path
import shutil
import os

app = Flask(__name__)

# Define the target directory for unzipping the model
target_dir = Path("trained_model")

# Create the target directory if it doesn't exist
if not target_dir.exists():
    target_dir.mkdir(parents=True, exist_ok=True)

# Path to the ZIP file (not needed if already unzipped)
zip_file_path = Path("transformer.zip")

# Check if the model directory exists and is valid
if target_dir.is_dir() and any(target_dir.iterdir()):
    print(f"Model directory {target_dir} exists and is valid.")
else:
    print(f"Model directory {target_dir} does not exist or is empty.")

# Load the fine-tuned T5 model and tokenizer from the target directory
try:
    print(f"Loading tokenizer from: {str(target_dir)}")
    tokenizer = T5Tokenizer.from_pretrained(str(target_dir))
    print(f"Loading model from: {str(target_dir)}")
    model = T5ForConditionalGeneration.from_pretrained(str(target_dir))
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading model/tokenizer: {e}")
    model = None  # Ensure model is defined even if loading fails

# Set the device if model loaded successfully
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if model is not None:
    model.to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    input_text = data['input_text']

    # Check if model is loaded before proceeding
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    # Tokenize the input and move it to the same device as the model
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    
    # Generate the output
    output_ids = model.generate(inputs['input_ids'], max_length=150)
    
    # Decode and return the output
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if no port is set
    app.run(host="0.0.0.0", port=port, debug=True)
