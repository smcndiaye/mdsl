from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.template import loader
import json
from Bot import sentiment_mod as s 
from time import gmtime, strftime
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
import warnings
import pickle
import os
import nltk
from sklearn.linear_model import LogisticRegression,SGDClassifier
from nltk.classify.scikitlearn import SklearnClassifier
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
warnings.filterwarnings("ignore")
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

@csrf_exempt
@ensure_csrf_cookie

def classify(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        #data = json.loads(request.body.decode('utf-8'))
        message = data['message']
        chat_response = s.sentiment(message)
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'
    else:
        response['error'] = 'no post data found'

    return HttpResponse(
        json.dumps(response),
            content_type="application/json"
        )


def home(request, template_name="bot/home.html"):
    context = {'title': 'Chatbot version 1.0'}
    return render(None,template_name, context)


def display(request, template_name="bot/txtclass.html"):
    context = {'title': 'Chatbot version 1.0'}
    return render(None,template_name, context)



