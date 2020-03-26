from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo


class Veiculo(models.Model):
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    observacao = models.TextField()

    def __str__(self):
        return str(self.marca) + ' - Placa: ' + self.placa


class Paramentros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Paramentros Gerais'