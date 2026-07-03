import os
import shutil


class File:

    def create(self, filename):
        try:
            with open(filename, "w") as file:
                pass
            print("✅ File created successfully.")
        except Exception as e:
            print(f"❌ Error: {e}")

    def delete(self, filename):
        try:
            os.remove(filename)
            print("✅ File deleted successfully.")
        except FileNotFoundError:
            print("❌ File not found.")

    def rename(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print("✅ File renamed successfully.")
        except FileNotFoundError:
            print("❌ File not found.")

    def copy(self, source, destination):
        try:
            shutil.copy(source, destination)
            print("✅ File copied successfully.")
        except FileNotFoundError:
            print("❌ File not found.")

    def move(self, source, destination):
        try:
            shutil.move(source, destination)
            print("✅ File moved successfully.")
        except FileNotFoundError:
            print("❌ File not found.")