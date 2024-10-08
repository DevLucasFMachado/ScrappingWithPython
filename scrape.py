import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service 
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Inicializando o brownser: chrome")


    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Pagina carregada")
        html = driver.page_source
        time.sleep(3)
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    #remove os \n desnecessários providos pelo html
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content, max_lenght=6000):
    return[
        dom_content[i: i + max_lenght] #pega os primeiros 6000 caracteres
        for i in range(0, len(dom_content), max_lenght) # divide o conteudo em varios blocos do valor max_lenght
                                                        # termina ao utilizar todos os valores dentro de dom_content
    ]