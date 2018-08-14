from django.shortcuts import render
from django.views import View
from firebase_admin import credentials

import firebase_admin
# Create your views here.

class IndexView(View):
    def get(self, request):
        context = {
            'temperature': 20,
            'humidity': 70
        }
        return render(request, 'heat_index/index.html', context)
