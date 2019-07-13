from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .forms import NewOffer, ImageForm, SearchOff
from .models import Offer, Images
from .models import Category, CarMark, Stan, Status, Type, Fuel, GearBox, Naped
from .choices import *


# Create your views here.

def home(response):
    if response.user.is_authenticated:
        name = response.user
    else:
        name = 'niezalogowany użytkowniku'

    list = Offer.objects.order_by('created_at')
    offers = list.reverse()[:6]

    for offer in offers:
        print(offer.images_set.all())

    i = 1

    return render(response, 'main/home.html', {"name":name, "offers":offers, "i":i})

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

        offers = Offer.objects.all()

        name = response.user
        return render(response, 'main/user_offs.html', {"offers": offers})

    else:
        user = name
        li = []
        for offer in Offer.objects.all():
            b = '{}'.format(offer.user)
            if b == user:
                li += [offer]
        print(li)

        return render(response, 'main/user_offs.html', {"offers":li, "user":user, "response":response})


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

            return render(response, 'main/create.html', {"form": form,
                                                         "iform": formset,
                                                         })

        else:
            form = NewOffer
            formset = ImageFormSet(queryset=Images.objects.none())
            return render(response, 'main/create.html', {"form": form,
                                                         "iform":formset,
                                                         })
    else:
        return render(response, 'main/notlogged.html', {})


def offer(response, id):
    offer = Offer.objects.get(id=id)
    img = offer.images_set.all()

    print(img)



    return render(response, 'main/offer.html', {"offer":offer,
                                                "images":img,

                                                })



def search(response):


    list = Offer.objects.order_by('price')
    marka = []

    if response.method == "GET":
        form = SearchOff(response.GET)

        if response.GET.get('search'):



            category = response.GET.get('category')
            if category:
                category = [Category.objects.get(id=i) for i in category]
                list = list.filter(category__in=category)

            marka = response.GET.get('marka')
            if marka:
                marka = [CarMark.objects.get(id=i) for i in marka]
                list = list.filter(marka__in=marka)

            model = response.GET.get('model')
            if model:
                list = list.filter(model__icontains=model)

            type = response.GET.getlist('type')
            if len(type) != 0:
                itype = [TYPE[int(type[i])-1][1] for i in range(len(type))]
                if itype:
                    list = list.filter(type__in=itype)

            stan = response.GET.getlist('stan')
            if len(stan) != 0:
                istan = [STAN[int(stan[i]) - 1][1] for i in range(len(stan))]
                if istan:
                    list = list.filter(stan__in=istan)

            min_prod = response.GET.get('prod_year_min')
            if min_prod:
                list = list.filter(prod_year__gte=min_prod)

            max_prod = response.GET.get('prod_year_max')
            if max_prod:
                list = list.filter(prod_year__lte=max_prod)

            min_mileage = response.GET.get('mileage_min')
            if min_mileage:
                list = list.filter(mileage__gte=min_mileage)

            max_mileage = response.GET.get('mileage_max')
            if max_mileage:
                list = list.filter(mileage__lte=max_mileage)

            min_cap = response.GET.get('cap_min')
            if min_cap:
                list = list.filter(cap__gte=min_cap)

            max_cap = response.GET.get('cap_max')
            if max_cap:
                list = list.filter(cap__lte=max_cap)

            fuel = response.GET.getlist('fuel')
            if len(fuel) != 0:
                ifuel = [FUEL[int(fuel[i])-1][1] for i in range(len(fuel))]
                print(ifuel)
                if ifuel:
                    list = list.filter(fuel__in=ifuel)

            price_min = response.GET.get('price_min')
            if price_min:
                list = list.filter(price__gte=price_min)

            price_max = response.GET.get('price_max')
            if price_max:
                list = list.filter(price__lte=price_max)



            return render(response, 'main/search.html', {"list": list, "form": form})


    else:
        form = SearchOff

    return render(response, 'main/search.html', {"list": list, "form": form})



def edit_offer(response, id=None):
    if response.user.is_authenticated:


        offer = Offer.objects.get(id=id)
        if offer.user == response.user:
            img = offer.images_set.all()

            if response.method == 'POST':
                if response.POST.get('del'):
                    img.delete()
                    offer.delete()


            return render(response, 'main/edit_offer.html', {"images":img, "offer":offer})

        else:
            return render(response, 'main/notlogged.html', {})


    else:
        return render(response, 'main/notlogged.html', {})





