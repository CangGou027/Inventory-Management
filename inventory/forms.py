from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': '产品名称',
            'category': '产品类别',
            'quantity': '库存数量',
            'production_date': '生产日期',
            'image': '产品图片'
        }
        exclude = ['owner', 'created_at']
        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False  # 允许更新时不修改图片