from flask.ext.wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired

class addForm(Form):
    subject = StringField('subject', validators=[DataRequired()])
    code = StringField('code', validators=[DataRequired()])
    homework = TextField('homework', validators=[DataRequired()])