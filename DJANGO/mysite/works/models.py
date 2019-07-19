from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

class Categoria(models.Model):
    titolo_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.titolo_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'

class Fase(models.Model):
    titolo_fase = models.CharField(max_length=200)

    def __str__(self):
        return self.titolo_fase

    class Meta:
        verbose_name = 'Fase'
        verbose_name_plural = 'Fasi'

class Lavoro(models.Model):
    titolo = models.CharField(max_length=100)
    oggetto = models.CharField(max_length=400)
    importo = models.DecimalField(decimal_places=2, max_digits=10)
    data_lavoro = models.DateField(("Data lavori"), default=datetime.date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo + " - " + self.oggetto + " - " + str(self.importo)

    class Meta:
        verbose_name = "Lavoro"
        verbose_name_plural = "Lavori"

class Dettaglio(models.Model):
    descrizione_dettaglio = models.CharField(max_length=200)
    data_dettaglio = models.DateField(("Data dettaglio"), default=datetime.date.today)
    fase_dettaglio = models.ForeignKey(Fase, on_delete=models.CASCADE)
    lavoro_dettaglio = models.ForeignKey(Lavoro, on_delete=models.CASCADE)

    def __str__(self):
        return self.descrizione_dettaglio + " - " + str(self.lavoro_dettaglio)

    class Meta:
        verbose_name = "Dettaglio"
        verbose_name_plural = "Dettagli"


class Allegato(models.Model):
    dettaglio = models.ForeignKey(Dettaglio, on_delete=models.CASCADE)
    foto_allegato = models.FileField(upload_to='upload/')
    documento_allegato = models.FileField(upload_to='upload/')

    def __str__(self):
        return str(self.foto_allegato) + " - " + str(self.documento_allegato)

    class Meta:
        verbose_name = "Allegato"
        verbose_name_plural = "Allegati"
