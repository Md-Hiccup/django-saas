from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.core import serializers

from .forms import AddModuleForm, EditModuleForm
from .models import AddModule, EditModule


def menu():
    menu, sub_menu = '', ''
    menu = AddModule.objects.order_by('module_name')
    # menu_serial = serializers.serialize('json',menu)
    for i in menu:
        sub_menu = EditModule.objects.order_by('module_name')
        # sub_menu = EditModule.objects.filter(module_name_id = i.id).values('module_name__module_name', 'module_name__order_no', 'submodule_name')
    # sub_menu_serial = serializers.serialize('json', sub_menu)
    return { 'menu': menu, 'sub_menu': sub_menu}


def home(request):
    menus = menu()
    return render(request, 'moduleApp/home.html', {**menus} )


def create_module(request):
    menus = menu()
    if request.method == 'POST':
        form = AddModuleForm(request.POST)
        if form.is_valid():
            addform = form.save()
            mod = form.cleaned_data['module_name']
            addform.module_name = '-'.join(mod.split())
            addform.save()
            return redirect('home')
    else: 
        form = AddModuleForm()
    return render(request, 'moduleApp/create_module.html', { 'form': form, **menus  })


def edit_module(request):
    menus = menu()
    if request.method == 'POST':
        form = EditModuleForm(request.POST)
        if form.is_valid():
            editform = form.save()
            editform.save()
            return redirect('home')
    else: 
        form = EditModuleForm()
    return render(request, 'moduleApp/create_submodule.html', { 'form': form, **menus   })


def random_page(request):
    menus = menu()
    return render(request, 'moduleApp/random_page.html',  { **menus   })


def common_page(request, pk):
    menus = menu()
    if request.method == 'POST':
        print('inside post method of common page')
        
        ############ For  Module  Name  Checkbox ######################
        moduleData = AddModule.objects.filter(id = pk).values()
        modData = []
        modData.append(moduleData[0]['module_name'])

        moduleChkbox = request.POST.get('moduleChkbox', None)
        if moduleChkbox in modData :
            AddModule.objects.filter(id=pk).update(show=True)
        else:
            AddModule.objects.filter(id=pk).update(show=False)
            
        ############ For  Submodule  Name  Checkbox  ######################        
        data = EditModule.objects.filter(module_name_id = pk).values()
        if data:
            print('data: ', data)
            da = []
            dataList = {}
            for i in range(len(data)):
                # dataList.append(data[i]['submodule_name'])
                dataList[i] = {
                    'name': data[i]['submodule_name'],
                    'mid':  data[i]['id']
                }
                da.append(data[i]['submodule_name'])
            print('DataList: ', dataList)
            selectedChkbox = request.POST.getlist('optionsCheckboxes', None)
            print('selected Checkbox ', selectedChkbox)
            
            for k, v in dataList.items():
                print(v)
                if v['name'] in selectedChkbox :
                    print('if condition ', v['name'])
                    EditModule.objects.filter(id=v['mid']).update(show = True)
                else :
                    print('else condition ', v)
                    EditModule.objects.filter(id=v['mid']).update(show = False)
                
        return redirect('home')
        
    else:
        mod = AddModule.objects.filter(id = pk).values()
        modName = mod[0]['module_name']
        show = mod[0]['show']
        sendAttr = {**menus, 'modName': modName, 'show': show }
        data = EditModule.objects.filter(module_name_id = pk)
        if data:
            print('have data', modName, " ", data)
            sendAttr['data'] = data
    return render(request, 'moduleApp/common.html', sendAttr)
