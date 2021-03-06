from django.shortcuts import render
from filepicker.forms import TestModelForm


def view(request):
    message = None
    if request.method == "POST":
        print "POST parameters: ", request.POST
        print "Files: ", request.FILES

        #building the form - automagically turns the uploaded fpurl into a File object
        form = TestModelForm(request.POST, request.FILES)
        if form.is_valid():
            #Save will read the data and upload it to the location defined in TestModel
            form.save()

            #Reading the contents of the file
            fpfile = form.cleaned_data['fpfile']
            #Since we already read from it in save(), we'll want to seek to the beginning first
            fpfile.seek(0)
            print fpfile.read()

            message = "Save successful. URL for %s: %s" % (fpfile.name, request.POST['fpfile'])
        else:
            message = "Invalid form"
    else:
        form = TestModelForm()

    return render(request, "filepicker.html", {'form': form, 'message': message})


def test(request):
    return render(request, "test.html")


def widget(request):
    return render(request, "widget.html")