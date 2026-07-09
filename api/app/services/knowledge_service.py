from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

KNOWLEDGE_FILE = BASE_DIR / "knowledge" / "company.txt"


def get_company_context():

    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return file.read()