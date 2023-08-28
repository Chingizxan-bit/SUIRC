from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AdvertsForm
from .models import Advertisement
# Create your views here.
def index(request):
 adverts = Advertisement.objects.all() 
 context = {'adverts': adverts}
 return render(request, 'app_FNAF/index.html', context)
 
def topSellers(request):
 return render(request,'app_FNAF/top-sellers.html')
   




 def AdvertsForm(request):
    if request.method == "POST":
        form=AdvetsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Adverts(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse ('main-page')
            return redirect(url)
    else:
        form=AdvetsForm()
    context = {'form' : form}
    return render(request, 'app_FNAF/advertisement-post.html', context)

