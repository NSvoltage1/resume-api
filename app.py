from flask import Flask, request, jsonify
import PyPDF2
# Import functions from your flask_resume_parser script
from flask_resume_parser import extract_text_from_pdf, parse_resume

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Naman's Resume Parser API!", 200

@app.route('/parse_resume', methods=['POST'])
def parse_resume_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        # Adjust the extract_text_from_pdf function to work with file content rather than a file path
        resume_text = extract_text_from_pdf(file)
        parsed_resume = parse_resume(resume_text)
        return jsonify(parsed_resume)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
