# 🎂 Birthday Wisher - Automated Email Greetings 📧

A Python application that automatically sends personalized birthday emails to your loved ones on their special day.

***
<p align="center">
    <img src="https://marketplace.canva.com/EAFYJKGkaTQ/2/0/1600w/canva-white-and-gold-modern-greeting-happy-birthday-card-YQuXbM7Sca8.jpg" alt="Birthday Candles" width="300">
</p>

***
## ✨ Features

* **📅 Automatic Date Checking:** Checks if today's date matches any birthday in your database.
* **📝 Random Letter Templates:** Selects from multiple customizable letter templates for variety.
* **🔄 Name Personalization:** Automatically replaces placeholder text with the recipient's actual name.
* **📬 SMTP Email Sending:** Sends birthday wishes directly via Gmail's SMTP server.
* **📊 CSV Data Management:** Easy-to-manage birthday data in a simple CSV format.

***

## 🛠️ Prerequisites

To run this program, you need:

* Python 3.x
* **pandas** library
* A Gmail account with [App Password](https://support.google.com/accounts/answer/185833) enabled

Install pandas using pip:

```bash
pip install pandas
```

***

## ⚙️ Setup Instructions

1. **Configure Email Credentials:**
   
   Update the sender email and app password in `main.py`:
   ```python
   sender = "your_email@gmail.com"
   password = "your_app_password"
   ```

2. **Add Birthdays to Track:**
   
   Edit `birthdays.csv` with the following format:
   ```csv
   name,email,year,month,day
   John,john@example.com,1990,5,15
   Jane,jane@example.com,1985,12,25
   ```

3. **Customize Letter Templates:**
   
   Edit the templates in `letter_templates/` folder. Use `[NAME]` as a placeholder for personalization.

***

## 🚀 How to Run

1. Navigate to the project directory in your terminal:

   ```bash
   cd Project-09-Birthday_Wisher
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. If today matches a birthday, an email will be sent automatically!

***

## 💡 How It Works

1. **Load Data:** Reads birthday information from `birthdays.csv`.
2. **Check Date:** Compares today's date (month and day) against stored birthdays.
3. **Match Found:** If a match exists, selects a random letter template.
4. **Personalize:** Replaces `[NAME]` placeholder with the birthday person's name.
5. **Send Email:** Connects to Gmail SMTP server and delivers the birthday message.

***

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `main.py` | The **main application** that handles date checking, template selection, and email sending. |
| `birthdays.csv` | **Birthday database** containing names, emails, and birth dates. |
| `letter_templates/letter_1.txt` | **Template 1** - A short and sweet birthday greeting. |
| `letter_templates/letter_2.txt` | **Template 2** - An alternative birthday message. |
| `letter_templates/letter_3.txt` | **Template 3** - Another variation of birthday wishes. |

***

## 🔧 Automation Tips

To run this script daily automatically:

| Platform | Method |
| :--- | :--- |
| **Windows** | Use Task Scheduler to run the script daily |
| **macOS/Linux** | Set up a cron job: `0 8 * * * python /path/to/main.py` |
| **Cloud** | Deploy on PythonAnywhere or similar service |

***

## ⚠️ Important Notes

* **Gmail Security:** You must use an [App Password](https://support.google.com/accounts/answer/185833), not your regular Gmail password.
* **2FA Required:** App Passwords require Two-Factor Authentication to be enabled.
* **Privacy:** Never commit your actual email credentials to version control.
* **Testing:** Test with your own email first before adding others.

***

## 🎯 Use Cases

* **Personal:** Never forget a friend or family member's birthday again!
* **Business:** Send automated birthday greetings to clients or team members.
* **Learning:** Great project for understanding SMTP, file handling, and date operations in Python.
