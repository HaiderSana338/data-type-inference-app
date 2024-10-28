from django.shortcuts import render
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .infer_data_types import load_and_infer

class FileUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Load and infer data types
            inferred_types = load_and_infer(file)
            return Response({"inferred_data": inferred_types}, status=status.HTTP_200_OK)

        except Exception as e:
            # Log the error message to the console
            print(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




