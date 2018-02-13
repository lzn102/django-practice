from django.db import models
# 导入python标准时间模块
import datetime
# 导入Django时区函数,以正确显示时间
from django.utils import timezone

# Create your models here.


# 创建Question模型用来生成要投票的问题,继承models的Model类
class Question(models.Model):
    # models的CharField函数设置创建的问题的文本长度
    question_text = models.CharField(max_length=200)
    # DateTimeField函数在问题创建时自动生成当前时间
    pub_date = models.DateTimeField('date published')
    # 返回对象的表示为字符串,如果不设置,查看该模型的objects.all()显示的是"object(id)",这样不利于查看

    def __str__(self):
        return self.question_text
    # 上面的__str__是python的自带方法,下面使我们自己创建的方法

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# 创建投票所用的选项类
class Choice(models.Model):
    # 投票的问题用ForeignKey函数关联Question类创建的问题,2.0版本需要加入on_delete参数
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 设置选项的文本
    choice_text = models.CharField(max_length=200)
    # IntegerField函数设置票数为整形,传入默认参数为0
    votes = models.IntegerField(default=0)

    # 返回choice_text的字符串表示

    def __str__(self):
        return self.choice_text


