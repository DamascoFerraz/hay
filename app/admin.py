from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(freqQuestionario)
admin.site.register(questionario) 
admin.site.register(tipoPergunta)
# pergunta>inline (line 20)
admin.site.register(funcao)
admin.site.register(usuario)
admin.site.register(resposta)
admin.site.register(questionarioPergunta)

class questionarioPerguntaInline(admin.StackedInline):
    model = questionarioPergunta
    extra = 1

class perguntaAdmin(admin.ModelAdmin):
    inlines = [questionarioPerguntaInline]

admin.site.register(pergunta, perguntaAdmin)