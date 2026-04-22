# Birthday Wisher

Automatically sends personalized birthday emails to people in your contacts list when today matches their birthday.

## How It Works

1. Reads `birthdays.csv` to get a list of contacts and their birthdays
2. Checks if today's date matches any birthday
3. Picks a random letter template from `letter_templates/` and fills in the person's name
4. Sends the personalized email via Gmail SMTP

## Setup

### Prerequisites

- Python 3
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) enabled

### Install dependencies

```bash
pip install pandas
```

### Configure your credentials

In `main.py`, update the following with your Gmail address and App Password:

```python
my_email = "your_email@gmail.com"
password = "your_app_password"
```

### Add birthdays

Edit `birthdays.csv` to add your contacts:

```
name,email,year,month,day
Alice,alice@example.com,1990,6,15
Bob,bob@example.com,1985,12,3
```

### Customize templates

Edit the files in `letter_templates/` (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`). Use `[NAME]` as a placeholder — it will be replaced with the recipient's name when the email is sent.

## Running

```bash
python main.py
```

To run this automatically every day, use a scheduler like `cron` (macOS/Linux) or Task Scheduler (Windows).

**Example cron job (runs daily at 8am):**

```
0 8 * * * /usr/bin/python3 /path/to/main.py
```
