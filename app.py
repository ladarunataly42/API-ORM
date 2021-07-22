from flask import Flask, request
from flask_restful import Api, Resource
from repository.MariaDB import MariaDB
from models.File import FileBase
import os

app = Flask(__name__)
api = Api(app)
repo = MariaDB()


class Home(Resource):
    def get(self):
        return "Hello. This is a blank page"


class Upload(Resource):
    def post(self):
        file = request.files['file']
        filename = file.filename
        file.save("UPLOAD_FOLDER" + "/" + filename)
        my_file = open("UPLOAD_FOLDER/" + filename, "r")
        text = my_file.read()
        try:
            obj = FileBase(filename=filename, file_text=text)
            repo.session.add(obj)
            repo.session.commit()
            return "Uploaded", 200
        except Exception:
            return "Problem on upload the file", 404


class Delete(Resource):
    def delete(self):
        id = request.form.get('id')
        try:
            file = repo.session.query(FileBase).get(id)
            filename=file.filename
            repo.session.delete(file)
            repo.session.commit()
            os.remove("UPLOAD_FOLDER/" + filename)
            return "Deleted", 200
        except Exception:
            return "The id you entered does not exist", 404


class Update(Resource):
    def patch(self):
        id = request.form.get('id')
        text = request.form.get('text')
        try:
            files=repo.session.query(FileBase).get(id)
            files.file_text=text
            repo.session.commit()
            return "Updated", 200
        except Exception:
            return "Problem on update or id doesn't exist", 404


api.add_resource(Home, '/')
api.add_resource(Upload, '/upload')
api.add_resource(Delete, '/delete')
api.add_resource(Update, '/update-file')

if __name__ == '__main__':
    app.run()
