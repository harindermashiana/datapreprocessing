from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect,HttpResponse
from .form import FileFieldForm, edit, delc
from django.shortcuts import render
from .models import Document
import pandas as pd
import numpy as np
# Create your views here.
list1=[]
X=[]
class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'base.html'  # Replace with your template.
   # success_url = 'moreorless' # Replace with your URL or reverse().
    files = []
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files=request.FILES.getlist('file_field')

        if form.is_valid():
            file = Document(file_field=request.FILES['file_field'])
            file.description='fill'
            print(file.file_field.path)
            for f in files:

             file.save()
            print('reached')
            dataset = pd.read_csv(file.file_field.path)
            print(type(dataset.iloc[:, :-1].values))
            X.append(dataset.iloc[:, :-1].values)

            viewing2(request)
            return HttpResponseRedirect('/dataprocessing/view')
        else:
            return self.form_invalid(form)

class editable(FormView):
    form_class = edit
    template_name = 'edit.html'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()

        form = edit(request.POST)
        if form.is_valid():
            dum=form.cleaned_data['dummy']
            dumdum=int(dum)
            y=X[0]
            print(type(y))
            from sklearn.preprocessing import LabelEncoder, OneHotEncoder
            from sklearn.preprocessing import Imputer
            #imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
            #imputer = imputer.fit(y[:, 1:3])
            #y[:, 1:3] = imputer.transform(y[:, 1:3])
            labelencoder_X = LabelEncoder()
            y[:, dumdum] = labelencoder_X.fit_transform(y[:, dumdum])
            onehotencoder = OneHotEncoder(categorical_features=[dumdum])
            y = onehotencoder.fit_transform(y).toarray()
            X.insert(0,y)
            return HttpResponseRedirect('/dataprocessing/view/')
def viewing2(request):





    return render(request, "view.html", {'word':X})

class columnn(FormView):
    form_class = delc
    template_name = 'columnremoval.html'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()

        form = delc(request.POST)

        if form.is_valid():
            y=X[0]
            dum=form.cleaned_data['delc1']
            delv=int(dum)
            y=np.delete(y,delv,1)
            X.insert(0,y)
        return HttpResponseRedirect('/dataprocessing/view/')

