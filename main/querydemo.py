'''
From main.model import *
users= account.objects.all()
userbyname= account.objects.get(username="Altair")

r1= recipe.objects.get(id=1)
r1.hcon.all()
recipe = recipe.objects.filter(rtype="B")
'''