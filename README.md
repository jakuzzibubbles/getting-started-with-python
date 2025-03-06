## Project Overview

My goal was to filter and extract specific emails from my inbox, particularly those containing a keyword, such as "bewerbung" (application), from a large set of emails stored in an MBOX file.

### Problem
I had a collection of emails in the MBOX format, and I needed to filter out emails that contained a particular keyword in either the subject or the body of the email. The goal was to extract these emails and store them in a structured format, such as CSV, for further analysis and reference.

### Solution
I used Python to create a script that processes the MBOX file and extracts the relevant emails. The key steps involved were:

1. **Extracting Emails from MBOX File**: Using the `mailbox` module, the script reads the MBOX file and iterates through each email message.
   
2. **Filtering Emails by Keyword**: The script checks if the keyword ("bewerbung") is present in either the subject or the body of the email. This way, only relevant emails are selected.

3. **Extracting Important Information**: The script extracts essential details from each email, such as the date, sender, recipient, subject, and message body.

4. **Saving Data to CSV**: After filtering and extracting the necessary data, the script writes the relevant information into a CSV file for easy access and analysis.

### Outcome
The filtering process was successfully completed, and a CSV file containing only the relevant emails was generated. This allowed me to isolate and review the specific emails that matched the criteria, enabling a more efficient way to manage and process my inbox.
