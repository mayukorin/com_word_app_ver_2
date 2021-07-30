from . import views
from django.urls import path

app_name = "com_word_app"
urlpatterns = [
    path("analyze/execute", views.SentenceAnalyzeView.as_view())
]
