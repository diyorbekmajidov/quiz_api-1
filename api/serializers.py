from .models import Quiz, Question, Option, Topic, Student, Result, ResultDetail
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class Topicserilaizers(serializers.ModelSerializer):
    class Meta:
        quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
        model = Topic
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        quiz = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
        model = Option
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
        topic = serializers.PrimaryKeyRelatedField(queryset = Topic.objects.all())
        model = Result
        fields = '__all__'

class ResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        result = serializers.PrimaryKeyRelatedField(queryset=Result.objects.all())
        question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
        option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())
        model = ResultDetail
        fields = '__all__'
