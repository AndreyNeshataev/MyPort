from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


class DateForm(forms.Form):
    date_start = forms.DateField(widget=DatePickerInput(),
                                 label='Начальная дата')
    end_time = forms.DateField(widget=DatePickerInput(),
                               label='Конечная дата')
