from django.shortcuts import render

def index(request):
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1

    context = {
        'num_visitas': num_visitas,
        'nav': '',
        'listname': 'Home'
    }

    return render(request, 'index.html', context=context)