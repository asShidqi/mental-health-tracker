from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306230395',
        'name': 'Muhammad Fayyed As Shidqi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)