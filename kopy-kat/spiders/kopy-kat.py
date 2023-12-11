import scrapy, os, re, sys


class KopyKat(scrapy.Spider):
    name = 'kopy-kat'

    custom_settings = {
        "KOPY-KAT_BASE_URL": "https://github.com/sulphurcrested/",
        "KOPY-KAT_BASE_CONTENT_PATH": "./content/",
        "KOPY-KAT_SAVE_FILE": False,
        "KOPY-KAT_MAX_CRAWLS": 0
    }

    base_url = custom_settings["KOPY-KAT_BASE_URL"]
    start_urls = [base_url]
    base_write = custom_settings["KOPY-KAT_BASE_CONTENT_PATH"]
    
    # MAX CRAWLS counter
    count = int(custom_settings["KOPY-KAT_MAX_CRAWLS"])

    def save_file(self, response):
        fileName = response.url.replace(self.base_url,'') or "index.html"
        # strip input
        if fileName.find("?") >= 0:
            fileName = fileName[:(fileName.find("?"))]
        
        if fileName.find("#") >= 0:
            fileName = fileName[:(fileName.find("#"))]

        if fileName:
            print(f'===### writing a new file: {fileName}')
            f = open(self.get_path(fileName), "+bw")
            f.write(response.body)
        else:
            print(f'===### skiping link: {fileName}')


    # builds a relative directory structure
    def get_path(self, filePath: str):
        # remove base URL in case absolute path is used
        tokens = filePath.split('/')
        fileName = tokens[-1]
        path = "/".join(tokens[:-1])

        if (self.base_write[-1] == '/'):
            path = self.base_write+path
        else:
            path = self.base_write+"/"+path

        if not os.path.exists(path):
            print(f'===### creating a new directory: {path}')
            os.makedirs(path)

        return path+"/"+fileName


    def parse(self, response):

        if int(self.custom_settings["KOPY-KAT_MAX_CRAWLS"]) > 0:
            if self.count <= 0:
                return
            self.count -= 1

        if bool(self.custom_settings["KOPY-KAT_SAVE_FILE"]):
            self.save_file(response)

        for next_page_url in response.xpath("//a/@href").getall():
            print(f'===### found link:{next_page_url}')
            next_page_url = next_page_url.replace(self.base_url,'')
            next_url = response.urljoin(next_page_url)
            print(f'===### next url:{next_url}')

            # if pointing to external url then continue
            if next_url.find(self.base_url) == 0 :
                print(f'====#### crawling url: {next_url}')
                yield scrapy.Request(next_url)
            else:
                print(f'====#### skiping external url: {next_url}')
