import graphene
import graphene_django

from django.utils import timezone
from polls.models import Question


class QuestionType(graphene_django.DjangoObjectType):
	class Meta:
		model = Question


class PollsQuery(graphene.ObjectType):
	questions = graphene.List(QuestionType)

	def resolve_questions(self, args, context, info):
		return Question.objects.all()


class NewQuestionMutation(graphene.Mutation):
	class Input:
		text = graphene.String()

	question_output = graphene.Field(QuestionType)

	def mutate(self, args, context, info):
		text_for_question = args.get('text')
		new_question = Question.objects.create(question_text=text_for_question, pub_date=timezone.now())
		return NewQuestionMutation(question_output=new_question)


class PollsMutation(graphene.ObjectType):
	new_question = NewQuestionMutation.Field()


schema = graphene.Schema(query=PollsQuery, mutation=PollsMutation)
