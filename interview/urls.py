from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import InterviewViewSet, QuestionViewSet, AnswerViewSet, PossibleAnswerViewSet

app_name = 'interview'

router = DefaultRouter()
router.register('interview', InterviewViewSet, 'interview')
router.register('answer', AnswerViewSet, 'answer')
router.register('question', QuestionViewSet, 'question')
router.register('possible-answer', PossibleAnswerViewSet, 'possible-answer')

urlpatterns = [
    *router.urls,
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
