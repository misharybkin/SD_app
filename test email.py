import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ваші дані для підключення до поштового сервера
email_address = 'm.rybkin@lot.pl'
email_password = 'RealMadrid3_1PSG'
smtp_server = 'smtp.office365.com'
smtp_port = 587

# Отримувач і тема листа
to_email = 'mryb@ukr.net'
subject = 'Тема вашого листа'

# Текст листа
body = 'Текст вашого листа.'

# Створення об'єкта листа
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Встановлення з'єднання з поштовим сервером
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_address, email_password)

# Відправлення листа
server.sendmail(email_address, to_email, msg.as_string())

# Закриття з'єднання з сервером
server.quit()
