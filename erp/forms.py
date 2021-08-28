from django.forms import *
from erp.models import Category

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():      #Optimización de Código para evitar duplicación de código
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete '] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        #labels = {
        #    'name': 'Nombre',
        #    'desc': 'Descripción'
        #}

        widgets = {                # Dar propiedades al código 
            'name': TextInput(
                attrs={
                    #'class': 'form-control',
                    #'autocomplete': 'off',
                    'placeholder': 'Ingrese un nombre',
                }
            ),
           'desc': Textarea(
                attrs={
                    #'class': 'form-control',
                    #'autocomplete': 'off',
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3,
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
        