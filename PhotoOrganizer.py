import os
import shutil
from PIL import Image
from datetime import datetime


class PhotoOrganizer:
    extensions = [
        'jpg',
        'jpeg',
        'JPG',
        'JPEG'
    ]

    def FolderPathFromPhotoDate(self, file):
        date = self.PhotoShootingDate(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def PhotoShootingDate(self, file):
        photo = Image.open(file)
        info = photo._getexif()
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        else:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def MovePhoto(self, file):
        new_folder = self.FolderPathFromPhotoDate(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def Organize(self):
        photo = [
            filename for filename in os.listdir('.')
            if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in photo:
            self.MovePhoto(filename)


PO = PhotoOrganizer()
PO.Organize()
