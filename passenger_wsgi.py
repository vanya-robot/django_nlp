# -*- coding: utf-8 -*-
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/a/alexeexb/alexeexb.beget.tech/django_ml')
sys.path.insert(1, '/home/a/alexeexb/venv_django/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_ml.settings'

application = get_wsgi_application()
