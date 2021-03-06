from rest_framework import serializers 
from files.models import Files
 
 
class FileSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Files
        fields = ('id',
                  'title',
                  'description',
                  'published')