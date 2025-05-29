"""
WSGI config for YWS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os, sys
site_user_root_dir = '/home/a/acid45k9/acid45k9.beget.tech/public_html'
sys.path.insert(0, site_user_root_dir + '/yogaws')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.11/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YWS.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()