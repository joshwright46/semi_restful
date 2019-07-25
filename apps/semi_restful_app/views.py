from django.shortcuts import render, redirect
from .models import Show
from .models import ShowManager
from django.contrib import messages

def shows(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request, 'shows.html', context)

def shows_new(request):
    return render(request,'shows_new.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key , value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], description=request.POST['description'])
        show = Show.objects.last()
        return redirect('/shows/'+ str(show.id))

def id(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request,'shows_id.html', context)

def edit(request, id):
    current_show = Show.objects.get(id=id)
    context = {
        'current_show': current_show
    }
    return render(request, 'shows_id_edit.html', context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    current_show = Show.objects.get(id=id)
    if len(errors) > 0:
        for key , value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+ str(current_show.id) +'/edit')

    else:
        current_show.title = request.POST['title']
        current_show.network = request.POST['network']
        current_show.release_date = request.POST['date']
        current_show.description = request.POST['description']
        current_show.save()
        return redirect('/shows/'+ str(current_show.id))

def destroy(request, id):
    delete_show = Show.objects.get(id=id)
    delete_show.delete()
    return redirect('/shows')