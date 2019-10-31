from django.shortcuts import render

posts = [
    {
        'author':'Ishimwe',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'August 8, 2019',
    },
    {
        'author':'Moise',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'August 9, 2019',
    },
]

def pome(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/pome.html', context)

def abot(request):
    return render(request, 'blog/abot.html', {'title': 'abot' })
