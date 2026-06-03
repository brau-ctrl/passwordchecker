<img width="1888" height="939" alt="Screenshot 2026-06-03 134948" src="https://github.com/user-attachments/assets/58faf165-cd31-413b-807c-c3d98f9e996d" />
Password Strength Checker

A simple Flask web interface that connects to the existing password_strength_checker.py script to evaluate password strength and provide feedback.

## Overview

This project provides:
- A Python password strength analysis engine
- A Flask backend in app.py
- A styled webpage in index.html
- Static CSS in styles.css

The webpage sends a password to the backend API and displays:
- Strength label
- Entropy score
- Improvement suggestions

## Features

- Length and character diversity checks
- Common password blacklist detection
- Entropy-based strength scoring
- Modern responsive UI
- Real-time server-backed analysis

## Requirements

- Python 3.10+
- Flask

## Setup

1. Create or activate your virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Start the Flask app:

```bash
python app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

## File Structure

- password_strength_checker.py — password analysis logic
- app.py — Flask web server
- index.html — frontend page
- styles.css — page styling
- requirements.txt — Python dependency list

## Usage

1. Open the browser page
2. Enter a password
3. Click **Check strength**
4. Review the strength, entropy, and suggestions

## Notes

- The page must be loaded through Flask so the styles.css path resolves correctly.
- No git operations were performed.
