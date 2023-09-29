import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def extract_entities_from_text(text):
    # Process the text with SpaCy NLP model
    doc = nlp(text)

    # Extract entities
    entities = {}
    for entity in doc.ents:
        entities[entity.label_] = entities.get(entity.label_, []) + [entity.text]

    return entities

def main(resume_path):
    # Assuming you have a function to extract text from your resume
    resume_text = extract_text_from_resume(resume_path)
    
    # Extract entities using SpaCy
    extracted_entities = extract_entities_from_text(resume_text)
    
    for entity_type, entity_values in extracted_entities.items():
        print(f"{entity_type}: {', '.join(entity_values)}")

if __name__ == '__main__':
    resume_path = 'path_to_your_resume.pdf'  # Replace with the path to your resume
    main(resume_path)
