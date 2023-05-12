# import form class from django
from django import forms

from .models import EntryModel

# create a ModelForm

class StoreNameForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntryModel
        fields = ["store_name"]
        labels = {
            'store_name': "store name"
        }
class GiftCardBalanceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntryModel
        fields = ["gift_card_balance"]
        labels = {
            'gift_card_balance': "gift card balance"
        }
class SellingPriceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntryModel
        fields = ["selling_price"]
        labels = {
            'selling_price': "selling price"
        }
class NetworkForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntryModel
        fields = ["network"]
        labels = {
            'network': "network"
        }
    def clean(self):
        # Then call the clean() method of the super  class
        cleaned_data = super(NetworkForm, self).clean()
        network = cleaned_data.get("network")
        if network == EntryModel.NONE:
            del cleaned_data['network']
            raise forms.ValidationError("Please select a credit card network")
        # Finally, return the cleaned_data
        return cleaned_data

class PostalAddressForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntryModel
        fields = ["postal_address"]
        labels = {
            'network': "postal address"
        }
        widgets = {'postal_address': forms.TextInput(attrs={'size': 50}),}
class EmailAddressForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EntryModel
        fields = ["email_address"]
        labels = {
            'email_address': "email address"
        }