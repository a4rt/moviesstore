import os
import sys

# Ensure project root is on sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.settings')
import django
django.setup()
from django.template import engines

libs = sorted(engines['django'].engine.template_libraries.keys())
print(libs)
