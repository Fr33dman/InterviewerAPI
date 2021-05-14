from rest_framework import viewsets, permissions
from .serializers import InterviewSerializer, QuestionSerializer, AnswerSerializer, PossibleAnswerSerializer
from .models import Interview, Question, Answer, PossibleAnswer

from .permissions import IsAdminOrReadOnly


class InterviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super(AnswerViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PossibleAnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = PossibleAnswer.objects.all()
    serializer_class = PossibleAnswerSerializer
