from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def numbered_boxes(request):
    return render(request, 'numbered_boxes.html')