# Fine-Tuned T5 Summarization API
A Flask-based API for text summarization using a fine-tuned T5 model. 
The model is trained on the CNN/DailyMail dataset, optimized via knowledge distillation with Pegasus-Large, 
and further enhanced using custom techniques for cleaner and more concise summaries.

**Features**
State-of-the-art Summarization: Powered by T5, fine-tuned on CNN/DailyMail.
Knowledge Distillation: Leveraged Pegasus Large to improve model outputs.
Custom Enhancements:
Removes low-relevance lines based on TF-IDF scores.
Eliminates repeated lines for cleaner summaries.
Flask API: Simple REST API for generating summaries.

# Model Details
1. Base Model: T5 fine-tuned on CNN/DailyMail.
2. Optimization: Knowledge distillation using Pegasus Large.
3. Custom Enhancements:
    **TF-IDF-based line scoring to remove low-relevance sentences.**
    **Removal of duplicate lines for clarity.**

## File Structure
.
├── app.py                # Flask application code
├── requirements.txt      # Python dependencies
├── trained_model/        # Directory for the fine-tuned T5 model
│   ├── config.json
│   ├── pytorch_model.bin
│   └── tokenizer_config.json
├── transformer.zip       # (Optional) ZIP file of the model
├── templates/
│   └── index.html        # Frontend template (if needed)
└── static/               # (Optional) Static files for the frontend
│   └── style.css         
