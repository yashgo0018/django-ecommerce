from django.shortcuts import render


# HTTP Error 404
def bad_request(request, exception):
    return render(
        request,
        '404.html',
        status=404
    )
