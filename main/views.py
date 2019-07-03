from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewOffer, ImageForm
from .models import Offer, Images


# Create your views here.

def home(response):
    if response.user.is_authenticated:
        name = response.user
    else:
        name = 'niezalogowany użytkowniku'
    return render(response, 'main/home.html', {"name":name})

def bye(response):
    name = response.user
    return render(response, 'main/bye.html', {"name":name})

def user_info(response):


    if response.user.is_authenticated:
        user = response.user

        if response.POST.get('edit'):
            user.username = response.POST.get('username')
            user.email = response.POST.get('email')
            user.first_name = response.POST.get('first_name')
            user.last_name = response.POST.get('last_name')

            user.save()

        return render(response, 'main/user_info.html', {"user": user})

    else:
        return render(response, 'main/notlogged.html', {})




def user_offs(response, name=None):
    if name == None:
        name = response.user
        return render(response, 'main/home.html', {"name": name})
    else:
        user = name
        li = []
        for offer in Offer.objects.all():
            b = '{}'.format(offer.user)
            if b == user:
                li += [offer]
        print(li)
        return render(response, 'main/user_offs.html', {"offers":li})


def create(response):
    if response.user.is_authenticated:

        ImageFormSet = modelformset_factory(Images,
                                            form=ImageForm, extra=2)

        if response.method == "POST":
            form = NewOffer(response.POST)
            formset = ImageFormSet(response.POST, response.FILES,
                                   queryset=Images.objects.none())

            if form.is_valid() and formset.is_valid():
                r = form.save(commit=False)
                r.user = response.user
                r.save()

                for form in formset.cleaned_data:
                    print(form)
                    if form:
                        image = form['image']
                        photo = Images(offer=r, image=image)
                        photo.save()

                return HttpResponseRedirect('/%i' % r.id)

            return render(response, 'main/create.html', {"form": form, "iform": formset})

        else:
            form = NewOffer
            formset = ImageFormSet(queryset=Images.objects.none())
            return render(response, 'main/create.html', {"form": form, "iform":formset})
    else:
        return render(response, 'main/notlogged.html', {})


def offer(response, id):
    offer = Offer.objects.get(id=id)
    img = offer.images_set.all()

    return render(response, 'main/offer.html', {"offer":offer, "images":img})

def search(response):
    list = Offer.objects.all()
    return render(response, 'main/search.html', {"list":list})

def your_offers(response, id=None):
    if response.user.is_authenticated:
        if id == None:
            offers = response.user.offer.all()
            print(list)
            return render(response, 'main/your_offers.html', {"offers": offers})
        else:

            offer = Offer.objects.get(id=id)
            img = offer.images_set.all()

            if response.method == 'POST':
                if response.POST.get('del'):
                    img.delete()
                    offer.delete()

                if response.POST.get('edit'):

                    return HttpResponseRedirect('/uoffer')

            return render(response, 'main/edit_offer.html', {"images":img, "offer":offer})
    else:
        return render(response, 'main/notlogged.html', {})





