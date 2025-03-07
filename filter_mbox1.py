import mailbox
import csv
import quopri
from email import message_from_string
from bs4 import BeautifulSoup  # To clean HTML content
import string

# Function to check if a string contains only ASCII characters
def is_ascii(text):
    return all(char in string.printable for char in text)

# Function to extract text from email (handles HTML and quoted-printable encoding)
def extract_text_from_email(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            payload = part.get_payload(decode=True)
            if payload:
                decoded_text = payload.decode(errors="ignore")  # Ignore decoding errors
                if content_type == "text/plain":
                    body = decoded_text  # Prefer plain text
                elif content_type == "text/html" and not body:
                    body = BeautifulSoup(decoded_text, "html.parser").get_text()  # Extract text from HTML
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors="ignore")  # Ignore decoding errors

    # Avoid processing non-ASCII characters
    if is_ascii(body):
        return quopri.decodestring(body).decode(errors="ignore")
    else:
        print("Skipping non-ASCII email body")
        return ""  # Skip this email if it contains non-ASCII characters

# Paths
mbox_file = "/Users/dieulinhnguyen/Downloads/gmx-mails/INBOX.partial.mbox/mbox"  # Change to actual file path
csv_file = "filtered_emails1.csv"
keyword = "Bewerbung".lower()  # Change to keyword of your choice

# Open MBOX file
mbox = mailbox.mbox(mbox_file)

# Write to CSV
with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "From", "To", "Subject", "Message"])

    for message in mbox:
        try:
            date = message["date"] or "Unknown"
            sender = message["from"] or "Unknown"
            recipient = message["to"] or "Unknown"
            subject = message["subject"] or "No Subject"
            body = extract_text_from_email(message)

            # Filter messages containing the keyword
            if keyword in subject.lower() or keyword in body.lower():
                writer.writerow([date, sender, recipient, subject, body])
        except Exception as e:
            print(f"Error processing email: {e}")

print(f"Filtering complete. Saved to {csv_file}")
