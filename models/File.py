from sqlalchemy import Column, Integer, String,update
from repository.base_model import Base



class FileBase(Base):
    __tablename__ = 'api_file'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    filename = Column(String, nullable=False)
    file_text = Column(String, nullable=False)
