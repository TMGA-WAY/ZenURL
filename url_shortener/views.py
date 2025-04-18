from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponseRedirect, JsonResponse

from .schema.long_url_serializer import LongUrlSerializer
from .service import url_shortner_service


class HomeView(APIView):
    def get(self, request, slug):
        """
        Redirect to the original URL based on the slug.
        """
        url = url_shortner_service.get_long_url(slug)
        if not url:
            return JsonResponse({"error": "URL Not Found"}, status=status.HTTP_404_NOT_FOUND)

        return HttpResponseRedirect(url)


class ShortenUrlView(APIView):
    def post(self, request):
        payload = LongUrlSerializer(data=request.data)

        if not payload.is_valid():
            return Response(payload.errors, status=status.HTTP_400_BAD_REQUEST)

        res = url_shortner_service.create_short_url(payload.validated_data["url"], extra_small = payload.validated_data["extra_small"])

        return Response(res, status=status.HTTP_201_CREATED)
