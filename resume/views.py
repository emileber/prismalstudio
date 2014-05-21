#from django.shortcuts import render
from django.views import generic

from resume.models import LifeOccupation

# Create your views here.



class IndexView(generic.ListView):
    template_name = 'resume/index.html'
    context_object_name = 'latest_occupation_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return LifeOccupation.objects.order_by('-finished_date', '-start_date')