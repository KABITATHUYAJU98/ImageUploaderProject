from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES) #rakhnai parxa
        if form.is_valid():#valid xa ki nai check garxa..
            #mathi bata ako form obj lai validate gareko
            form.save()
    form = ImageForm()#post request ahyo vane..matra valid check garne yeta wuti hunxa..natra sidhai khali form matra show garira hunxa
    img = Image.objects.all()
    return render(request,'myapp/home.html', {'img':img, 'form':form}) 
    # as a context form pass garem
    #img ko rup ma home.html ma janxa..aba..