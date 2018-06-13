from django import forms
from .models import Category, Product, CustomerDetail


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ("Name", "Description")


class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=("Categories", "Name","Image","IDorSNO","Description","Price","NumbersAvailable")
		
		
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]
 
 
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CustomerDetailForm(forms.ModelForm):
	class Meta:
		model=CustomerDetail
		fields=("Name", "phonenumber", "Email", "PermanentAddress", "TemporaryAddress", "City", "State", "Landmark", "Pincode")



		
