from .views import *
from django.urls import path

urlpatterns = [
    path('', index_test, name='index'),
    path("<str:mode_name>/", mode_general, name="mode-general"),
    path("<str:mode_name>/<str:tonality>", note_mode, name="note-mode"),
    path("scales", scales_page , name="scales"),
    path("chords", chords_page , name="chords"),
    path("lessons", lessons_page , name="lessons"),
    path("about", about_page , name="about"),
]
