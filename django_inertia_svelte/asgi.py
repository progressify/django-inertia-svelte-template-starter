import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_inertia_svelte.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Base')

from configurations.asgi import get_asgi_application

application = get_asgi_application()
