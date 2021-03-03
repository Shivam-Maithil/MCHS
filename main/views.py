from django.shortcuts import render, redirect, reverse
from .models import Result10th, Result12th, ResultYear, Teacher, StudentRegistration, Notice, EventPicture, Event
import random


def index(request):
    notice_queryset = Notice.objects.all()
    re10_querset = Result10th.objects.all()
    re12_querset = Result12th.objects.all()
    teachers_queryset = Teacher.objects.all()
    result_year = ResultYear.objects.all()[0]

    if request.method == "POST":
        name = request.POST["full-name"]
        number = request.POST["number"]
        city = request.POST["city"]

        student = StudentRegistration.objects.create(
            name=name, contact_number=number, city=city)
        student.save()
        return redirect(reverse('index'))

    context = {
        'all_notice': notice_queryset,
        'result10': re10_querset,
        'result12': re12_querset,
        'teachers': teachers_queryset,
        'result_year': result_year
    }
    return render(request, "index.html", context)


def random_color():
    colors = ['lightcoral', '#457b9d', '#81b29a', '#ee6c4d', '#9cafb7', '#4281a4', '#bcb8b1', '#e6b89c', '#a5a58d',
              '#02c39a', '#64a6bd', '#90be6d', '#bc4749', '#1fa6b8', '#3ec4d6', '#7c98b3', '#b36a5e', '#68e0c0', '#c5a158']
    return random.choice(colors)


def event(request):
    event_queryset = Event.objects.all().order_by('-timestamp')
    event_count = Event.objects.all().count()
    picture_queryset = EventPicture.objects.filter(featured=True)
    header_color = random_color()

    context = {
        'event': event_queryset,
        'event_count': event_count,
        'pictures': picture_queryset,
        'header_color': header_color
    }
    return render(request, 'activities.html', context)


def gallery(request, id):
    gallery_queryset = EventPicture.objects.filter(event_id=id)
    event_info_queryset = Event.objects.filter(id=id)
    header_color = random_color()

    context = {
        'pictures': gallery_queryset,
        'event_info': event_info_queryset,
        'header_color': header_color
    }
    return render(request, 'gallery.html', context)


def view_404(request, exception):
    return render(request, '404.html')
