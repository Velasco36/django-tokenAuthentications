from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from firebase_admin import auth
from django.shortcuts import render

from .models import User
from django.views.generic import TemplateView
from .serializers import LoginSocialSeilizers


class LoginUser(TemplateView):
    template_name = "users/login.html"
# Create your views here.

class GoogleLoginView(APIView):
    serializer_class = LoginSocialSeilizers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        decoded_token = auth.verify_id_token(id_token)

        email = decoded_token['email']
        name = decoded_token['name']
        avatar = decoded_token['picture']
        verified = decoded_token['email_verified']

        usuario, created = User.objects.get_or_create(
            email=email,
            defaults={
                'full_name': name,
                'email': email,
                'is_active': True,
            }
        )
        #
        if created:
            token = Token.objects.create(user=usuario)
        else:
            token= Token.objects.get(user=usuario)

        userGet = {
            'id': usuario.pk,
            'email':usuario.email,
            'full_name': usuario.full_name,
            'genero': usuario.genero,
            'date_birth': usuario.date_birth,
            'city': usuario.city
        }

        
        return Response(
            {
                'token':token.key,
                'user': userGet
            }
        )
