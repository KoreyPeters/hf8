import pendulum
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from polium.models import Candidate, Election, Politician, PoliticianSurvey
from util.models import Activity


def polium_root(request):
    return render(request, "polium/root.html", locals())


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
    candidates = Candidate.objects.filter(election=election)
    return render(request, "polium/elections_detail.html", locals())


def politicians_list(request):
    politicians = Politician.objects.all()
    return render(request, "polium/politicians_list.html", locals())


def politicians_detail(request, sqid):
    politician = get_object_or_404(Politician, sqid=sqid)
    return render(request, "polium/politicians_detail.html", locals())


@login_required
def politicians_detail_survey(request, sqid):
    if request.method == "GET":
        politician = get_object_or_404(Politician, sqid=sqid)
        survey = PoliticianSurvey.objects.get_or_create(
            politician=politician,
            user=request.user,
        )
        # criteria =
        return render(request, "polium/politician_survey.html", locals())
    else:
        # Do this if the survey is complete.
        # activity = Activity.objects.create(
        #     kind=Activity.ActivityKind.POLIUM_POLITICIAN_SURVEY_COMPLETED,
        #     url=reverse("polium_politicians_detail", args=[sqid]),
        #     user=request.user,
        #     entity=sqid,
        #     last_updated_at=pendulum.now(),
        # )
        print(request)
        return
