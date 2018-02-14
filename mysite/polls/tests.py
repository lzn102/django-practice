# 导入时间模块
import datetime
# 导入时区模块
from django.utils import timezone
# 从测试模块导入测试案例函数,它有某个实例在未来创建的方法
from django.test import TestCase
# 导入测试用的模型
from .models import Question
from django.urls import reverse


# Create your tests here.


# 创建一个测试类,继承TestCase
class QuestionModelTests(TestCase):
    # 定义一个方法,用来创建在未来的问题
    def test_was_published_recently_with_future_question(self):
        # 时间设置为现在的时区时间 + 两个时间之间的差值(这里是30天)
        time = timezone.now() + datetime.timedelta(days=30)
        # 创建一个未来的问题,创建时间设置为30天后
        future_question = Question(pub_date=time)
        # assertIs方法发现第一个参数的值,第二个参数是我们希望的值,如果两个值不同,测试会报错
        self.assertIs(future_question.was_published_recently(), False)

    # 测试问题的创建时间是否早于现在,希望返回错误
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # 测试问题的创建时间是否是当前时间.希望返回正确
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# 创建一个可以自定义创建任意时间的问题的函数,
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# 测试过去未来现在的问题是否正确的显示
class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question>'])

    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


# 测试未来的问题内容是否可以被用户猜到而透露
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


