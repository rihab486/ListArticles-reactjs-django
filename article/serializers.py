from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer) : 
     class Meta : 
        model = Article
        fields = [
          'id',
          'declarationarabe',
          'declarationlatine',
          'classe',
          'unite',
          'validité',
          'numero_de_lot',
          'remarque',
          'variable',
          'idClassification',
          'ch'
          
     
        ]
class ClassificationSerializer(serializers.ModelSerializer) : 
     class Meta : 
        model = Classification
        fields = [
          'id',
          'nom'
          
     
        ]