from django import forms
from .models import Listings, ListingMedia

class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ['make', 'model', 'price', 'tax_paid', 'condition', 'country', 'location', 'year_construction', 'length', 'beam', 'draft', 'weight', 'type', 'category', 'hull_material', 'fuel', 'number_of_engines', 'maximum_speed', 'cruising_speed', 'range', 'cabins', 'berths', 'heads', 'cabin_headroom', 'listing_excerpt', 'listing_description', 'boat_feature_list', 'featured_image']
 
class ListingMediaForm(forms.Form):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    model = ListingMedia
    fields = ['image']

