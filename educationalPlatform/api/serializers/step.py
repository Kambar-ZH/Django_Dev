from rest_framework import serializers
from api.models.step import Step
from api.serializers.video import VideoDetailSerializer


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class StepDetailSerializer(serializers.ModelSerializer):
    videos = VideoDetailSerializer(many=False, read_only=True)

    class Meta:
        model = Step
        fields = '__all__'