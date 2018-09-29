# 返回页面视图

# 于是 Django 提供了一个快捷函数render，载入模板，填充上下文，再返回由它生成的 HttpResponse 对象。
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
# 加载模板
from django.template import loader
# 数据
from django.db.models import F
from .models import Question, Choice


# Create your views here.

# 返回页面1
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list
# 	}

# 	return HttpResponse(template.render(context, request))

# 返回页面， rander重写
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list
# 	}

# 	return render(request, 'polls/index.html', context)
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published question"""
		return Question.objects.order_by('-pub_date')[:5]


# 详情
# def detail(request, question_id):
# 	try:
# 		# pk: primary key
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404('Question does not exist')
# 	return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {
# 		'question': question
# 	})
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redispaly the question voting from.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice",
		})
	else:
		# 避免提交竞争条件
		selected_choice.votes = F('votes')+1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# 视频测试
def video(request):
	template = loader.get_template('polls/video.html')
	context = {
		1: 1,
	}
	return HttpResponse(template.render(context, request))

# json测试
def jsonDemo(request, question_id=1):
	question = Question
	return HttpResponse(question)
