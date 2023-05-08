from app.app import create_app
from app.routes.user.user_crud import user_crud
from app.routes.course.course_crud import course_crud
from app.routes.course.lection_crud import lection_crud
from app.routes.course_management.user_content import user_content
from app.files_management.utils import FilesGenerator, FilesLoader


app = create_app()
app.register_blueprint(user_crud)
app.register_blueprint(course_crud)
app.register_blueprint(lection_crud)
app.register_blueprint(user_content)


@app.cli.command("generate_csv")
def generate_csv():
    FilesGenerator.generate_csv_files('app\\files_management\\csv_files')


@app.cli.command("write_csv_into_db")
def write_csv_into_db():
    FilesLoader.write_csv_data_into_db('app\\files_management\\csv_files')
