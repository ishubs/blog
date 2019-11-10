from django.shortcuts import render, redirect
from blog.models import Post, emailid, images, Comments
from django.contrib import messages 
from django.views.generic.detail import DetailView
import random 
from blog.forms import emailidform, CommentsForm
def blog_index(request):
	posts = Post.objects.all().order_by('-created_on')
	
	
	
	if request.method == 'POST':

		form=emailidform(request.POST or None)
		if form.is_valid():
			form.save()
			
			messages.success(request, f'Subscribed  ! ')
			return redirect('blog_index')
	else:
		form = emailidform()

	context = {
		"posts": posts,
		"form": form,
		
	}
		

	return render(request,"blog_index.html", context)



def blog_category(request, category):

	posts = Post.objects.all().order_by('-created_on')
	context = {
		"category" : category,
		"posts" : posts,
	}
	return render(render, 'blog_category.html', context)



def blog_detail(request, pk):
	post = Post.objects.get(pk=pk)
	posts = Post.objects.all().order_by('-created_on')
	

	#comments

	form = CommentsForm()
	if request.method == 'POST':
		form = CommentsForm(request.POST)
		if form.is_valid():
			comment = Comments(
					author=form.cleaned_data["author"],
					body=form.cleaned_data["body"],
					post=post
			)
			comment.save()
			return redirect('blog_index')

	comments = Comments.objects.filter(post=post)




	
	context = {
		"post": post,
		"list" : posts[:3],
		"comments": comments,
		"form": form


		
	}
	return render(request, "blog_detail.html", context)


