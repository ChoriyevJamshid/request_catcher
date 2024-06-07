from rest_framework import generics
from rest_framework.response import Response

from rest_framework.views import APIView

from . import serializers


class HomeAPIView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        return Response({"message: POST"})


class RequestCatcherView(generics.GenericAPIView):

    serializer_class = serializers.RSerializer

    def get(self, request, *args, **kwargs):

        headers = request.headers
        path = kwargs.get("path", "/")

        return Response({
            "message": "GET",
            "headers": headers,
            "path": path
        })

    def post(self, request, *args, **kwargs):
        headers = request.headers
        path = kwargs.get("path", "/")

        return Response({
            "message": "POST",
            "headers": headers,
            "path": path
        })

    def put(self, request, *args, **kwargs):
        headers = request.headers
        path = kwargs.get("path", "/")
        return Response({
            "message": "PUT",
            "headers": headers,
            "path": path
        })

    def patch(self, request, *args, **kwargs):
        headers = request.headers
        path = kwargs.get("path", "/")
        return Response({
            "message": "PATCH",
            "headers": headers,
            "path": path
        })

    def head(self, request, *args, **kwargs):
        headers = request.headers
        path = kwargs.get("path", "/")
        return Response({
            "message": "HEAD",
            "headers": headers,
            "path": path
        })

    def options(self, request, *args, **kwargs):
        headers = request.headers
        path = kwargs.get("path", "/")
        return Response({
            "message": "OPTIONS",
            "headers": headers,
            "path": path
        })



