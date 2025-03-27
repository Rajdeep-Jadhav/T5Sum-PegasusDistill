# *Fine-Tuned T5 Summarization API*

## Project Overview 

A Flask-based API for text summarization using a fine-tuned T5 model. The model is trained on the **CNN/DailyMail** dataset, optimized via knowledge distillation with Pegasus Large, and further enhanced using custom techniques for cleaner and more concise summaries.

## Features

- **State-of-the-art Summarization**: Powered by T5, fine-tuned on CNN/DailyMail.
- **Knowledge Distillation**: Leveraged Pegasus Large to improve model outputs.
- **Custom Enhancements**:
  - Removes low-relevance lines based on TF-IDF scores.
  - Eliminates repeated lines for cleaner summaries.
- **Flask API**: Simple REST API for generating summaries.

<div align="center">
  <img src="https://github.com/user-attachments/assets/494e6f68-0acd-4ca8-9efd-b3ac2663441c" alt="Project Image" width="750"/>
</div>

Article: [The renewable energy sector continues to expand rapidly as governments and private companies invest in green technology to combat climate change. 
Solar power has seen a significant breakthrough with the development of perovskite solar cells, which promise higher efficiency at a lower cost. 
Meanwhile, wind energy projects are setting records with the installation of offshore wind turbines capable of producing several megawatts of electricity. 
Additionally, researchers are focusing on energy storage solutions, like advanced lithium-ion and solid-state batteries, to address the intermittency of renewable power sources. 
While challenges remain in infrastructure and adoption, experts are optimistic that renewable energy could account for a majority of global energy consumption by 2050.] 

Summary: [*Renewable energy could account for a majority of global energy consumption by 2050. The development of perovskite solar cells has seen a significant breakthrough. 
The renewable energy sector continues to expand rapidly*] 

## Achivement
- Successfully trained a T5-Small model on the CNN/Daily Mail dataset using knowledge distillation from Pegasus-Large.
- The model generates high-quality summaries, effectively captures key aspects and retain important information from the text.
- All this while being resource-efficient and using a fraction of the resources compared to larger models.
  
---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fine-tuned-t5-summarization-api.git
cd fine-tuned-t5-summarization-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the Fine-Tuned Model

- Unzip your fine-tuned model into the `trained_model/` directory.  
  If you have the model as a `.zip` file:
  ```bash
  unzip transformer.zip -d trained_model/
  ```

### 4. Run the Flask App

```bash
python app.py
```

The app will be available at `http://localhost:5000`.

---

## API Usage

### 1. Endpoint: `/generate`  
**Method**: `POST`  
**Content-Type**: `application/json`  

---

## File Structure

```plaintext
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
```

---

## Model Details

- **Base Model**: T5 fine-tuned on CNN/DailyMail.
- **Optimization**: Knowledge distillation using Pegasus Large.
- **Custom Enhancements**:
  - TF-IDF-based line scoring to remove low-relevance sentences.
  - Removal of duplicate lines for clarity.

---

## Notes

- Ensure that the `trained_model/` directory contains the fine-tuned model files.
- The API runs on port `5000` by default. You can change the port using the `PORT` environment variable:
  ```bash
  export PORT=8080
  python app.py
  ```

---
