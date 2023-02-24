from django.shortcuts import render
from django.http import JsonResponse
from ChatGPTAPP.chat import chat_gen
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([AllowAny])

def generate_answers(request):
    question = request.data["question"]
    answer = chat_gen(question)

    return JsonResponse(
            {"Answer": [answer]}
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def healthz(request):
     return JsonResponse({"result": "OK - healthy"},status=200)