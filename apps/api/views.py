import json

from django.http import JsonResponse
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.api.models import SomeUser


class ListUsers(APIView):
    def get(self, request, format=None):
        users = SomeUser.objects.all()
        return Response(users)

    def post(self, request, format=None):
        data = json.loads(request.body.decode('utf-8'))
        res = SomeUser.create_user(**data)
        return Response(res.to_json())


class DetailUser(APIView):

    def get_object(self, pk):
        try:
            return SomeUser.objects.get(pk=pk)
        except SomeUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        return Response(user.to_json())

    def put(self, request, pk, format=None):
        #TODO: not in prototype
        return Response({})

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def ping(request):
    return JsonResponse({'answer': 'pong'})
