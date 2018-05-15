from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import Image
from .form import ImageForm
import os

@login_required(login_url='/account/login')
@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            # print(456)
            new_item = form.save(commit=False)
            # print(789)
            new_item.user = request.user
            new_item.save()
            return JsonResponse({'status':"1"})
        except:
            # print(123)
            return JsonResponse({'status':"0"})

@login_required(login_url='/account/login/')
def list_images(request):
    images = Image.objects.filter(user=request.user)

    paginator = Paginator(images,5) #创建Paginator对象，第二个数值是这一页最大图片数量
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page) #page方法用于获取page页面的内容
        images = current_page.object_list #object_list属性 返回页面内容的列表
    except PageNotAnInteger:
        current_page = paginator.page(1)
        images = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages) #num_pages获取最大的页数
        images = current_page.object_list

    # return render(request, 'image/list_images.html', {"images":images,"page":current_page})
    return render(request, 'image/list_images.html', {"images": images, "page": paginator})

@login_required(login_url='/accout/login/')
@require_POST
@csrf_exempt
def del_image(request):
    image_id = request.POST['image_id']
    image_url = request.POST['image_url']
    print(image_url)
    try:
        os.remove(image_url)
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({"status":"1"})
    except:
        return JsonResponse({"status":"2"})


def falls_images(request):
    images = Image.objects.all()
    return render(request, 'image/falls_image.html',{"images":images})
