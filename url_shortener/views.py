import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .schema.long_url_serializer import LongUrlSerializer
from .service import url_shortner_service


class HomeView(View):
    def get(self, request):
        # TODO: Include Other features
        return render(request, 'url_shortener/home.html')


class ShortenUrlView(APIView):
    def post(self, request):
        payload = LongUrlSerializer(data=request.data)

        if not payload.is_valid():
            return Response(payload.errors, status=status.HTTP_400_BAD_REQUEST)

        res = url_shortner_service.create_short_url(payload.validated_data["url"])

        return Response(res, status=status.HTTP_201_CREATED)
