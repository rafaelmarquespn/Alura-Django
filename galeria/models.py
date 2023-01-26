from django.db import models
from datetime import datetime
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA","nebulosa"),
        ("ESTRELA", "estrela"),
        ("GALAXIA", "galaxia"),
        ("PLANETA","planeta"),
    ]

    nome = models.CharField(max_length=100, null =False, blank=False)
    legenda = models.CharField(max_length=150, null =False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return f"Fotografia [nome={self.nome}]"