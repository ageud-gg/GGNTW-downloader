import webbrowser
import random
import requests as re
import time

file = open("list.txt", "r")
success_file = open("success.txt", "a")

with open("proxies.txt", "r") as proxy_file:
    proxies = proxy_file.read().splitlines()

for url in file.readlines():
    url = url.strip()
    success = False

    while not success:
        proxy_ip = random.choice(proxies)
        proxy_dict = {
            "http": f"http://{proxy_ip}",
            "https": f"http://{proxy_ip}",
        }

        try:
            print("Now checking:", url, "using proxy:", proxy_ip)
            payload = {"url": url}
            request = re.post("https://api.ggntw.com/steam.request", json=payload, proxies=proxy_dict, timeout=10)
            response = request.json()
            print(response["url"], response["result"])
            webbrowser.open(response["url"])
            print("Success:", url)
            success_file.write(url + "\n")
            success = True
            time.sleep(7)
        except Exception as e:
            print(f"Failed with proxy {proxy_ip}: {e}. Retrying...")

file.close()
success_file.close()
