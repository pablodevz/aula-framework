from django.contrib import admin
from .models import Post
from .models import Pessoa, Endereco

admin.site.register(Post)
admin.site.register(Pessoa)
admin.site.register(Endereco)