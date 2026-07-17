import os
import time
import hashlib
import requests

from tqdm import tqdm

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ==========================================
# PERSONAJES Y BÚSQUEDAS
# ==========================================

search_queries = {
    "Iron_Man": [
        "Iron Man MCU"
    ],

    "Captain_America": [
        "Captain America MCU"
    ],

    "Thor": [
        "Thor MCU"
    ],

    "Hulk": [
        "Hulk MCU"
    ],

    "Spider_Man": [
        "Spider-Man MCU"
    ],

    "Doctor_Strange": [
        "Doctor Strange MCU"
    ],

    "Scarlet_Witch": [
        "Scarlet Witch MCU"
    ],

    "Loki": [
        "Loki MCU"
    ],

    "Black_Panther": [
        "Black Panther MCU"
    ],

    "Thanos": [
        "Thanos MCU"
    ]
}

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ==========================================
# HASHES PARA EVITAR DUPLICADOS
# ==========================================

downloaded_hashes = set()


# ==========================================
# DESCARGA DE UN PERSONAJE
# ==========================================

def download_character(driver, character, queries):

    save_dir = os.path.join("dataset", character)
    os.makedirs(save_dir, exist_ok=True)

    image_count = len(os.listdir(save_dir))

    for query in queries:

        print(f"\n🔎 {character} -> {query}")

        driver.get("https://images.google.com")

        time.sleep(2)

        search_box = driver.find_element(By.NAME, "q")

        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)

        # Scroll para cargar más imágenes
        for _ in range(8):

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(2)

        imgs = driver.find_elements(By.TAG_NAME, "img")

        for img in tqdm(imgs, leave=False):

            src = img.get_attribute("src")

            if src is None:
                continue

            if "encrypted-tbn0.gstatic.com" not in src:
                continue

            try:

                response = requests.get(src, timeout=10)

                if response.status_code != 200:
                    continue

                image_bytes = response.content

                image_hash = hashlib.sha256(image_bytes).hexdigest()

                if image_hash in downloaded_hashes:
                    continue

                downloaded_hashes.add(image_hash)

                filename = os.path.join(
                    save_dir,
                    f"{image_count:05d}.jpg"
                )

                with open(filename, "wb") as f:
                    f.write(image_bytes)

                image_count += 1

            except Exception:
                pass

    print(f"✅ {character}: {image_count} imágenes descargadas")


# ==========================================
# DESCARGAR TODO EL DATASET
# ==========================================

os.makedirs("dataset", exist_ok=True)

for character, queries in search_queries.items():

    download_character(
        driver,
        character,
        queries
    )

print("\n🎉 Dataset completado.")