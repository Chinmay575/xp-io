from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from notebook import getExtractedData
import json


@api_view(["POST"])
def get_data(request):
    print(request)
    try:
        if request.FILES.get("file"):
            f = request.FILES["file"]
            print(f)
            file_content = f.read().decode('utf-8')
            
            # Load JSON data from file content
            j = json.loads(file_content)
            print(j)
            data = getExtractedData(j,'output.json')
            return JsonResponse(
                {
                    "data": data,
                    "error": None,
                },
                status=200,
            )
        else:
            return JsonResponse(
                {
                    "data": None,
                    "error": "field `file` is missing",
                },
                status=400,
            )
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "data": None,
                "error": e.__cause__,
            },
            status=400,
        )
