from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return self.marca.nome + ' - ' + self.placa
        

