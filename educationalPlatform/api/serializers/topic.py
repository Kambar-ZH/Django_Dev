from rest_framework import serializers
from api.models.topic import Topic
from api.serializers.step import StepSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicGridSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'steps']
