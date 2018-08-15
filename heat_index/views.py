from django.shortcuts import render
from django.views import View
from firebase_admin import credentials, db

import firebase_admin

# Create your views here.


class IndexView(View):
    # Load Firebase data
    cred = credentials.Certificate(
        './ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://iot-heat-index.firebaseio.com/'
    })

    def get(self, request):
        data = db.reference().get()
        
        context = {
            'temperature': data['temperature'],
            'humidity': data['humidity'],
            'heat_index': int(data['heat_index']),
        }

        return render(request, 'heat_index/index.html', context)
