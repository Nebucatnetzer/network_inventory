from django.http import Http404


def superuser_required(old_function):
    def new_function(request, *args, **kwargs):
        if request.user.is_superuser:
            return old_function(request)
        else:
            raise Http404
    return new_function
