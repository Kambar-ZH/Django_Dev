from rest_framework import serializers
from api.models.topic import Topic
from api.serializers.step import StepSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicGridSerializer(serializers.ModelSerializer):
    steps = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = '__all__'

    def get_steps(self, obj):
        steps = obj.step_set.all()
        serializer = StepSerializer(steps, many=True)
        return serializer.data
