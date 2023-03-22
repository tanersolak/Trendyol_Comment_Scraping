import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Taner Solak tarafından güncellenmiştir.
def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 0.5
driver = webdriver.Chrome()
#driver.maximize_window()

urun_url =  "https://www.trendyol.com/avva/unisex-siyah-yarim-balikci-yaka-tuylenmeyen-triko-kazak-e005001-p-54102467/yorumlar?boutiqueId=61&merchantId=107671" # Ürünün yorumlarının linki buraya eklenir.

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
match = False


try:
    driver.get(urun_url )#, "/yorumlar") # Eğer isterseniz bu satırı açarak sadece ürün linki ile yorumlara ulaşabilirsiniz.
    time.sleep(5)
    while match == False:
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
    time.sleep(3)

    kac_yorum_var = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/span')
    print("yorum ",len(kac_yorum_var))
    #kac_yorum_var = kac_yorum_var.replace(" Yorum", "")
    #log('Toplam ' , kac_yorum_var , ' yorum var.')

    for i in range(len(kac_yorum_var)):
        try:
            for yorum in driver.find_elements(By.XPATH, f'/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/div[3]/div[4]/div[{i}]/div[1]/div/p'):
                print(yorum.text)
            #log('Yorum: '+ yorum)
            yorum_file = open("yorumlar.txt", "a", encoding='utf-8')
            yorum_file.write(str(yorum.text) + "\n")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(global_delay)
        except:
            continue
except Exception as e:
    log(f'Hata: {e}')
    log('Program sonlandı')
    driver.quit()
    exit()
