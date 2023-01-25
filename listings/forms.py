from django import forms
from .models import Listings, ListingMedia

class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listings
        widgets = {
            "featured_image": forms.FileInput(
                attrs={
                    "enctype": "multipart/form-data"
                }
            ),
            "boat_feature_list": forms.HiddenInput(attrs={'required': 'false'}),
            "type": forms.HiddenInput(),
            "condition": forms.HiddenInput(),
            "tax_paid": forms.HiddenInput(),
            "category": forms.HiddenInput(),
        }
        fields = "__all__"
        exclude = ("created_by", "created_on", "last_modified", "listing_status", )

class ListingEditForm(forms.ModelForm):
    class Meta:
        model = Listings
        widgets = {
            "boat_feature_list": forms.HiddenInput(attrs={'required': 'false'}),
            "type": forms.HiddenInput(),
            "condition": forms.HiddenInput(),
            "tax_paid": forms.HiddenInput(),
            "category": forms.HiddenInput(),
        }
        fields = "__all__"
        exclude = ("created_by", "created_on", "last_modified", "featured_image",)

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
