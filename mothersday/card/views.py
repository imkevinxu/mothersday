from django.shortcuts import render, redirect
from .models import Card

# Create your views here.

def app(request, phone):
    if phone:
        try:
            card = Card.objects.get(phone=str(phone))
            return render(request, "app.html", {"card": card})
        except:
            pass
    return redirect("/app")


def create(request):
    if request.method == 'POST':
        try:
            card = Card.objects.get(phone=''.join(c for c in request.POST["phone"] if c.isdigit()))
            if request.POST["name"]:
                card.name = request.POST["name"]
                card.save()
            return redirect("/mothersday/%s" % card.phone)
        except:
            pass
    return redirect("/")
