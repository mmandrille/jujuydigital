#!/bin/bash
cd /opt/jujuydigital
source venv/bin/activate
cd /opt/jujuydigital/jujuydigital
gunicorn jujuydigital.wsgi -t 600 -b 127.0.0.1:8000 -w 6 --user=servidor --group=servidor --log-file=/opt/jujuydigital/gunicorn.log 2>>/opt/jujuydigital/gunicorn.log

