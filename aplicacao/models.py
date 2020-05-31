from django.db import models
from django.urls import reverse


class Unidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=3)
    descricao = models.CharField(max_length=50)

    class Meta:
        ordering = ['descricao']

    def get_absolute_url(self):
        return reverse('unidade', args=[str(self.codigo)])

    def __str__(self):
        return "{0}-{1}".format(self.sigla, self.descricao)


class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)

    class Meta:
        ordering = ['descricao']

    def get_absolute_url(self):
        return reverse('produto', args=[str(self.codigo)])

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    STATE_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    documento = models.BigIntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES)
    telefonePrincipal = models.CharField(max_length=15, null=True, blank=True)
    telefoneSecundario = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('cliente', args=[str(self.codigo)])

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefonePrincipal = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        ordering = ['nome']

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
        ordering = ['data', 'produto']

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
        ordering = ['data', 'produto']

    def get_absolute_url(self):
        return reverse('venda', args=[str(self.codigo)])

    def __str__(self):
        return "{0} {1}".format(self.data, self.produto)
