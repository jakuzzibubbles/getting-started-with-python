# MBOX Email Filtering and Export to CSV

## Overview
This project focuses on extracting and filtering emails from an MBOX file, specifically searching for emails related to job applications (containing the word "Bewerbung" in the subject or body). After filtering, the relevant emails are exported to a CSV file, which can then be imported into Google Sheets or other tools for further analysis.

## Learning Journey

### Step 1: **Understanding the Problem**
The main task was to filter through a large MBOX file containing email data and extract specific emails that contain the word **"Bewerbung"** (job application) in the subject or body of the email. The final goal was to output this filtered list as a **CSV** file, which would then be easily accessible for analysis or record-keeping.

#### Initial Challenges:
1. **MBOX Format**: The MBOX file stores multiple emails in a single file with a complex structure that needed to be parsed correctly.
2. **Filtering and Parsing**: Extracting specific fields from the emails such as **sender**, **recipient**, **subject**, **date**, and **body** required proper handling of MIME encoding, multi-part messages, and different content types (plain text and HTML).
3. **Errors in the Script**: 
   - The first attempt led to **NoneType errors** when accessing the email body, due to incorrect handling of multi-part messages.
   - Field assignments for **sender**, **date**, and other attributes were incorrect or mixed up due to improper parsing logic.

### Step 2: **Solution Approach**
To tackle these challenges, a Python script was created using the `mailbox` library to read and parse the MBOX file. The key issues that needed to be addressed were:
- **MIME parsing** for multi-part messages.
- **Decoding email headers** and body content correctly.
- **Filtering** emails based on specific keywords (like "Bewerbung").
- **Exporting data to CSV** with proper formatting.

#### Key Code Changes:
- **Email Parsing**: 
  - Used the `mailbox.mbox` method to read the MBOX file.
  - **`email.header.decode_header`** was used to decode the subject and sender's email address correctly.
- **Body Extraction**: 
  - A custom function, `extract_text_from_email`, was implemented to extract text from both **plain text** and **HTML** content.
- **Filtering Logic**: 
  - Added a simple `if "Bewerbung" in body` condition to filter the emails.
- **Export to CSV**: 
  - Emails were filtered based on the subject and body, and the relevant fields (sender, recipient, subject, date, body) were written into a CSV file using Python's `csv` module.

#### Major Fixes:
- **Fixing `NoneType` Errors**: The `NoneType` error occurred because some emails didn't have a body or the body couldn't be accessed. A check was added to safely handle cases where the body was empty or unavailable.
- **Proper Field Assignment**: The fields like **sender**, **date**, and **subject** were properly assigned by carefully parsing the email headers. The correct encoding was ensured by decoding headers before using them.

### Step 3: **Refining the Process**
After the basic functionality was working (filtering and saving to CSV), additional improvements were needed:
1. **Handling Empty Rows in CSV**: After exporting the CSV, there were empty rows in the resulting data. We solved this by:
   - Using **Google Sheets**' filtering and sorting functionality to clean up the data by deleting empty rows.
2. **Ensuring Correct Formatting**: The CSV output wasn’t initially split into columns properly in Google Sheets. The solution was to use Google Sheets’ built-in CSV import tools, which automatically split the data into columns when imported correctly.

### Step 4: **Final Solution**
The final solution involved:
- Creating a Python script that reads an MBOX file, filters emails containing the word "Bewerbung", and extracts key fields such as **sender**, **subject**, **date**, and **body**.
- The filtered emails were written into a CSV file, which could be imported into **Google Sheets** or other tools for further processing.

### Step 5: **Learning Outcomes**
1. **MBOX File Parsing**: Understanding the structure of MBOX files and how to use Python’s `mailbox` library to parse them.
2. **Handling MIME Format**: Extracting both plain text and HTML content from multi-part MIME emails.
3. **Decoding Email Headers**: Using `email.header.decode_header` to handle encoded email headers correctly.
4. **Error Handling**: Handling edge cases like missing bodies or malformed emails to prevent crashes in the script.
5. **Google Sheets Integration**: Using Google Sheets' import functionality to properly handle CSV data and clean it up by removing empty rows.

