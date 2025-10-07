from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog , category
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

@login_required
def create_blog(request):
    if not hasattr(request.user, 'profile') or request.user.profile.user_type != 'doctor':
        return redirect('dashboard')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user.profile  # ✅ Fix: Assign Profile, not User
            blog.save()
            return redirect('doctor_blogs')
    else:
        form = BlogForm()

    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def doctor_blogs(request):
    if not hasattr(request.user, 'profile'):
        return redirect('dashboard')  # or handle missing profile
    
    blogs = Blog.objects.filter(author=request.user.profile)  # ✅ Fix here
    return render(request, 'blog/doctor_blogs.html', {'blogs': blogs})


@login_required
def patient_blogs(request):
    categories = category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        blogs = Blog.objects.filter(is_draft=False, category_id=category_id)
    else:
        blogs = Blog.objects.filter(is_draft=False)
    return render(request, 'blog/patient_blogs.html', {
        'categories': categories,
        'blogs': blogs,
    })
