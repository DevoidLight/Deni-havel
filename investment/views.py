from django.shortcuts import render, redirect
from django.urls import reverse
from .models import BusinessIdea
from .forms import IdeaCreateForm
from entrepreneurs.models import EntrepreneurProfile
from django.shortcuts import get_object_or_404
# Create your views here.

def ideas(request):
    business_ideas = BusinessIdea.objects.filter(status='published')
    return render(request, 'investment/ideas.html', {'ideas': business_ideas})

def my_ideas(request):
    business_ideas = BusinessIdea.objects.filter(author=request.user)
    return render(request, 'investment/ideas.html', {'ideas': business_ideas})

def idea(request, pk):
    idea = get_object_or_404(BusinessIdea, pk=pk)
    profile = get_object_or_404(EntrepreneurProfile, user=idea.author)
    return render(request, 'investment/idea.html', {'idea': idea, 'profile': profile})

def idea_delete(request, pk):
    idea = get_object_or_404(BusinessIdea, pk=pk)

    if request.method == 'POST':
        idea.delete()
        return redirect('investment:my_ideas')

    return render(request, 'investment/idea_delete.html', {'idea': idea})

def idea_create(request):
    if request.method == 'POST':
        form = IdeaCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            if 'publish' in request.POST:
                idea.status = 'published'
            idea.save()
            return redirect(reverse('investment:ideas'))
    else:
        form = IdeaCreateForm()
    return render(request, 'investment/idea_create.html', {'form': form})


def idea_edit(request, pk):
    idea = get_object_or_404(BusinessIdea, pk=pk)

    if request.method == 'POST':
        form = IdeaCreateForm(data=request.POST, files=request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save(commit=False)
            if 'draft' in request.POST:
                idea.status = 'draft'
            if 'publish' in request.POST:
                idea.status = 'published'
            idea.save()
            return redirect('investment:idea', pk=idea.pk)
    else:
        form = IdeaCreateForm(instance=idea)

    return render(request, 'investment/idea_edit.html', {'form': form, 'idea': idea})