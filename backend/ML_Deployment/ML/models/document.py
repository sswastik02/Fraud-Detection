from ISR.models import RRDN
from pdf2image import convert_from_path
import img2pdf
import os, sys

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from helpers.document.uid import Extract_and_Mask_UIDs
from helpers.document.file_downloader import downloader

class Document:
    def get_model(self):
        return RRDN(weights='gans')

    def preprocess_data(self,path:str):
        name,ext = path.split('.')
        if ext == 'pdf':
            pages = convert_from_path(path,300)
            pages[0].save(name+'.jpg','JPEG')
            
        path = path if ext != "pdf" else name+'.jpg'

        masked_img,possible_UIDs = Extract_and_Mask_UIDs(path)
        return masked_img,possible_UIDs

    def verify(self,url):
        try:
            file_path = downloader(url)
            masked_img,possible_UIDs = self.preprocess_data(file_path)
            os.remove(file_path)
        except:
            raise "Error in Document"
        
        return (masked_img != None)


    