from django.db import models

# Create your models here.
class Serializers(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome