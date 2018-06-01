from django.db import models

# Ask a question with text parameter and time asked
class Question(models.Model):
    question_text = models.CharField(max_length = 100) 
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return '%s' % (self.question_text)
   
   
   
# Question choices and votes 
class Choice(models.Model):
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #makes sure that each choice is linked to the correct question and deletes it if the question is deleted
    
    def __str__(self):
        return self.choice_text
    
    