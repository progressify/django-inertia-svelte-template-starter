from django.views import View
from inertia import render
import logging


class Index(View):
    def get(self, request):
        logger = logging.getLogger("Index")
        logger.debug("DEBUG")
        logger.info("INFO")
        logger.error("ERROR")
        logger.warning("WARNING")
        logger.critical("CRITICAL HIT! ")
        return render(request, 'sample_app/index', props={
            'events': [
                'Milano',
                'Napoli',
            ],
            'page_name': 'Home'
        })


class About(View):
    def get(self, request):
        return render(request, 'sample_app/about', props={
            'events': [
                'Nola',
                'Cimitile',
            ],
            'page_name': 'About us'
        })
