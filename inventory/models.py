from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # 修改CATEGORY_CHOICES为明确的分类
    CATEGORY_CHOICES = [
        ('tobacco', '烟草'),
        ('liquor', '酒水'),
        # 如果有其他分类可以继续添加
    ]
    
    name = models.CharField('产品名称', max_length=100)
    category = models.CharField('产品类别', max_length=50, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField('库存数量')
    production_date = models.DateField('生产日期')
    image = models.ImageField('产品图片', upload_to='products/', null=True, blank=True)
    # 确保以下三个新增字段存在
    import_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    batch_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_category_display()} - {self.name}"
