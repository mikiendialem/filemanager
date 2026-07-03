import os
from datetime import datetime


class FileInfo:

    def display(self, filename):

        if not os.path.exists(filename):
            print("❌ File not found.")
            return

        size = os.path.getsize(filename)

        created = datetime.fromtimestamp(
            os.path.getctime(filename)
        )

        modified = datetime.fromtimestamp(
            os.path.getmtime(filename)
        )

        print("\n========== File Information ==========")
        print(f"Name: {os.path.basename(filename)}")
        print(f"Path: {os.path.abspath(filename)}")
        print(f"Size: {size} bytes")
        print(f"Created: {created}")
        print(f"Modified: {modified}")