import os


class SearchEngine:

    def search(self, filename, path="."):

        found = False

        for root, dirs, files in os.walk(path):

            if filename in files:
                print(os.path.join(root, filename))
                found = True

        if not found:
            print("❌ File not found.")