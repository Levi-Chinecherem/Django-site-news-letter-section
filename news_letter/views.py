from django.shortcuts import render
from .forms import News_Letter_Form

# Create your views here.
def news_letter_view(request):
    form = News_Letter_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = News_Letter_Form()
    context={
        'form' : form
    }
    return render(request, 'news_letter/index.html', context)