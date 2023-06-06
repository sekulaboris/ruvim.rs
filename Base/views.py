from django.shortcuts import render, get_object_or_404
from .models import Onama
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .form import SearchForm
from Blog.models import Post
from django.contrib.postgres.search import TrigramSimilarity


def base_onama(request):
    onamas=Onama.published.all()
    return render(request,
                'base.html',
                {'onamas':onamas})

def onama(request):
    onamas=Onama.published.all()
    return render(request,
                    'onama.html',
                    {'onamas':onamas})


#---------------------------search polje---------------------------

def search(request):
    form=SearchForm()
    query=None
    results=[]
    if 'query' in request.GET:
        form=SearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data['query']
            search_vector=SearchVector('title',weight='A')+\
                          SearchVector('body', weight='B')
            search_query=SearchQuery(query)
            results=Post.published.annotate(
                similarity=TrigramSimilarity('title', query),
                rank=SearchRank(search_vector,search_query)
            ).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request,
                    'search.html',
                    {'form':form,
                    'query':query,
                    'results':results})

