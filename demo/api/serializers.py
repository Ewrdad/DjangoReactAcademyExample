from rest_framework import serializers
from .models import astro, blogPost

class blogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogPost
        fields = '__all__'

class astroSerializer(serializers.ModelSerializer):
    class Meta:
        model = astro
        fields = '__all__'