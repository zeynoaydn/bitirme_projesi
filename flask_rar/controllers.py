from flask import Flask,request,send_file,send_from_directory
from flask_restful import Resource
from openCV_funcs import * 
import os

class ImageController(Resource):
    def get(self,operation):
        file=request.files["dosya"]
        file.save(os.path.join("upload/",file.filename))
        path="upload/"+file.filename
        #
        if operation=='applyPencilSketch':
            applyPencilSketch(path)
        elif operation=='convert_to_image_gray':
            convert_to_image_gray(path)
        elif operation=='applyPencilSketch2':
            applyPencilSketch2(path)
        elif operation=='applyGotham':
            applyGotham(path)
        elif operation=='applyWarm':
            applyWarm(path)
        elif operation=='applyCold':
            applyCold(path)
        elif operation=='applyGrayscale':
            applyGrayscale(path)
        elif operation=='applySepia':
            applySepia(path)
        elif operation=='applySharpening':
            applySharpening(path)
        elif operation=='applySharpening2':
            applySharpening2(path)
        elif operation=='applyDetailEnhancing':
            applyDetailEnhancing(path)
        elif operation=='applyStylization':
            applyStylization(path)
        elif operation=='applyInvert':
            applyInvert(path)
        elif operation=='reverseReflection':
            reverseReflection(path)
        elif operation=='resizedImg':
            resizedImg(path)
        elif operation=='horizontalStack':
            horizontalStack(path)
        elif operation=='verticalStack':
            verticalStack(path)
        elif operation=='blackToBlack':
            blackToBlack(path)
        elif operation=='whiteToWhite':
            whiteToWhite(path)
        #
        return send_file(file.filename,as_attachment=True)
        pass
