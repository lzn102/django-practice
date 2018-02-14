from django.shortcuts import render
# 导入HttpResponse函数
from django.http import HttpResponse
# 导入Question模型,导入Choice模型
from .models import Question, Choice
# 从django的template模块导入loader函数,用于加载模板
# from django.template import loader 第三次修改
# 导入Http404函数
# from django.http import Http404 第五次修改
# 导入定制404页面的快捷函数,object用get()返回一个参数,list用filter()返回一个列表
from django.shortcuts import get_object_or_404, get_list_or_404
# 导入HttpResponseRedirect函数
from django.http import HttpResponseRedirect
# 导入reverse
from django.urls import reverse
# 从Django视图模块导入一种通用视图的函数
from django.views import generic
# 导入时区模块验证问题是否发布在未来
from django.utils import timezone


# Create your views here.

'''
# 不调用Django通用函数的写法
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
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    # 返回查看票数结果的页面
    return render(request, 'polls/results.html', {'question': question})
'''
# 抽象显示对象列表和对象的内容,List抽象出只有列表的形式,Detail抽象出返回具体内容的形式,通用视图捕获的主键都叫pk,urls.py需要改


class IndexView(generic.ListView):
    # 需指定模板
    template_name = 'polls/index.html'
    # 指定自己定义的上下文名称
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # 定义查询集只返回五个问题
        # return Question.objects.order_by('-pub_date')[:5]
        # 筛选出五个创建时间早于现在的问题
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # 需指定用到的模型名称
    model = Question
    template_name = 'polls/detail.html'

    # 筛选出早于当前时间创建的问题,避免用户猜出url访问未来的问题内容
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 问题票数的页面
def vote(request, question_id):
    # 根据id获取Question的对象,没有则返回自定义404页面
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice']返回投票那个选项的id(是以字符串形式),request.POST返回的是一个字典,而choice则是传入的键
        # 尝试根据pk获取的id获取与对象相关联的值(用ForeignKey的那个值)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 如果id不存在,或者没有相关联的值
    except (KeyError, Choice.DoesNotExist):
        # 返回问题的内容页面,显示该对象没有相应的选项
        return render(request, 'polls/detail.html', {
            'question': question, 'error_message': "you didn't select a choice."
        })
    # 如果有对应的选项
    else:
        # 该选项的投票数量加1
        selected_choice.votes += 1
        # 把数据存入数据库
        selected_choice.save()
        # HttpResponseRedirect函数返回指定的页面,reverse函数确定页面url和id,注意args只有一个参数也需要逗号
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)












