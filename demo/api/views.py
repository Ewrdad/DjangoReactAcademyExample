from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import blogPost, astro
import requests
import datetime
from pathlib import Path
import os

from .serializers import blogPostSerializer, astroSerializer

def log(details):
    #Log the request
    BASE_DIR = Path(__file__).resolve().parent.parent
    file = open(str(BASE_DIR)+"/log/"+str(datetime.date.today())+".txt","a")
    file.write(str(datetime.datetime.now()) + ":::"+ str(details) + "\n")
    file.close()



#Display public URL list for the APIs(Outdate)
@api_view(['GET'])
def apiOverview(request):

    log(request)
   
    api_public_urls = {
        'recent' :'/recent/',
        'Detailed' : '/details/<str:pk>/',
        'Create' : '/create-post/',
        'ListSome' : '/list/',

    }

    return Response(api_public_urls)

#Returns all blog data
@api_view(['GET'])
def blogList(request):
    log(request)
    blogPosts = blogPost.objects.all()
    serailizer = blogPostSerializer(blogPosts, many=True)
    return Response(serailizer.data)
#Possibility to add filter for top x number of posts by also lookibng at objects.latest then subtracting 
#Not done because small quantity and I messed up and deleted 2

#Returns individual blog post
@api_view(['GET'])
def blogDetail(request, pk):
    log(request)
    blogPosts = blogPost.objects.get(postID=pk)
    serailizer = blogPostSerializer(blogPosts, many=False)
    return Response(serailizer.data)

#Retreives letest blog post
@api_view(['GET'])
def blogLatest(request):
    log(request)
    blogPosts = blogPost.objects.latest('postID')
    #print(blogPosts)
    serailizer = blogPostSerializer(blogPosts, many=False)
    print(serailizer)
    return Response(serailizer.data)


#Handles the logging and broadcasting of astronauts in space
@api_view(['GET'])
def astroCurr(request):
    log(request)
    
    now = datetime.date.today()
    astros = astro.objects.latest('astroID')


    if astros.astroDay != now.day or astros.astroMonth != now.month or astros.astroYear != now.year:
        response = requests.get('http://api.open-notify.org/astros.json')
        json=response.json()

        for person in json['people']:
            print("Updating Database with")
            print(person["name"], person["craft"])

            #Creates an astronaut object with details such as in database
            b = astro(astroName=person["name"], astroCraft=person["craft"],astroDay = now.day, astroMonth = now.month ,astroYear = now.year)
            #Saves the information
            b.save()
            #clears out the astronaut object....I think
            b = astro()
            
    #Creates query to the database for todays date
    quer = astro.objects.filter(astroDay = now.day, astroMonth = now.month, astroYear = now.year)
    #print(quer)

    #Formats data for response
    serailizer = astroSerializer(quer, many=True)

    return Response(serailizer.data)








#Features that never happened
#@csrf_exempt
@api_view(['POST'])
def makeBlog(request):
    serializer = blogPostSerializer(data = request.data)
    print(serializer)
    #print(request.POST["username"])
    #data = JSONParser().parse(request)
    #serailizer = blogPostSerializer(data, many=False)
    #print(data)

    return Response("Submitted")
#prevented due to cross site scripting protect preventing react front end from working. Did work if done entirely withing Django


#Locate ISS data
@api_view(['GET'])
def locISS(request):
    print("hello")
    response = requests.get('http://api.open-notify.org/iss-now.json')
    json = response.json()
    return Response(json)
#Prevented due to issues on the front end. Api still works