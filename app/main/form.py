from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[Required()])
    post = TextAreaField('Pitch at Perfect', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comments are also Perfect at Pitch',validators=[Required()])
    submit = SubmitField('Comment')
