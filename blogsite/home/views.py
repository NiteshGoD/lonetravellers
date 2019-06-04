# from django.shortcuts import render
#
# # Create your views here.
# def index(request):
#     return render(request,'home/index.html',{})


from django.shortcuts import render
from .models import Project,Comment
from .forms import CommentForm
# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request,'project_index.html',context)

def project_detail(request,pk):
    project = Project.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form. cleaned_data['body'],
                project = project
            )
            comment.save()
    comments = Comment.objects.filter(project=project)
    context = {
        "project":project,
        "comments":comments,
        "form":form

    }
    return render(request,'project_detail.html', context)
