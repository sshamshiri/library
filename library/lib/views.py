from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class Index (generic.TemplateView):
    template_name = "lib/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['num_books'] = models.Book.objects.all().count()
        context ['num_instances'] = models.BookInstance.objects.all().count()
        context ['num_instances_available'] = models.BookInstance.objects.filter(status__exact='a').count()   
        context ['num_authors'] = models.Author.objects.count()
        return context
