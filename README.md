### Problem 😵‍💫
I had a few large collection of emails in the MBOX format, and I needed to filter out emails that contained a particular keyword in either the subject or the body of the email. The goal was to extract these emails and store them in a structured format, such as CSV, for further analysis and reference.

### Solution
I used Python to create a script that processes the MBOX file, that i downloaded from my apple mail and extracts the relevant emails. Key steps:

1. **Extracting Emails from MBOX File**: Using the `mailbox` module, the script reads the MBOX file and iterates through each email message.
   
2. **Filtering Emails by Keyword**: The script checks if the keyword ("bewerbung") is present in either the subject or the body of the email. This way, only relevant emails are selected.

3. **Extracting Important Information**: The script extracts essential details from each email, such as the date, sender, recipient, subject, and message body.

4. **Saving Data to CSV**: After filtering and extracting the necessary data, the script writes the relevant information into a CSV file for easy access and analysis.

### Outcome 🤓
The filtering process was successfully completed, and a CSV file containing only the relevant emails was generated. This allowed me to isolate and review the specific emails that matched the criteria, enabling a more efficient way to manage and process my inbox.


### **Processing and Extracting Emails -> Learnings**  

#### **Extracting Email Content**   
- processed multipart emails by iterating through different content types.  
- used `BeautifulSoup` to extract text from HTML content, removing unnecessary formatting.  
- handled "quoted-printable" encoding with the `quopri` module to correctly decode email bodies.  

#### **Handling Encoding Issues**   
- a preprocessing step was added to ensure extracted text contained only printable ASCII characters.  
- error handling mechanisms were implemented to skip problematic emails instead of terminating the script.  

#### **Filtering Emails by Keyword**   
- converted both the subject and body to lowercase for case-insensitive matching.  
- checked if the keyword appeared in either field before extracting the email.  

#### **Storing Filtered Results**   
- extracted key fields: date, sender, recipient, subject, and body.  
- saved the filtered data into a CSV file for easy access and further analysis.  

#### **Troubleshooting and Optimization**   
- encoding errors were resolved by ensuring proper decoding of email content.  
- virtual environment issues and incorrect Python installations were addressed to enable smooth execution.  
- error handling was improved to ensure robustness, allowing the script to continue running even when encountering problematic emails.  
