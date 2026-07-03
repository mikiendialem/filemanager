from file import File
from directory import Directory
from search_engine import SearchEngine
from file_info import FileInfo


class FileManager:

    def __init__(self):

        self.file = File()
        self.directory = Directory()
        self.search = SearchEngine()
        self.info = FileInfo()