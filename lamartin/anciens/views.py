from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from .models import Ancien, AncienForm
# Create your views here.

@login_required
def anciens(request):
    anciens_list = Ancien.objects.order_by('promo')
    has_created = Ancien.objects.filter(user=request.user).exists()
    context = {
        "anciens_list" : anciens_list,
        "has_created" : has_created
    }
    return render(request, "anciens/index.html", context)

@login_required
def ancien(request, ancien_id):
    ancien = get_object_or_404(Ancien, pk=ancien_id)

    return render(request, "anciens/detail.html", {"ancien": ancien})

@login_required
def create(request):
    try:
        form = AncienForm(request.POST)
        if form.is_valid() and not Ancien.objects.filter(user=request.user).exists():
            new = form.save()
            new.user = request.user
            new.save()
            return redirect("/")
    except:
        return redirect("/")
    return redirect("/")

@login_required
def edit_ancien(request, ancien_id):
    entry = get_object_or_404(Ancien, pk=ancien_id)
    if request.method != "POST":
        form = AncienForm(instance=entry)
        return HttpResponse(form.as_p())
    else:
        form = AncienForm(instance=entry, data=request.POST)
        if form.is_valid() and (request.user == entry.user or request.user.is_superuser):
            form.save()
            return HttpResponseRedirect(f"/{ancien_id}")
        return HttpResponseRedirect(f"/{ancien_id}")