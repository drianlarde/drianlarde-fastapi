import ormar
from db import MainMata

class Doc(ormar.Model):
    class Meta(MainMata):
        pass


id = ormar.Integer(primary_key=True)
title = ormar.String(max_length=30)
text = ormar.string(max_length=1000)
author = ormar.String(max_length=30)