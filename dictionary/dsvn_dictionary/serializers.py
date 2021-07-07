from django.db import models
from rest_framework import serializers 
from dsvn_dictionary.models import DsvnDictionary, Vi_Dictionary, Ja_Dictionary
 
 
class DsvnDictionarySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = DsvnDictionary
        fields = ('id',
                  'title',
                  'description',
                  'published')
                  
class Vi_DictionarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vi_Dictionary
        fields = "__all__"

class Ja_DictionarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ja_Dictionary
        fields = "__all__"