import os
import shutil


class Directory:

    def create(self, folder_name):
        try:
            os.mkdir(folder_name)
            print("✅ Folder created.")
        except FileExistsError:
            print("❌ Folder already exists.")

    def delete(self, folder_name):
        try:
            shutil.rmtree(folder_name)
            print("✅ Folder deleted.")
        except FileNotFoundError:
            print("❌ Folder not found.")

    def rename(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print("✅ Folder renamed.")
        except FileNotFoundError:
            print("❌ Folder not found.")

    def list_contents(self, path="."):
        print("\nContents:\n")

        for item in os.listdir(path):
            print(item)