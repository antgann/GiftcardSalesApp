from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .models import EntryModel

from .forms import StoreNameForm
from .forms import GiftCardBalanceForm
from .forms import SellingPriceForm
from .forms import NetworkForm
from .forms import PostalAddressForm
from .forms import EmailAddressForm

def home_view(request):
    context ={}

    # create object of form
    form = StoreNameForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        fm = form.save()
        request.session['uniqueid'] = fm.id
        request.session['refreshed'] = "false"
        url = reverse('giftcardbalance-view')
        return HttpResponseRedirect(url)

    context['form']= form
    return render(request, "home.html", context)

def second_view(request, model_form, query_item_name, next_view):
    context ={}

    # create object of form
    form = model_form(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        q = EntryModel.objects.get(id=request.session['uniqueid'])
        setattr(q, query_item_name, form.cleaned_data[query_item_name])
        # save the form data to model
        q.save()
        request.session['refreshed'] = "false"
        return HttpResponseRedirect(reverse(next_view))
    if query_item_name == 'postal_address':
        context['google_maps_api_key'] = settings.GOOGLE_API_KEY
    context['form']= form
    if request.session['refreshed'] == "true" and not form.non_field_errors:
        request.session['uniqueid'] = ""
        return HttpResponseRedirect(reverse('home-view'))
    request.session['refreshed'] = "true"
    return render(request, "home.html", context)

def gift_card_balance_view(request):
    return second_view(request, GiftCardBalanceForm, 'gift_card_balance', 'sellingprice-view')

def selling_price_view(request):
    return second_view(request, SellingPriceForm, 'selling_price', 'network-view')

def network_view(request):
    return second_view(request, NetworkForm, 'network', 'postaladdress-view')

def postal_address_view(request):
    return second_view(request, PostalAddressForm, 'postal_address', 'emailaddress-view')

def email_address_view(request):
    return second_view(request, EmailAddressForm, 'email_address', 'thankyou-view')

def thank_you_view(request):
    return render(request, "thankyou.html")

def results_view(request):
    allentries= EntryModel.objects.all()
    return render(request, 'results.html', {'allentries': allentries})