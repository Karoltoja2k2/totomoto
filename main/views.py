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
    user = response.user
    print(user)
    return render(response, 'main/user_info.html', {"user":user})

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
            list = response.user.offer.all()
            print(list)
            return render(response, 'main/your_offers.html', {"list": list})
        else:
            offer = Offer.objects.get(id=id)
            img = offer.images_set.all()
            return render(response, 'main/edit_offer.html', {"offer":offer, "images":img})
    else:
        return render(response, 'main/notlogged.html', {})





