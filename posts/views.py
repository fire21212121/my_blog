from django.shortcuts import render, redirect
from posts.models import Post, Category
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
    category_data = request.GET.get("category_form")
    # print(category_data)
    if category_data == None or category_data == "0":
        values = Post.objects.all()
    else:
        values = Post.objects.filter(category=category_data)
    date_sort_date = request.GET.get("date_sort_form")
    if date_sort_date == "new":
        values = values.order_by("-datetime_created")
    else:
        values = values.order_by("datetime_created")
    categories = Category.objects.all()
    if category_data:
        category_data =  int(category_data)
    return render(request, 'index.html', {'posts':values, "categories":categories, "selected_category":category_data, "selected_data_sort":date_sort_date})

def post(request):
    if request.method == "POST":
        print(request.POST)
        header_data = request.POST.get("header_form")
        text_data = request.POST.get("text_form")
        category_data = request.POST.get("category_form")
        category = Category.objects.get(id=category_data)
        file_data = request.FILES.get("file_form")
        if header_data and text_data:
            Post.objects.create(header=header_data, text=text_data, category=category, image=file_data)
            return redirect("index")
    categories = Category.objects.all()
    return render(request, 'post.html', {"categories":categories})
