from django.db import models
from django.urls import reverse


class Unidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=3)
    descricao = models.CharField(max_length=50)

    class Meta:
        db_table = "unidades"
        ordering = ['-descricao']

    def get_absolute_url(self):
        return reverse('unidade', args=[str(self.codigo)])

    def __str__(self):
        return "{0}-{1}".format(self.sigla, self.descricao)


class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)

    class Meta:
        db_table = "produtos"
        ordering = ['-descricao']

    def get_absolute_url(self):
        return reverse('produto', args=[str(self.codigo)])

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    documento = models.BigIntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    telefonePrincipal = models.BigIntegerField()
    telefoneSecundario = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = "clientes"
        ordering = ['-nome']

    def get_absolute_url(self):
        return reverse('cliente', args=[str(self.codigo)])

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefonePrincipal = models.BigIntegerField()

    class Meta:
        db_table = "fornecedores"
        ordering = ['-nome']

    def get_absolute_url(self):
        return reverse('fornecedor', args=[str(self.codigo)])

    def __str__(self):
        return self.nome


class Compra(models.Model):
    PREVISTO = 'P'
    REALIZADO = 'R'
    COMPRAS_SITUACAO_CHOICES = [
        (PREVISTO, 'Previsto'),
        (REALIZADO, 'Realizado'),
    ]
    codigo = models.AutoField(primary_key=True)
    notafiscal = models.CharField(max_length=50)
    data = models.DateTimeField()
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)
    unidade = models.ForeignKey('Unidade', on_delete=models.PROTECT)
    quantidade = models.DecimalField(max_digits=9, decimal_places=3)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    situacao = models.CharField(max_length=1, choices=COMPRAS_SITUACAO_CHOICES, default=PREVISTO)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.PROTECT)

    class Meta:
        db_table = "compras"
        ordering = ['data', '-produto']

    def get_absolute_url(self):
        return reverse('compra', args=[str(self.codigo)])

    def __str__(self):
        return "{0} {1}".format(self.data, self.produto)


class Venda(models.Model):
    PREVISTO = 'P'
    REALIZADO = 'R'
    VENDAS_SITUACAO_CHOICES = [
        (PREVISTO, 'Previsto'),
        (REALIZADO, 'Realizado'),
    ]
    codigo = models.AutoField(primary_key=True)
    data = models.DateTimeField()
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)
    unidade = models.ForeignKey('Unidade', on_delete=models.PROTECT)
    quantidade = models.DecimalField(max_digits=9, decimal_places=3)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    situacao = models.CharField(max_length=1, choices=VENDAS_SITUACAO_CHOICES, default=PREVISTO)
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT)

    class Meta:
        db_table = "vendas"
        ordering = ['data', '-produto']

    def get_absolute_url(self):
        return reverse('venda', args=[str(self.codigo)])

    def __str__(self):
        return "{0} {1}".format(self.data, self.produto)
