from django.shortcuts import render, redirect, reverse

from blog.models import Post


def list_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})


def create_post(request):
    if request.POST:
        Post.objects.create(
            title=request.POST['title'],
            sub_title=request.POST['sub_title'],
            content=request.POST['content'],
            user=request.user
        )
        return render(request, 'blog/create.html', {'save': 'Salvo com sucesso'})
    return render(request, 'blog/create.html')


def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'blog/update.html', {'post': post})
    else:
        Post.objects.filter(pk=pk).update(
            title=request.POST['title'],
            sub_title=request.POST['sub_title'],
            content=request.POST['content'],
            user=request.user)
        return render(request, 'blog/update.html',
                      {'update_status': 'item atualizado', 'post': Post.objects.get(pk=pk)})


def delete_post(request, pk):
    if request.method == 'GET':
        Post.objects.get(pk=pk).delete()
    return redirect(reverse('list'))
