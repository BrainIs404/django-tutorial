from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder" : "your title"}
        
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class" : "new-class-name two",
                "rows" : 20,
                "col" : 30,
                "id" : "actually-an-id",
            }
        )
    )
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("Not a valid title")
        else:
            return title

class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "your title"}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class" : "new-class-name two",
                "rows" : 20,
                "col" : 30,
                "id" : "actually-an-id",
            }
        )
    )
    price = forms.DecimalField()