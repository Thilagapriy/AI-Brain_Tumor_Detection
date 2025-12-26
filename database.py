import sqlite3
from datetime import datetime

def get_db_connection():
    return sqlite3.connect('history.db')

# Create table if not exists (call once)
with get_db_connection() as conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS history
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     patient TEXT,
                     date TEXT,
                     result TEXT)''')
    conn.commit()

def save_history(patient_name, result):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    with get_db_connection() as conn:
        conn.execute("INSERT INTO history (patient, date, result) VALUES (?, ?, ?)",
                     (patient_name, date, result))
        conn.commit()

def get_history():
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT patient, date, result FROM history ORDER BY date DESC")
        return cursor.fetchall()

# Simple chatbot
def chatbot(question):
    q = question.lower()
    if 'treatment' in q: return "Treatments vary by tumor type. Common options: surgery, radiation, chemotherapy."
    if 'survival' in q: return "Survival depends on tumor type, grade, and treatment. Consult a doctor."
    if 'symptoms' in q: return "Common symptoms: headaches, seizures, vision changes, nausea."
    return "I can answer questions about brain tumors (type, treatment, or symptoms)."