# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from polls.models import Question
from polls.schema import schema


class PollsApiTestCase(TestCase):
	def test_can_list_questions(self):
		# new question
		Question.objects.create(question_text="test 1", pub_date=timezone.now())

		# query it with graphql
		query = """
		query {
			questions {
				id,
				questionText
			}
		}
		"""

		result = schema.execute(query)
		self.assertEquals(len(result.data['questions']), 1)
		self.assertEquals(result.errors, None)

	def test_can_create_question(self):
		mutation = """
		mutation {
		  newQuestion(text: "%s") {
		    questionOutput {
		      id
		      questionText
		    }
		  }
		}
		""" % "does it work"

		result = schema.execute(mutation)
		self.assertEquals(result.data['newQuestion']['questionOutput']['questionText'], "does it work")
		self.assertEquals(result.errors, None)
		question = Question.objects.get(pk=result.data['newQuestion']['questionOutput']['id'])
		self.assertEquals(question.question_text, "does it work")
