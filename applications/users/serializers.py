from rest_framework import serializers

class LoginSocialSeilizers(serializers.Serializer):

    token_id= serializers.CharField(required=True)