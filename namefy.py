import re

def nameFile(text: str) -> str:

    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    text = text.strip('-') + '.py'
    return text

print(nameFile("Trapping Rain Water")) 
