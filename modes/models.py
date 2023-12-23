from django.db import models
from django.urls import reverse

# Create your models here.

class Mode(models.Model):
    mode_name = models.CharField(max_length=255)
    tonality = models.CharField(max_length=2)
    note_1 = models.CharField(max_length=3)
    note_2 = models.CharField(max_length=3)
    note_3 = models.CharField(max_length=3)
    note_4 = models.CharField(max_length=3)
    note_5 = models.CharField(max_length=3)
    note_6 = models.CharField(max_length=3)
    note_7 = models.CharField(max_length=3)


    def __str__(self):
        return f"{self.mode_name} in {self.tonality}"

    def get_absolute_url(self):
        return reverse("note-mode", kwargs={"tonality": self.tonality,"mode_name": self.mode_name})
    