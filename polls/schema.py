import graphene
import graphene_django

from django.utils import timezone
from graphene_django.debug import DjangoDebug
from polls.models import Question


class QuestionType(graphene_django.DjangoObjectType):
	class Meta:
		model = Question


class PollsQuery(graphene.ObjectType):
	questions = graphene.List(QuestionType)
	single_question = graphene.Field(QuestionType, id=graphene.Int())
	debug = graphene.Field(DjangoDebug, name='__debug')

	def resolve_questions(self, args, context, info):
		return Question.objects.all()

	def resolve_single_question(self, args, context, info):
		question_id = args.get('id')
		return Question.objects.get(id=int(question_id))


class NewQuestionMutation(graphene.Mutation):
	class Input:
		text = graphene.String()

	question_output = graphene.Field(QuestionType)

	# context argument is django request. Can be used for user auth and permissions, etc
	# e.g. context.user.is_authenticated()
	def mutate(self, args, context, info):
		text_for_question = args.get('text')
		new_question = Question.objects.create(question_text=text_for_question, pub_date=timezone.now())
		return NewQuestionMutation(question_output=new_question)


class PollsMutation(graphene.ObjectType):
	new_question = NewQuestionMutation.Field()


schema = graphene.Schema(query=PollsQuery, mutation=PollsMutation)
