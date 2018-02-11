from django.shortcuts import render
# 导入HttpResponse函数
from django.http import HttpResponse
# 导入Question模型
from .models import Question
# 从django的template模块导入loader函数,用于加载模板
# from django.template import loader 第三次修改
# 导入Http404函数
# from django.http import Http404 第五次修改
# 导入定制404页面的快捷函数,object用get()返回一个参数,list用filter()返回一个列表
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.


# 第一个展示网页的视图
def index(request):
    # 获取按时间排序的五个问题
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # 从django模板加载我们定义的html页面
    # template = loader.get_template('polls/index.html') 第三次修改

    # 定义发送给模板的上下文(变量,集合等要在html页面显示的内容)
    context = {'latest_question_list': latest_question_list}

    # 输出五个问题的内容
    # output = ', '.join([q.question_text for q in latest_question_list]) 第二次修改

    # 返回由HttpResponse生成的html页面
    # return HttpResponse("Hello, world. You're at the polls index") 第一次修改

    # return HttpResponse(output) 第二次修改

    # 将上下文的字典传送给模板,由模板语言调用内容
    # return HttpResponse(template.render(context, request)) 第三次修改

    # 用render简化模板的调用,无需导入django的template,HttpResponse函数
    return render(request, 'polls/index.html', context)


# 定义问题的具体内容的页面,从urls.py接收question_id作为返回问题的参数
def detail(request, question_id):
    # 返回显示问题的页面
    # return HttpResponse("You're looking at question %s." % question_id) 第四次修改

    # 尝试获取Question对象的内容,传入的question_id参数做id值
    # try:
    #     question = Question.objects.get(pk=question_id) 第五次修改
    # 如果引发获取内容失败的异常(id不存在),发送Http404函数生成的404提示页面
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist") 第五次修改

    # 传入要获取的对象,和它在数据库中的id的值
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 问题结果的页面
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# 问题票数的页面
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
