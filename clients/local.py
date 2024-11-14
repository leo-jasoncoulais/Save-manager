
import os
import shutil

class Service:

    def __init__(self):
        pass

    def upload(self, file, name=None):

        if not name:
            name = os.path.basename(file)
        
        shutil.copy(file, name)

class LocalClient:

    def __init__(self):
        pass

    def get_service(self):
        return Service()
