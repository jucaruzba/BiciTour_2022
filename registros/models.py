from django.db import models

class Tours(models.Model):
    
    disponible = models.BooleanField(default=True, verbose_name='Disponible')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    fechaIni=models.DateTimeField(auto_now=False, verbose_name='Fecha de Inicio')
    ciudad = models.CharField(max_length=200, verbose_name='Ciudad')
    kmreC = models.IntegerField(verbose_name='Km recorridos')
    timeStimed = models.CharField(max_length=100,verbose_name='Tiempo estimado')
    puntoIni = models.CharField(max_length=200, verbose_name='Punto de inicio')
    costo = models.IntegerField(verbose_name='Costo')
    foto = models.ImageField(null=True, verbose_name='Foto', upload_to='fotos')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ['-created']
        
    def __str__(self):
        return self.title