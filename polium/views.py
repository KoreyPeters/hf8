from django.shortcuts import get_object_or_404, render

from polium.models import Candidate, Election, Politician


def candidates_list(request):
    candidates = Candidate.objects.all()
    return render(request, "polium/candidates_list.html", locals())

def candidates_detail(request, sqid):
    candidate = get_object_or_404(Candidate, sqid=sqid)
    return render(request, "polium/candidates_detail.html", locals())

def elections_list(request):
    elections = Election.objects.all()
    return render(request, "polium/elections_list.html", locals())

def elections_detail(request, sqid):
    election = get_object_or_404(Election, sqid=sqid)
    return render(request, "polium/elections_detail.html", locals())

def politicians_list(request):
    politicians = Politician.objects.all()
    return render(request, "polium/politicians_list.html", locals())

def politicians_detail(request, sqid):
    politician = get_object_or_404(Politician, sqid=sqid)
    return render(request, "polium/politicians_detail.html", locals())