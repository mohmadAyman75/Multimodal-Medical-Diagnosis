import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    with zipfile.ZipFile(path) as docx:
        tree = ET.XML(docx.read('word/document.xml'))
    text = []
    for node in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
        if node.text:
            text.append(node.text)
    return ''.join(text)

print(get_docx_text(r'c:\my\Projectes\DeepLearning\Multimodal_Medical_Diagnosis_System\README.docx'))
