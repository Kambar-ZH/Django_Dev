from rest_framework import serializers
from api.models.step import Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'
