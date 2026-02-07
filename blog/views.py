from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from blog.forms import CommentForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    featured_posts = Post.objects.filter(featured=True)
    # print(featured_posts)
    return render(request, "index.html", {'posts': posts, 'featured_posts': featured_posts})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def archive(request):
    categories = Category.objects.all()
    featured_posts = Post.objects.filter(featured=True)
    return render(request, "mainCategory.html", {'categories': categories,  'featured_posts': featured_posts})


def single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    featured_posts = Post.objects.filter(featured=True)
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "single.html", {'post': post, 'featured_posts': featured_posts, 'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def category(request, pk):
    categorySelected = Category.objects.get(pk=pk)
    print(categorySelected)
    posts = Post.objects.filter(categories=categorySelected)
    featured_posts = Post.objects.filter(featured=True)
    print(posts)
    return render(request, "archive.html", {'posts': posts, 'featured_posts': featured_posts})