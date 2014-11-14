from django.template import Context
from django.shortcuts import  render
from django.template import RequestContext
from django.http import HttpResponse
from django import template
from django.conf import settings
from shoeRanks.models import imageOrders
import os
import random
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
    #if request.method == 'POST':
    location1 = random_image()
    location2 = random_image()
    attributes = ['Shiny','Open','Dark in Color','High Heeled']
    index = random.randint(0,len(attributes)-1)
    queryString = ''
    if request.GET:
        queryString = request.get_full_path()
        queryString = queryString.split("&",2)[2]
        queryString = queryString.split("=",1)[1]
    if queryString == 'ImageOne':
        data = imageOrders.objects.create(attribute = index,first_image = location1,second_image = location2)
        print queryString
    elif queryString == 'ImageTwo':
        data = imageOrders.objects.create(attribute = index,first_image = location2,second_image = location1)
        print queryString
    else:
        print "ERROR"
    return render(request,'compare.html',{'attribute': attributes[index], 'file_location1' : location1,'file_location2' : location2})

def results(request):
    
    return HttpResponse("Hello world")
