from django.shortcuts import render#,render_to_response
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import os
import requests
from django.http import HttpResponse,JsonResponse
import json
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
IMG_SIZE = 80

@csrf_exempt

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        img = im_data = mpimg.imread(myfile)
        image_resized = resize(im_data, (80,80,1),
                       anti_aliasing=True)
        im   = np.array(image_resized)
        im = im.reshape(-1,IMG_SIZE,IMG_SIZE,1)
    
        url = "https://rety-model.herokuapp.com/"
        data = {'arr': im.tolist()}
        resp = requests.post(url, json=data)
        todos = json.loads(resp.text)
        results = todos['predicted'][0]
        print(results)
        context = [round(results[0]*100),round(results[1]*100),round(results[2]*100),round(results[3]*100),round(results[4]*100)]
        return render(request, 'rpd/home.html',{'results': context})
    return render(request, 'rpd/home.html')


