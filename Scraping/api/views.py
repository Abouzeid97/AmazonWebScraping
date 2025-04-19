from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .SeleniumScraper import scraper

class ScrapeView(APIView):
    def post(self, request):
        search_term = request.data.get("search_term")
        if not search_term:
            return Response({"error": "search_term is required"}, status=status.HTTP_400_BAD_REQUEST)

        data = scraper(search_term)
        return Response(data, status=status.HTTP_200_OK)