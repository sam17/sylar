from django.template.loader import get_template
from django.template import Context
from django.shortcuts import  render
from django.http import HttpResponse
import os
import random
from django import template
from django.conf import settings
import datetime

def random_image():
    try:
        valid_extensions = settings.RANDOM_IMAGE_EXTENSIONS
    except AttributeError:
        valid_extensions = ['.jpg','.jpeg','.png','.gif',]


    rel_dir = settings.RANDOM_IMAGE_DIR
    rand_dir = os.path.join(settings.MEDIA_ROOT, rel_dir)

    files = [f for f in os.listdir(rand_dir) if os.path.splitext(f)[1] in valid_extensions]

    #print os.path.join(rel_dir, random.choice(files))
    return os.path.join(rel_dir, random.choice(files))

def home(request):
	now = datetime.datetime.now()
	now = now + datetime.timedelta(minutes = 10)
	return render(request,'home.html',{'current_time': now})

def compare(request):
	location1 = random_image()
	location2 = random_image()
	return render(request,'compare.html',{'attribute': 'Sexy', 'file_location1' : location1,'file_location2' : location2})

def hello(request):
    return HttpResponse("Hello world")
