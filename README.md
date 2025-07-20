# Django REST Images Example Project

- [Django REST Image Upload - ChatGPT - Shared](https://chatgpt.com/share/687ceccf-4874-8002-8ca5-7502007ba785)

## First Request

Provide the code for a Django REST app with a model `Image` that can store an image file. I don't need this to be in production. It is only needed to work locally to check a Python `requests` script I'm creating. The `Image` model does not need any other fields than the one to store the image.

I want to be able to use the URL of `"http://localhost/upload/"` to upload the files using my Python `requests` script. I do not yet need help with the upload via requests script.

## First Response

Here’s a minimal Django REST API setup for uploading images to a local-only endpoint at `http://localhost/upload/`.

---

### ✅ 1. Create Django Project and App

```bash
django-admin startproject image_uploader
cd image_uploader
python manage.py startapp images
```

---

### ✅ 2. Update `settings.py`

In `image_uploader/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'images',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

### ✅ 3. Define the `Image` model

In `images/models.py`:

```python
from django.db import models

class Image(models.Model):
    file = models.ImageField(upload_to='uploads/')
```

---

### ✅ 4. Create Serializer

In `images/serializers.py`:

```python
from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['file']
```

---

### ✅ 5. Create View

In `images/views.py`:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

### ✅ 6. URL Configuration

In `images/urls.py` (create this file):

```python
from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
]
```

In `image_uploader/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('images.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### ✅ 7. Run Migrations and Start Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Your upload endpoint is now available at:
📍 `http://localhost:8000/upload/`
(If you want `http://localhost/upload/`, add `--port 80` to your `runserver` command **with sudo on Linux**.)

---

Let me know if you want CORS support or to view uploaded images in a browser.

## Second Request

Provide the 'admin.py' so that I can view the objects there.

## Second Response

Here's a simple `admin.py` for your `images` app to register the `Image` model and show a thumbnail preview in the Django admin:

---

### ✅ `images/admin.py`

```python
from django.contrib import admin
from .models import Image
from django.utils.html import format_html

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'preview']

    def preview(self, obj):
        if obj.file:
            return format_html('<img src="{}" width="100" />', obj.file.url)
        return "-"
    preview.short_description = 'Preview'
```

---

### 📝 Notes:

* This adds a column to preview the uploaded image in the list view.
* Make sure you're serving media files by including this in `urls.py` (already shown in previous steps):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Once done, visit your admin panel (`http://localhost:8000/admin/`) and you'll see uploaded images with thumbnails. Let me know if you want to add filtering, search, or inline editing!

## Third Request

Provide a simple Python requests script to upload a single image to the endpoint. I want to test a simple script before I build my behemoth.

## Third Response

Here’s a **minimal working `requests` script** to upload a single image file to your local Django REST endpoint at `http://localhost:8000/upload/`:

---

### ✅ `upload_test.py`

```python
import requests

url = 'http://localhost:8000/upload/'

# Path to your local image file
file_path = 'test_image.jpg'

with open(file_path, 'rb') as image_file:
    files = {'file': image_file}
    response = requests.post(url, files=files)

print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
```

---

### 📝 Notes:

* Replace `'test_image.jpg'` with the path to a valid image file.
* This matches your `ImageSerializer` expecting a field named `file`.
* Assumes your Django server is running on port `8000`.

Let me know when you're ready to level up to your behemoth version—I’ll help you add features like metadata, headers, auth tokens, retry logic, etc.

