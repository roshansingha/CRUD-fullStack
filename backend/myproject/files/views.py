from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from files.models import Files
from files.serializers import FileSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def file_list(request):
    if request.method == 'GET':
        files = Files.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            files = files.filter(title__icontains=title)
        
        files_serializer = FileSerializer(files, many=True)
        return JsonResponse(files_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        file_data = JSONParser().parse(request)
        file_serializer = FileSerializer(data=file_data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Files.objects.all().delete()
        return JsonResponse({'message': '{} Files were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def file_detail(request, pk):
    try: 
        file = Files.objects.get(pk=pk) 
    except Files.DoesNotExist: 
        return JsonResponse({'message': 'The file does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        file_serializer = FileSerializer(file) 
        return JsonResponse(file_serializer.data) 
 
    elif request.method == 'PUT': 
        file_data = JSONParser().parse(request) 
        file_serializer = FileSerializer(file, data=file_data) 
        if file_serializer.is_valid(): 
            file_serializer.save() 
            return JsonResponse(file_serializer.data) 
        return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        file.delete() 
        return JsonResponse({'message': 'File was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def file_list_published(request):
    files = Files.objects.filter(published=True)
        
    if request.method == 'GET': 
        files_serializer = FileSerializer(files, many=True)
        return JsonResponse(files_serializer.data, safe=False)