from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import blogPost


from .serializers import blogPostSerializer
# Create your views here.


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