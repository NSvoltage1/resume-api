import PyPDF2

def extract_text_from_pdf(pdf_content):
    reader = PyPDF2.PdfReader(pdf_content)
    text = ''
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text


def parse_resume(resume_text):
    # Split resume into sections
    sections = ["PERSONAL INFORMATION", "EXPERIENCE", "EDUCATION", "LEADERSHIP  EXPERIENCE  AND  ACTIVITIES", "HONORS AND AWARDS", "ADDITIONAL  INFORMATION"]
    parsed_sections = {}

    # Using start as Personal Info by default
    start = "PERSONAL INFORMATION"
    for section in sections[1:]:
        if section in resume_text:
            part, resume_text = resume_text.split(section, 1)
            parsed_sections[start] = part.strip()
            start = section
        else:
            # Try splitting by a normalized version of the section header
            normalized_section = ' '.join(section.split())
            if normalized_section in resume_text:
                part, resume_text = resume_text.split(normalized_section, 1)
                parsed_sections[start] = part.strip()
                start = section
            else:
                print(f"WARNING: '{section}' not found in the resume.")

    parsed_sections[start] = resume_text.strip()

    return parsed_sections


def main():
    pdf_file_path = "C:\\Users\\nammi\\Resume\\Naman Sharma - Resume.pdf"
    resume_text = extract_text_from_pdf(pdf_file_path)
    parsed_resume = parse_resume(resume_text)

    # Display parsed sections
    for section, content in parsed_resume.items():
        print(f"\n--- {section} ---\n")
        print(content)

if __name__ == "__main__":
    main()