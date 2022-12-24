from django.urls import path
from .views import QuizListView, QuestionListView, TopicListView,OptionListViev,StudentListView,StudentListView1,UpdaterStudent,ResultListView

urlpatterns = [
    path('quiz/', QuizListView.as_view()),
    path('quiz/<int:pk>/', QuestionListView.as_view()),
    path('question/', QuestionListView.as_view()),
    path('topic/<int:pk>/', TopicListView.as_view()),
    path('option/', OptionListViev.as_view()),
    path('student/', StudentListView.as_view()),
    path('studentget/<int:chatid>/', StudentListView1.as_view()),
    path('updaterstudent/<int:pk>/', UpdaterStudent.as_view()),
    path('resultadd/', ResultListView.as_view())
]