from urllib import request
from django.shortcuts import render

from .models import Question

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'List':'/question',
        'Detail View':'/question/<str:pk>/',
        'Create':'/question/',
        'Update':'/question/<str:pk>/',
        'Delete':'/question/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def questionList(res):
    question = Question.objects.all()
    serializer = QuestionSerializer(question, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def questionDetail(res, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(question, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def questionCreate(res):
    serializer = QuestionSerializer(data=res.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def questionUpdate(res, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(instance=question, data=res.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def questionDelete(res, pk):
    question = Question.objects.get(id=pk)
    question.delete()

    return Response({'Delete Ok!'})
