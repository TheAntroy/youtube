from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
    data = [
        {
            "id": 1,
            "title": "Electronics",
            "image": "https://cdn.tailkit.com/media/placeholders/photo-PDX_a_82obo-700x700.jpg",
        },
        {
            "id": 2,
            "title": "Computers",
            "image": "https://cdn.tailkit.com/media/placeholders/photo-1SAnrIxw5OY-700x700.jpg",
        },
        {
            "id": 3,
            "title": "Clothes",
            "image": "https://cdn.tailkit.com/media/placeholders/photo-gUPiTDBdRe4-700x700.jpg",
        },
        {
            "id": 4,
            "title": "Smart Home",
            "image": "https://cdn.tailkit.com/media/placeholders/photo-ALpEkP29Eys-700x700.jpg",
        },
        {
            "id": 5,
            "title": "Shoes",
            "image": "https://cdn.tailkit.com/media/placeholders/photo-164_6wVEHfI-700x700.jpg",
        },
        {
            "id": 6,
            "title": "Wearables",
            "image": "https://cdn.tailkit.com/media/placeholders/photo-wW7XbWYoqK8-700x700.jpg",
        },
    ]
    page = request.GET.get("page")
    results = 3
    paginator = Paginator(data, results)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        data = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        data = paginator.page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        "data": data,
        "custom_range": custom_range,
    }
    return render(request, "myapp/index.html", context)
