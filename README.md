Smart-Minute Agent

A cross-platform administrative assistant designed to parse meeting transcripts into structured data, including summaries, actionable tasks, and email drafts.
Overview

The Smart-Minute Agent leverages Google's Generative AI to automate meeting documentation. It processes unstructured meeting transcripts and converts them into structured formats using Pydantic schemas, ensuring consistent and professional output for team management.
Features

    Automated Summarization: Quickly generate concise summaries from long meeting transcripts.

    Task Extraction: Automatically identify and extract action items with assigned tasks.

    Email Drafting: Generate professional follow-up emails based on meeting discussions.

    Cross-Platform: Compatible with both Ubuntu and Windows environments.

Installation
Prerequisites

    Python 3.x

    Git installed on your machine

Setup Steps

    Clone the repository:
    Bash

    git clone https://github.com/sree07popzzz/smart-minute-agent.git
    cd smart-minute-agent


2. **Install dependencies:**
   ```bash
pip install google-genai streamlit pydantic python-dotenv

    Configure Environment Variables:
    Create a file named .env in the project root directory and add your Google API key:
    Plaintext

    GOOGLE_API_KEY=your_actual_api_key_here


## Usage
To launch the application, run the following command in your terminal:

```bash
streamlit run ap.py

Contributing

This project is managed via a centralized repository workflow. For team members:

    To update your local environment: Run git pull origin main.

    Feature Requests/Bug Fixes: Please discuss changes before implementing to maintain synchronization across platforms.
