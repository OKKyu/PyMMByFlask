#! python3
# -*- coding:utf-8

def mailsend(smtpAddr, smtpPort, frAddr, passwd, toAddrs, subject, msg):
#import
  import smtplib
  from email.mime.text import MIMEText
  from email.header import Header
  
  try:
  #validation check
    if type(smtpAddr) is not str:
      raise ValueError('smtpAddr has uncorrect value. Type str is correct.')
    
    if type(smtpPort) is not int:
      raise ValueError('smtpPort has uncorrect value. Type int is correct.')
    
    if type(frAddr) is not str:
      raise ValueError('frAddr has uncorrect value. Type str is correct.')
    
    if type(passwd) is not str:
      raise ValueError('passwd has uncorrect value. Type str is correct.')
    
    if type(toAddrs) is not str:
      raise ValueError('toAddrs has uncorrect value. Type str is correct.')
    elif len(toAddrs) <= 0:
      raise ValueError('toAddrs has no value. please give toAddr value least one.')
    
    if type(subject) is not str:
      raise ValueError('subject has uncorrect value. Type str is correct.')
    
    if type(msg) is not str:
      raise ValueError('msg has uncorrect value. Type str is correct.')
    
  #open smtp. 
    obj = smtplib.SMTP(smtpAddr, smtpPort)
    obj.ehlo()
    obj.starttls()
      
  #login attempt
    obj.login(frAddr, passwd)
      
  #message setting
    msg = msg
    
  #constructing MIMEText
    info = MIMEText(msg, 'plain', 'utf-8')
    info['Subject'] = Header(subject, 'utf-8')
    info['From'] = frAddr
    info['To']   = toAddrs
    
  #send
    obj.sendmail(info["From"], info["To"], info.as_string())
  #close
    obj.quit()
    
  except Exception as ex:
    raise
  finally:
    pass