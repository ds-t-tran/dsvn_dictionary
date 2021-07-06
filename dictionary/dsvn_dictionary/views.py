from copy import Error
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from dsvn_dictionary.models import DsvnDictionary, Vi_Dictionary
from dsvn_dictionary.serializers import DsvnDictionarySerializer
from dsvn_dictionary.serializers import Vi_DictionarySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = DsvnDictionary.objects.all()
        
        title = request.GET.get('title', None)
        
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = DsvnDictionarySerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = DsvnDictionarySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = DsvnDictionary.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = DsvnDictionary.objects.get(pk=pk) 
    except DsvnDictionary.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = DsvnDictionarySerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = DsvnDictionarySerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = DsvnDictionary.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = DsvnDictionarySerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
@api_view(['GET', 'POST', 'DELETE'])
def vidictionary_list(request):
    if request.method == 'GET':
        tutorials = Vi_Dictionary.objects.all()
        
        vi_text = request.GET.get('vi_text', None)
        if vi_text is not None:
            tutorials = tutorials.filter(title__icontains=vi_text)
        
        tutorials_serializer = Vi_DictionarySerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        vidic_data = JSONParser().parse(request)
        vidic_serializer = Vi_DictionarySerializer(data=vidic_data)
        if vidic_serializer.is_valid():
            vidic_serializer.save()
            return JsonResponse(vidic_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vidic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Vi_Dictionary.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def vidictionary_search(request):
    if request.method == 'GET':
        title_name=request.GET['vi_text']
        # if title_name is not None:
        #     return JsonResponse(Error("please enter key search"), status=status.HTTP_400_BAD_REQUEST)

        tutorials = Vi_Dictionary.objects.raw("SELECT id, vi_text FROM dsvn_dictionary_vi_dictionary WHERE vi_text=%s",[title_name])
        tutorials_serializer = Vi_DictionarySerializer(tutorials, many=True)
        
        return JsonResponse(tutorials_serializer.data, safe=False)

    if request.method == 'DELETE':
        title_name = request.GET['vi_text']
        Vi_Dictionary.objects.filter(vi_text = title_name).delete()
        return JsonResponse({'message': 'Tutorials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def vidictionary_update(request, pk):

    try: 
        tutorial = Vi_Dictionary.objects.get(id=pk) 
    except Vi_Dictionary.DoesNotExist: 
        return JsonResponse({'message': 'The vi dictionary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Vi_DictionarySerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 