from django.shortcuts import render, get_object_or_404
from .models import Mode
from django.template.loader import get_template, TemplateDoesNotExist
from django.http import Http404


# Create your views here.

def index_test(request):
    return render(request, 'header/index.html')
    
    
def scales_page(request):
    return render(request, 'header/scales.html')    

def chords_page(request):
    return render(request, 'header/chords.html')

def lessons_page(request):
    return render(request, 'header/lessons.html')

def about_page(request):
    return render(request, 'header/about.html')

    
    
    
def mode_general(request, mode_name):
    template_path = f'gammes/{mode_name.lower()}.html'

    try:
        get_template(template_path)
    except TemplateDoesNotExist :
        raise Http404("Mode not found")

    return render(request, template_path)

def note_mode(request, mode_name, tonality):
    mode = get_object_or_404(Mode, mode_name=mode_name, tonality=tonality)
    return render(request, 'test.html', {'modes': mode})

        
        
