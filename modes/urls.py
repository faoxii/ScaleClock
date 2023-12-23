from .views import *
from django.urls import path

urlpatterns = [
    path('', index_test, name='index-test'),
    path("<str:mode_name>/", mode_general, name="mode-general"),
    path("<str:mode_name>/<str:tonality>", note_mode, name="note-mode"),
]
