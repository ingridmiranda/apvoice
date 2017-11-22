# -*- coding: utf-8 -*-
import mimetypes
import os
import smtplib
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def adiciona_anexo(msg, filename):
    if not os.path.isfile(filename):
        return
    ctype, encoding = mimetypes.guess_type(filename)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    maintype, subtype = ctype.split("/", 1)
    if maintype == "text":
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)
    elif maintype == "image":
        with open(filename, "rb") as f:
            mime = MIMEImage(f.read(), _subtype=subtype)
    elif maintype == "audio":
        with open(filename, "rb") as f:
            mime = MIMEAudio(f.read(), _subtype=subtype)
    else:
        with open(filename, "rb") as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())
        encoders.encode_base64(mime)
    mime.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(mime)
de = " "
para = [" "]
msg = MIMEMultipart()
msg["From"] = de
msg["To"] = ", ".join(para)
msg["Subject"] = "Alerta Campainha"
# Corpo da mensagem
msg.attach(MIMEText("Atenção! Esta pessoa acabou de tocar a campainha da sua casa...", "html", "utf-8"))
# Arquivos anexos.
adiciona_anexo(msg, "imagem.jpg")
raw = msg.as_string()
smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp.login(" ", " ")
smtp.sendmail(de, para, raw)
smtp.quit()
