import mailbox
import csv
from email import message_from_string

# function to extract text from the email (also handles HTML content)
def extract_text_from_email(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":  # xtract only plain text
                return part.get_payload(decode=True).decode(errors="ignore")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            return payload.decode(errors="ignore")
    return ""


mbox_file = "/path/to/folder/with/downloads"  # path to folder
csv_file = "gefilterte_emails.csv"  # Ziel-CSV-Datei

# keyowrd for filter
keyword = "bewerbung".lower()

# MBOX-Datei 
mbox = mailbox.mbox(mbox_file)

# CSV-Datei 
with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Datum", "Absender", "Empfänger", "Betreff", "Nachricht"])  # Spaltenüberschriften

  
    for message in mbox:
        date = message["date"] if message["date"] else "Unbekannt"
        sender = message["from"] if message["from"] else "Unbekannt"
        recipient = message["to"] if message["to"] else "Unbekannt"
        subject = message["subject"] if message["subject"] else "Kein Betreff"
        body = extract_text_from_email(message)

        # Prüfung auf das Keyword im Betreff oder Nachrichtentext
        if keyword in subject.lower() or keyword in body.lower():
            writer.writerow([date, sender, recipient, subject, body])

print(f"Filterung abgeschlossen. Gefilterte E-Mails gespeichert als: {csv_file}")
