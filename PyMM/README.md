# overwiev

A little simple mail sender for learning python myself.

referenced book is ...
 『退屈なことはPythonにやらせよう』
   AI Sweigart 著
   相川  愛三     訳

# Synopsis

- setup
  please run setup.sh

- run
  please run "bash run.sh" on terminal.  
  Before run this shell, please overwrite hostname in run.sh.  
  This shell use gunicorn with WSGI.  
  if you want to use other WSGI, you can overwirte this shell source.  

# Structure

- `PyMM/main.py` Flask app (entry point)
- `PyMM/mailsend.py` mailsending program
- `PyMM/logging.py` unused yet.
- `PyMM/templates/` webpage .
- `PyMM/static/`    static contents. css, image.
- `PyMM/env/encoding` default encoding mail.
- `PyMM/env/lg` default login account/password of Gmail.
- `PyMM/env/logging` unused yet.
- `PyMM/env/to` default mailaddress that send to.
- `PyMM/venv/` virtualenv folder.

# Lisense
  PyMiniMailer version 1.0.0  
  (c) 2020 OKKyu allrights reserved under MIT license.  
  
## Author
OKKyu
