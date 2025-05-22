from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as webdriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper.models import PropertyListing
import time

# Configura las opciones del navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")                # Navegación privada, sin cookies previas
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Oculta que usas Selenium
chrome_options.add_argument("--disable-extensions")       # Desactiva extensiones del navegador
chrome_options.add_argument("--disable-gpu")              # A veces ayuda en Windows para evitar bugs
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/114.0.0.0 Safari/537.36")


# Opcional: agrega un tamaño fijo para evitar detectar la ventana maximizada "real"
chrome_options.add_argument("window-size=1920,1080")


# Cambia el path al ejecutable de chromedriver si es necesario
service = Service()

# Inicia el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre idealista
driver.get("https://www.idealista.com/alquiler-viviendas/sevilla/aljarafe/con-precio-hasta_850,metros-cuadrados-mas-de_100,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,dos-banos,tres-banos-o-mas,publicado_ultima-semana/?ordenado-por=precios-asc")

#Espera que la pagina cargue
wait = webdriverWait(driver, 10)

#Extraccion de los anuncios
listings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item-info-container")))
properties = [] # Lista para almacenar los objetos PropertyListing

for listing in listings:
    # Extrae la descripcion del anuncio
    description = listing.find_element(By.CLASS_NAME, "main-info__title").text
    #Extrae la localizacion de la vivienda
    location = listing.find_element(By.CLASS_NAME, "main-info__title-minor").text
    # Extrae el precio del anuncio
    price = listing.find_element(By.CLASS_NAME, "info-data-price").text
    # Extrae las características del anuncio
    features = listing.find_element(By.CLASS_NAME, "info-features").text
    #Extrae el enlace del anuncio
    link = listing.find_element(By.TAG_NAME, "a").get_attribute("href")

    # Crea un objeto PropertyListing y lo añade a la lista
    prop = PropertyListing(description, location, price, features, link)
    properties.append(prop) 

for p in properties:
    print(p)
    print("_" * 50)

# Espera unos segundos para comprobar que se abre correctamente
time.sleep(5)

# Cierra el navegador
driver.quit()