from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status



from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer,Topicserilaizers
# Create your views here.

from .models import Quiz, Question, Option, Topic


# View for get all quiz
class QuizListView(APIView):
    def get(self, request: Request):
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)


    def post(self, request:Request):
        data=request.data
        serializer = QuizSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TopicListView(APIView):
    def get(self, request:Request, pk):
        quiz = Quiz.objects.get(id = pk)
        topic = Topic.objects.filter(quiz = quiz)
        serilaizer1 = QuizSerializer(quiz, many = False)
        serilaizer = Topicserilaizers(topic, many = True)
        data = {
            'quiz':serilaizer1.data,
            'topic':serilaizer.data
        }
        return Response(data)
    def post(self, request:Request):
        data = request.data
        serializer = Topicserilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class QuestionListView(APIView):
    def get(self, request:Request, pk):
        topic_id=Topic.objects.get(id = pk)
        topic = Topicserilaizers(topic_id, many = False)
        quiz_id = Quiz.objects.get(id=topic.data["quiz"])
        quiz = QuizSerializer(quiz_id)
        question_id = Question.objects.filter(topic=topic.data["id"])
        question = QuestionSerializer(question_id, many=True)

        data={
            "id":quiz.data["id"],
            "title":quiz.data["title"],
            "topic":{
                "id":topic.data["id"],
                "topic_name":topic.data["title"],
                "question":[],
                'quetion_index':list(range(1, len(question.data)+1)),
            }
        }
        for i in question.data:
            options = Option.objects.filter(question=i['id'])
            option_serializer = OptionSerializer(options, many=True) 
            data['topic']['question'].append({
                'id':i['id'],
                'title':i['title'],
                'topic_id':i['topic'],
                'img':i["img"],
                "optons":option_serializer.data
            })

        return Response(data)

    def post(self, request:Request):
        data=request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class OptionListViev(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = OptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class CheckAnswerView(APIView):
    pass

class GetResultView(APIView):
    pass



   
    