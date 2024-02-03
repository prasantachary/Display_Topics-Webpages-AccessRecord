from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def create_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO= Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'create_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=webpages.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=webpages.objects.all()

        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)

def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')#['C','FB','VB']
        #print(tn)
        QLWO=webpages.objects.none()
        for i in topiclist:
            QLWO=QLWO|webpages.objects.filter(topic_name=i)

        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1) 

    return render(request,'select_multiple_webpage.html',d)

def checkBox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkBox.html',d)