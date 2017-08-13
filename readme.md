Sample graphene playground:
http://graphene-python.org/playground/?query=mutation+%7B%0A++createNote%28content%3A+%22it+works+well%22%29+%7B%0A++++ok%0A++++note+%7B%0A++++++content%2C%0A++++++version%0A++++%7D%0A++%7D%0A%7D%0A&schema=import+graphene%0Aimport+datetime%0A%0A%0Aclass+NoteType%28graphene.ObjectType%29%3A%0A++++content+%3D+graphene.String%28%29%0A++++updated_at+%3D+graphene.String%28%29%0A++++version+%3D+graphene.String%28%29%0A++++language+%3D+graphene.String%28%29%0A++++def+resolve_content%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.content+%0A++++%0A++++def+resolve_updated_at%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.updated_at+%0A++++%0A++++def+resolve_language%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.language+%0A++++%0A++++def+resolve_version%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.version%0A++++%0Aclass+UserType%28graphene.ObjectType%29%3A%0A++++id+%3D+graphene.String%28%29%0A++++name+%3D+graphene.String%28%29%0A++++notes+%3D+graphene.List%28NoteType%29%0A++++%0A++++def+resolve_id%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.id%0A++++%0A++++def+resolve_name%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.name%0A++++%0A++++def+resolve_notes%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++return+self.notes%0A++++%0Aclass+Query%28graphene.ObjectType%29%3A%0A++++users+%3D+graphene.List%28UserType%29%0A%0A++++def+resolve_users%28self%2C+args%2C+context%2C+info%29%3A%0A++++++++note+%3D+NoteType%28%0A++++++++++++updated_at+%3D+datetime.datetime.now%28%29%2C+%0A++++++++++++version+%3D+%221%22%2C%0A++++++++++++content+%3D+%22it+is+text%22%2C%0A++++++++++++language+%3D+%22en%22%0A++++++++%29%0A++++++++return+%5BUserType%28id%3D+1%2C+name%3D+%22the+one%22%2C+%0A+++++++++++++++++++++++++notes%3D+%5Bnote%5D%29%5D%0A%0Aclass+CreateNote%28graphene.Mutation%29%3A%0A++++class+Input%3A%0A++++++++content+%3D+graphene.String%28%29%0A%0A++++ok+%3D+graphene.Boolean%28%29%0A++++note+%3D+graphene.Field%28NoteType%29%0A%0A++++%40staticmethod%0A++++def+mutate%28root%2C+args%2C+context%2C+info%29%3A%0A++++++++note+%3D+NoteType%28content%3Dargs.get%28%27content%27%29%2C%0A+++++++++++++++%09updated_at+%3D+datetime.datetime.now%28%29%2C+%0A++++++++++++%09version+%3D+%222%22%2C%0A++++++++++++%09language+%3D+%22en%22%0A+++++++++++++++++++++++%29%0A++++++++ok+%3D+True%0A++++++++return+CreateNote%28note%3Dnote%2C+ok%3Dok%29%0A%0Aclass+MyMutations%28graphene.ObjectType%29%3A%0A++++create_note+%3D+CreateNote.Field%28%29%0A++++%0Aschema+%3D+graphene.Schema%28query%3DQuery%2C+mutation%3DMyMutations%29%0A

# Basics

Visit: `polls/graphql` for interractive graphql api


# GraphQL Sample API
```
query {
  questions {
    id
    questionText
    date: pubDate
  }
}
```

Mutation (creating a new question):
```
mutation {
  newQuestion(text: "What is going on?") {
    questionCreated {
      id
      questionText
    }
  }
}
```
