from django.shortcuts import render
from .forms import NewForm
# Create your views here.


def index(request):
    alpha = {'A':'4', 'H':'#', 'k':'!<', 'K':'!<', 'S':'$', 'z':'2', 'Z':'2', 'Y':'`/', 'U':'(_)', 'D':'[)', 'O':'()',
             'B':'ß','C':'(','L':'!_','x':'><','t':'+','E':'£','Ṯ':'+','s':'5','a':'@','v':'\/','V':'\/','i':'ï','o':'ø',
             'b':'þ'}
    rev = {}
    for i in range(26):
        rev[chr(97+i)] = chr(122-i)
    data = ''
    def l1(text):
        temp = ''
        def replace_index(text, index=0, replacement=''):
            return '%s%s%s' % (text[:index], replacement, text[index + 1:])
        for i in range(len(text)):
            if (ord(text[i])>64 and ord(text[i])<91) or (ord(text[i])>96 and ord(text[i])<123):
                if text[i].islower():
                    text = replace_index(text,i,rev[text[i]])
                else:
                    text = replace_index(text, i, rev[text[i].lower()].upper())
        return text
    def symbol(text):
        for i in range(len(text)):
            try:
                text = text.replace(text[i],alpha[text[i]])
            except:
                pass
        return text
    if request.method == "POST":
        form = NewForm(request.POST)
        text = ""
        if form.is_valid():
            text = str(form.cleaned_data['text'])
            choice = str(form.cleaned_data['choice'])
            if choice == 'char':
                data = l1(text)
            else:
                data = symbol(text)
        return render(request,'app/index.html',{'data': data, 'form': form})
    else:
        form = NewForm()
    return render(request,'app/index.html',{'data': data, 'form': form})
