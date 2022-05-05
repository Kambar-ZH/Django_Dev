from rest_framework import serializers
from api.models.topic import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicGridSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
