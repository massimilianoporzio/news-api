from rest_framework import serializers
from rest_framework.settings import api_settings

from news.models import Article


class ArticleSerializer(serializers.Serializer):
    """ Serializer per oggetti Article"""
    id = serializers.IntegerField(read_only=True)  # chiave primaria
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)  # non editabile
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Crea una nuova istanza di Article sulla base di validated_data
        :param validated_data: dati in input validati
        :return: istanza di Article
        """
        # print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Aggiorna una  istanza di Article sulla base di validated_data
        :param instance: istanza (Article) da aggiornare
        :param validated_data: dati in input validati
        :return: l'istanza di Article aggiornata con i validated data
        """
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body',instance.body)
        instance.location = validated_data.get('location',instance.location)
        instance.publication_date = validated_data.get('publication_date',instance.publication_date)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
