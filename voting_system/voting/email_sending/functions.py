import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # для SSL подключения
smtp_server = "smtp.yandex.ru"
sender_email = "licknovoting@yandex.ru"  # Емайл
pass_path = "password.txt"              # Путь до файла с паролем
password = open(pass_path, 'r').read()
htmlWay = "voting/templates/email_templ.html"# в этом шаблоне заполняются {name}, {_pass} и {body_text} - описание голосования
html = open(htmlWay, 'r', encoding='utf8').read()


def create_message(subject: str, to: str, html='', text=''):
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    if isinstance(subject, str):
        message["Subject"] = subject
    else:
        Exception()
    if isinstance(to, str | list):
        if isinstance(to, list):
            if isinstance(to[0], str):
                message["To"] = to
            else:
                Exception()
        else:
            message["To"] = to
    else:
        Exception()
    if isinstance(html, str) and isinstance(text, str):
        # Сделать их текстовыми\html объектами MIMEText
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Почтовый клиент сначала попытается отрендерить последнюю часть
        message.attach(part1)
        message.attach(part2)
    else:
        Exception()
    return message


def send_email(email: str, name: str, _pass):
    subject = "Вы участвуете в голосовании"
    body_text = "голосование по рекомендации кандидатов"
    text = ''
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, email, create_message(
                                                subject,
                                                email,
                                                html.format(
                                                    name=name,
                                                    _pass=_pass,
                                                    body_text=body_text),
                                                text=text).as_string()
        )