import http
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from api.models.registration_form import NewUserForm

from rest_framework.permissions import AllowAny


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form_data = json.loads(request.body.decode())
        form = NewUserForm(form_data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response(data=None, status=http.HTTPStatus.CREATED)
        return Response(data=form.errors, status=http.HTTPStatus.BAD_REQUEST)
