from django.shortcuts import render
from django.views import View
from .models import User, Events, EventUser
from .forms import FreeUsersForm
from .utils import busy_users


class CheckUserAvailibity(View):
    def get(self, request):
        form = FreeUsersForm()
        return render(request, 'free_users_form.html', {"form": form})

    def post(self, request):
        if request.method == 'POST':
            form = FreeUsersForm(request.POST)
        if form.is_valid():
            date_time = form.cleaned_data['date_time']
            
            users_in_events = busy_users(date_time)
            
            all_users = User.objects.all()
            available_users = all_users.exclude(id__in=users_in_events)
            available_users = User.objects.exclude(id__in=EventUser.objects.filter \
                (event__in=Events.objects.filter(start_date_time__lte=date_time, 
                            end_date_time__gte=date_time)).values_list('user', flat=True))
            availability = round((available_users.count() / all_users.count()) * 100)
            
            return render(request, 'results.html', {'available_users': available_users, 
            'availability': str(availability)+"%", 'date_time': date_time})