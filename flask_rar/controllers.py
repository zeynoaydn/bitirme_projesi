from flask import Flask,request,send_file,send_from_directory
from flask_restful import Resource
from openCV_funcs import * 
import os
import random
import string

class ImageController(Resource):

    def get(self,resim_adi):
        return send_file(resim_adi)
    
    def post(self,operation):
        alphabet = string.ascii_letters + string.digits
        token = ''.join(random.choice(alphabet) for _ in range(10))

        file=request.files["dosya"]
        file.save(os.path.join("upload/",file.filename))
        path="upload/"+file.filename

        if operation=='applyPencilSketch':
            applyPencilSketch(path, token)
        elif operation=='convert_to_image_gray':
            convert_to_image_gray(path, token)
        elif operation=='applyPencilSketch2':
            applyPencilSketch2(path, token)
        elif operation=='applyGotham':
            applyGotham(path, token)
        elif operation=='applyWarm':
            applyWarm(path, token)
        elif operation=='applyCold':
            applyCold(path, token)
        elif operation=='applyGrayscale':
            applyGrayscale(path, token)
        elif operation=='applySepia':
            applySepia(path, token)
        elif operation=='applySharpening':
            applySharpening(path, token)
        elif operation=='applySharpening2':
            applySharpening2(path, token)
        elif operation=='applyDetailEnhancing':
            applyDetailEnhancing(path, token)
        elif operation=='applyStylization':
            applyStylization(path, token)
        elif operation=='applyInvert':
            applyInvert(path, token)
        elif operation=='reverseReflection':
            reverseReflection(path, token)
        elif operation=='resizedImg':
            resizedImg(path, token)
        elif operation=='horizontalStack':
            horizontalStack(path, token)
        elif operation=='verticalStack':
            verticalStack(path, token)
        return {'state':True, 'edit_image_url':'http://10.0.2.2:5000/getImage/'+token+file.filename}
        # return send_file(file.filename,as_attachment=True)