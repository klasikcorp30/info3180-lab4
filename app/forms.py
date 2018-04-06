from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired,FileField,FileAllowed


class UploadForm(FlaskForm):
    upload = FileField("Image", validators=[FileRequired(),
    FileAllowed(['jpg','jpeg','png'],'Images Only!')])
    
    