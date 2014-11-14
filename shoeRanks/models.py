from django.db import models

# Create your models here.
class imageOrders(models.Model):
	SHINY = 0
	OPEN = 1
	DARK = 2
	HIGH = 3
	
	ATTRIBUTES = (
    (SHINY, 'Shiny'),
    (OPEN, 'Open'),
    (DARK, 'Dark in Color'),
    (HIGH, 'High Heeled'),
  )
	attribute = models.IntegerField(default = OPEN, choices = ATTRIBUTES)
	first_image = models.CharField(max_length = 255)
	second_image = models.CharField(max_length = 255)

	def __unicode__(self):
		return u'%s %s' % (self.first_image, self.second_image)
	