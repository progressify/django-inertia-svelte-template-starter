from django.views import View
from inertia import render

class Contacts(View):
    def get(self, request):
        return render(request, 'another_app/contacts', props={
            'events': [
                'Napoli',
            ],
            'page_name': 'Contacts'
        })
