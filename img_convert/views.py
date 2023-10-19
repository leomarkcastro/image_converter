from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .services.file_convert import convert
from django.http import HttpResponse
from django.core.files import File
import os


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']

        fs = FileSystemStorage(
            location="./converted_images"
        )
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        # get file location in server
        file_location = fs.path(filename)
        jpg_to_png = file_location.replace(".jpg", ".png")
        convert(file_location, jpg_to_png)

        # get png file url
        uploaded_file_url = fs.url(jpg_to_png)

        # return render(request, 'core/index.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })

        # send file back to client via http response

        with open(jpg_to_png, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/png")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(jpg_to_png)
            return response

    return render(request, 'core/index.html')
