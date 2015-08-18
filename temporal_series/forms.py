from django import forms


class SubmitTable(forms.Form):
    table_fd = forms.FileField(label='table_fp', required=True)
    table_timevar = forms.CharField(label='table_timevar', required=True)
    table_idVar = forms.CharField(label='table_idVar', required=True)

    ## For selection of the form parsing for the Dates
    TIMEPOINT_CHOICES = ((1, 'Date Timepoints'),
                         (0, 'Discrete Timepoints'))

    COMPLITION_METHODS = (('bfill', "Use Previous Field"),
                          ('ffill', "Use Next Field"),
                          ('inter', "Use Linear Interpolation"))

    na_complition = forms.ChoiceField(widget=forms.Select, choices=COMPLITION_METHODS)
    timepoint_type = forms.ChoiceField(widget=forms.Select, choices=TIMEPOINT_CHOICES)
