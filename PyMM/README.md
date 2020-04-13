# overwiev

A little simple mail sender for my python practice.

referenced book is ...
 『退屈なことはPythonにやらせよう』
   AI Sweigart 著
   相川  愛三     訳

# Synopsis

```sh
# setup
 please run setup.sh

# run
 please run run.sh
 * Before run this shell, please overwrite hostname in this run.sh.
 
 This shell use gunicorn with WSGI.
 if you want to use other WSGI, you can overwirte this shell source.
 
```

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
- `PyMM/venv/` vurtualenv folder.

# Lisense

## Author
OKKyu
