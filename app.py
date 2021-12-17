from flask import Flask, render_template, request
import os, pytesseract
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask( __name__,
            static_url_path = '',
            static_folder = 'static',
            template_folder = 'templates')

photos = UploadSet('photos', IMAGES)

app.config['Debug'] = True
app.config['UPLOAD_FOLDER'] = 'images'



