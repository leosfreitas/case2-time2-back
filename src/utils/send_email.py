import os
import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart

sender = "testeps2fase@gmail.com" 
password = os.environ.get("GMAIL_PASSWORD")

def send_email(email, content):
    # Cria uma mensagem multipart para suportar HTML
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "FinTrack - Redefinição de senha"  
    msg['From'] = sender  
    msg['To'] = email  

    # Adiciona o conteúdo em formato HTML
    html_content = MIMEText(content, "html")
    msg.attach(html_content)
    
    # Envia o e-mail com suporte a HTML
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password) 
        smtp_server.sendmail(sender, email, msg.as_string())
