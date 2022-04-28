from api.models.step import Step
from api.serializers.step import StepSerializer
from rest_framework import viewsets


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
