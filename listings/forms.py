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
            "boat_feature_list": forms.HiddenInput(attrs={'required': 'false' }),
            "type": forms.HiddenInput(),
            "condition": forms.HiddenInput(),
            "tax_paid": forms.HiddenInput(),
        }
        test = forms.FloatField( widget=forms.HiddenInput(attrs={'id':'some-custom-test-id'}))
        fields = "__all__"
        exclude = ("created_by", "created_on", "last_modified", "listing_status", )

class ListingMediaForm(forms.ModelForm):
    class Meta:
        # image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        widgets = {
            "image": forms.ClearableFileInput(
                attrs={
                    "multiple": True
                }
            ),
        }
        model = ListingMedia
        fields = ['image']