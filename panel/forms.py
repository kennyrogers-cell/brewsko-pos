from django import forms
from accounts.models import User
from .models import MenuItem, InventoryItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = [
            'name',
            'price',
            'category',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
            'price': forms.NumberInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100', 'step': '0.01'}),
            'category': forms.Select(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
            'status': forms.Select(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
            'has_serving_style': forms.CheckboxInput(attrs={'class': 'h-4 w-4 rounded border-slate-600 text-orange-500'}),
            'has_size': forms.CheckboxInput(attrs={'class': 'h-4 w-4 rounded border-slate-600 text-orange-500'}),
            'has_temperature': forms.CheckboxInput(attrs={'class': 'h-4 w-4 rounded border-slate-600 text-orange-500'}),
        }


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'stock', 'unit', 'min_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
            'stock': forms.NumberInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100', 'step': '0.01'}),
            'unit': forms.Select(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
            'min_level': forms.NumberInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100', 'step': '0.01'}),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
        required=False,
        help_text='Leave blank to keep current password.',
    )

    class Meta:
        model = User
        fields = ['username', 'role', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
            'role': forms.Select(attrs={'class': 'w-full rounded-lg border border-slate-700 bg-slate-900 px-4 py-2 text-slate-100'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
