from django.shortcuts import render, get_object_or_404
from .models import Mode
from django.template.loader import get_template, TemplateDoesNotExist
from django.http import Http404


# Create your views here.

def svg_text(request, mode_name, tonality):
    mode = get_object_or_404(Mode, mode_name=mode_name, tonality=tonality)
    return render(request, 'svg_test.html', {'modes': mode})


def index_test(request):
    mode = Mode.objects.all()
    return render(request, 'index.html', {'modes': mode})
    
    
def mode_general(request, mode_name):
    template_path = f'modes/{mode_name.lower()}.html'

    try:
        get_template(template_path)
    except TemplateDoesNotExist :
        raise Http404("Mode not found")

    return render(request, template_path)

def note_mode(request, mode_name, tonality):
    mode = get_object_or_404(Mode, mode_name=mode_name, tonality=tonality)
    return render(request, 'test_mode.html', {'modes': mode})

        
        
