import smtplib

fadd = 'kotagirikranthi31@gmail.com'
tadd = 'kotagirikranthi31@gmail.com'
msg = 'mail sent through Python!'
username = 'kotagirikranthi31@gmail.com'
password = '9299552354'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
