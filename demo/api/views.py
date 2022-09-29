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

from .serializers import blogPostSerializer, astroSerializer

@api_view(['GET'])
def apiOverview(request):
    api_public_urls = {
        'recent' :'/recent/',
        'Detailed' : '/details/<str:pk>/',
        'Create' : '/create-post/',
        'ListSome' : '/list/',

    }

    return Response(api_public_urls)

@api_view(['GET'])
def blogList(request):
    blogPosts = blogPost.objects.all()
    serailizer = blogPostSerializer(blogPosts, many=True)
    return Response(serailizer.data)

@api_view(['GET'])
def blogDetail(request, pk):
    blogPosts = blogPost.objects.get(postID=pk)
    serailizer = blogPostSerializer(blogPosts, many=False)
    return Response(serailizer.data)

@api_view(['GET'])
def blogLatest(request):
    blogPosts = blogPost.objects.latest('postID')
    print(blogPosts)
    serailizer = blogPostSerializer(blogPosts, many=False)
    print(serailizer)
    return Response(serailizer.data)

@api_view(['GET'])
def astroCurr(request):
    
    now = datetime.date.today()
    print(now.year)
    print(now.month)
    print(now.day)
    astros = astro.objects.latest('astroID')
    print(astros.astroDay)

    if astros.astroDay != now.day or astros.astroMonth != now.month or astros.astroYear != now.year:
        response = requests.get('http://api.open-notify.org/astros.json')
        print("this isi a log")
        json=response.json()

        for person in json['people']:
            print(person["name"], person["craft"])
            b = astro(astroName=person["name"], astroCraft=person["craft"],astroDay = now.day, astroMonth = now.month ,astroYear = now.year)
            b.save()
            b = astro()
            print("hey") 

    quer = astro.objects.filter(astroDay = now.day, astroMonth = now.month, astroYear = now.year)
    print(quer)
    serailizer = astroSerializer(quer, many=True)

    return Response(serailizer.data)

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
