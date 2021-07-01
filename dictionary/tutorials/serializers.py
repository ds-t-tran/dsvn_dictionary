from rest_framework import serializers 
from tutorials.models import Tutorial, Word
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'created_at')

        model = Word
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'created_at')