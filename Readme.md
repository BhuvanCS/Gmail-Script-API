# Gmail Email Processing Script

## Overview
This Python script allows you to process and store emails from Gmail using the Gmail API. It fetches emails based on specified rules (like marking them as read/unread), stores them in a database, and allows you to perform actions on them.

## Features
- Fetch emails from Gmail.
- Store email details in a SQLite database.
- Apply predefined rules to mark emails as read/unread.
- Supports Gmail OAuth 2.0 authentication.

## Prerequisites
1. **Python 3.x**
2. **Google API Client Library**
3. **OAuth 2.0 Credentials from Google Developer Console**

## Installation & Setup

1. Clone or download the repository.

2. Install required Python libraries:
    ```bash
    pip install --upgrade google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
    ```

3. Download **OAuth 2.0 credentials** from the Google Developer Console:
    - Go to [Google Cloud Console](https://console.cloud.google.com/).
    - Enable the Gmail API for your project.
    - Create OAuth 2.0 credentials (download `credentials.json`).

4. Place the `credentials.json` file in the project folder.

5. Run the script:
    ```bash
    python database.py #To Create the database
    python fetch_emails.py #To Fetch the emails from Inbox
    python set_rules.py #To Add own custom rules
    python process_emails.py #To perform the rule operation on the emails
    ```

6. Follow the authentication flow to authorize the script to access your Gmail account.

## How It Works
1. The script uses OAuth 2.0 to authenticate with Gmail.
2. It fetches emails and stores them in a SQLite database.
3. Rules are applied to emails, such as marking them as read/unread.
4. Actions such as labeling, moving, or modifying emails can be defined in the script.

