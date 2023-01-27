from django import forms
from .models import Listings, ListingMedia


# This is the form to create a new listing
class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listings
        widgets = {
            "featured_image": forms.FileInput(
                attrs={
                    "enctype": "multipart/form-data"
                }
            ),
            # Hidden inputs are used by create.js to relay values
            "boat_feature_list": forms.HiddenInput(attrs={'required': 'false'}),  # noqa
            "type": forms.HiddenInput(),
            "condition": forms.HiddenInput(),
            "tax_paid": forms.HiddenInput(),
            "category": forms.HiddenInput(),
        }
        fields = "__all__"
        exclude = ("created_by", "created_on", "last_modified",
                   "listing_status", )


# This form edits listings & is the same as create except for no feaured_image
class ListingEditForm(forms.ModelForm):
    class Meta:
        model = Listings
        widgets = {
            "boat_feature_list": forms.HiddenInput(attrs={'required': 'false'}),  # noqa
            "type": forms.HiddenInput(),
            "condition": forms.HiddenInput(),
            "tax_paid": forms.HiddenInput(),
            "category": forms.HiddenInput(),
        }
        fields = "__all__"
        exclude = ("created_by", "created_on", "last_modified",
                   "featured_image",)


# This form is for the gallery images, not multiple attr is true
class ListingMediaForm(forms.ModelForm):
    class Meta:
        widgets = {
            "image": forms.ClearableFileInput(
                attrs={
                    "multiple": True
                }
            ),
        }
        model = ListingMedia
        fields = ['image']
