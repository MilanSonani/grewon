from .models import Events, EventUser


def busy_users(date_time):
    events = Events.objects.filter(start_date_time__lte=date_time, end_date_time__gte=date_time)
    users_in_events = EventUser.objects.filter(event__in=events).values_list('user', flat=True)
    return users_in_events
