from django.shortcuts import render
from django.http import HttpResponseRedirect

def feed(request):
    context = {
        'posts' : [
            {'author' : 'Jao', 'date': '01/02/2024', 'content' : 'sisu, vc me paga'},
            {'author' : 'Fernando', 'date': '31/01/2024', 'content' : 'eita, nois'},
            {'author' : 'Alecia', 'date': '01/02/2024', 'content' : 'kkk juro'}
        ]
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        print(author)
        print(content)
        return HttpResponseRedirect("/feed")
    else:
        return render(request, 'publicate.html')
