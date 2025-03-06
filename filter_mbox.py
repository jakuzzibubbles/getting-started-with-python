import mailbox
import csv
from email import message_from_string

# Funktion zum Extrahieren des Textes aus der E-Mail (behandelt auch HTML-Inhalte)
def extract_text_from_email(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":  # Nur Klartext extrahieren
                return part.get_payload(decode=True).decode(errors="ignore")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            return payload.decode(errors="ignore")
    return ""  # Falls keine Nutzlast oder Text gefunden wird

# Dateipfade (passen Sie den Pfad zur mbox-Datei an)
mbox_file = "/Users/dieulinhnguyen/Documents/INBOX.partial.mbox/mbox"  # Ersetzen Sie dies mit dem echten Pfad
csv_file = "gefilterte_emails.csv"  # Ziel-CSV-Datei

# Schlüsselwort für die Filterung
keyword = "bewerbung".lower()

# MBOX-Datei öffnen
mbox = mailbox.mbox(mbox_file)

# CSV-Datei erstellen und die Daten hineinschreiben
with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Datum", "Absender", "Empfänger", "Betreff", "Nachricht"])  # Spaltenüberschriften

    # Durch alle E-Mails im MBOX-Postfach iterieren
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
