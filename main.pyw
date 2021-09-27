import os
import shutil

while True:
    def img():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Documents/PI OS/"
        for file in source_files:
            if file.endswith('.img'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    def pdf():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Documents/PDF/"
        for file in source_files:
            if file.endswith('.pdf'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    def pptx():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Documents/OFFICE/"
        for file in source_files:
            if file.endswith('.pptx'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    def word():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Documents/OFFICE/"
        for file in source_files:
            if file.endswith('.docx'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    def jfif():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Pictures/"
        for file in source_files:
            if file.endswith('.jfif'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    def png():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Pictures/"
        for file in source_files:
            if file.endswith('.png'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    def jpg():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Pictures/"
        for file in source_files:
            if file.endswith('.jpg'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))
                

    def stl():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Documents/3D IMPRESSIONS/"
        for file in source_files:
            if file.endswith('.stl'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))
                
    
    def ino():
        source_path = "/Users/El mamoun/Downloads/"
        source_files = os.listdir(source_path)
        destination_path = "/Users/El mamoun/Documents/Arduino/"
        for file in source_files:
            if file.endswith('.ino'):
                shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))


    pptx()
    word()
    jfif()
    pdf()
    img()
    jpg()
    png()
    stl()
    ino()
