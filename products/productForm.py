from django.forms import ModelForm
from django import forms
from .models import Product


class ProductForm(ModelForm):
    class Meta:

        model = Product

        fields = ['title', 'bio', 'definition', 'price', 'count', 'delivery_price']


    def clean(self):

        super(ProductForm, self).clean()

        title = self.cleaned_data.get('title') 
        bio = self.cleaned_data.get('bio')
        text = self.cleaned_data.get('definition')
        price = self.cleaned_data.get('price')
        count = self.cleaned_data.get('count')
        delivery_price = self.cleaned_data.get('delivery_price')
        if not title:
            self._errors['title'] = self.error_class(['Complate the form'])
        elif len(title) > 30:
            self._errors['title'] = self.error_class(['Max lenght 30'])
        
        if not bio:
            self._errors['bio'] = self.error_class(['Complate the form'])
        elif len(bio) >50:
            self._errors['bio'] = self.error_class(['Max lenght 50'])
        
        if not text:
            self._errors['definition'] = self.error_class(['Complate the form'])

        if price < 0:
            self._errors['price'] = self.error_class(['Minimum value 0'])
        
        if count < 0:
            self._errors['count'] = self.error_class(['Minimum value 0'])

        if delivery_price < 0:
            self._errors['delivery_price'] = self.error_class(['Minimum value 0'])
        
        return self.cleaned_data



