from django import forms
from django.core.validators import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_product', 'category', 'price']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['image_product'].widget.attrs.update({
            'class': 'form-control-file'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Выберите категорию'
        })


    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price


    def clean_image_product(self):
        image_product = self.cleaned_data.get('image_product')
        if not image_product:
            raise ValidationError("Пожалуйста, выберите файл для загрузки.")

        valid_extensions = ['jpeg', 'png']
        ext = image_product.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise ValidationError(f"Неподдерживаемый формат. Разрешены только: {', '.join(valid_extensions)}.")

        max_size_mb = 5
        if image_product.size > max_size_mb * 1024 * 1024:
            raise ValidationError(f"Размер файла не должен превышать {max_size_mb} МБ.")

        return image_product


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if name.lower() in forbidden_words:
            self.add_error('name', 'Нельзя использовать запрещенное слова в наименование')
        elif description.lower() in forbidden_words:
            self.add_error('description', 'Нельзя использовать запрещенное слова в описание')
