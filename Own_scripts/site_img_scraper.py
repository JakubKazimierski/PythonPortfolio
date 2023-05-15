import os
import sys
import requests
from bs4 import *


class Web_img_scraper:
    def __init__(self, url_to_scrap, folder_name):
        self.url_to_scrap = url_to_scrap
        self.folder_name = folder_name
        
 
    def get_all_img_tags(self, url_to_scrap):
        try:
            site_obj = requests.get(url_to_scrap)
        
            website_html_code = BeautifulSoup(site_obj.text, 'html.parser')
        
            img_html_tags = website_html_code.findAll('img')
        
            return img_html_tags

        except Exception as e:
            print(f"Could not find img tags at: {self.url_to_scrap}: ", e)
            sys.exit(1)


    def create_folder(self, folder_name):    
        try:
            os.mkdir(folder_name)
        
        except Exception as e:
            print("Could not create folder: ", e)


    def get_image_src(self, img_html_tag):
        try:
            return img_html_tag["src"]
        except Exception as e:
            print(f"Could not get image src: ", e)


    def get_img_name_from_src(self, img_src):
        try:
            return img_src.split('/')[-1]
        except Exception as e:
            print(f"Could not extract img name from: {img_src}: ", e)


    def download_image_from_src(self, img_src):
        try:
            img_downloaded = requests.get(img_src).content
            return img_downloaded
        
        except Exception as e:
            print(f"Could not download img: {img_src}: ", e)


    def save_img_to_file(self, full_file_path, image):
        try:
            with open(full_file_path, "wb+") as file_buff:
                file_buff.write(image)

        except Exception as e:
            print(f"Could not save img: {full_file_path} {image}: ", e)


    def create_full_path_to_file(self, file_name, file_directory_name):

        try:
            directory_path = os.path.join(os.getcwd(), file_directory_name)

        except Exception as e:
            print(f"Could not prepare directory path: {directory_path}: ", e)
        
        try:
            return os.path.abspath(os.path.join(directory_path, file_name))
        except Exception as e:
            print(f"Could not return absolute path: ", e)


    def scrap_url(self):

        img_html_tags = self.get_all_img_tags(self.url_to_scrap)

        if len(img_html_tags) <= 0:
            print("No img tags from given url")
            sys.exit(1)
        else:

            self.create_folder(self.folder_name)    

            for img_html_tag in img_html_tags:

                img_src = self.get_image_src(img_html_tag)
                img_downloaded = self.download_image_from_src(img_src)
                img_name = self.get_img_name_from_src(img_src)
                full_path_to_img = self.create_full_path_to_file(img_name, self.folder_name)
                self.save_img_to_file(full_path_to_img, img_downloaded)



def main():

    web_img_scraper = Web_img_scraper("https://github.com/", "scrapped_images")
    web_img_scraper.scrap_url()
  

main()



