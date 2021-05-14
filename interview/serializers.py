from rest_framework import serializers
from .models import Interview, Question, Answer, PossibleAnswer


class InterviewSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(InterviewSerializer, self).__init__(*args, **kwargs)

        request = self.context['request']
        if request.method == 'PUT':
            self.fields.pop('start_time')

    class Meta:
        model = Interview
        fields = ['id', 'name', 'start_time', 'end_time', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class PossibleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAnswer
        fields = '__all__'
