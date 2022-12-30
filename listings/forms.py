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
        }
        fields = "__all__"
        exclude = ("created_by", "created_on", "last_modified",)

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

