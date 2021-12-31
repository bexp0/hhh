# NFT Downloader
I was getting bored sitting around, at this time of year. Today's 31st December, 2021. Few hours, and its gone. I sat down at the chair and was watching this John Hammond [video](https://www.youtube.com/watch?v=hzpyhZHDPys). Then it came to my mind to download some NFTs and see how it goes.

Thus these scripts came to life. I made three scripts to automate downloading NFTs from the following sites- 
- [Cryptopunks](https://www.larvalabs.com/cryptopunks)
- [Wall St. Bulls](https://wallstreetbulls.io/)
- [Mutant Ape Yacht Club](https://opensea.io/collection/mutant-ape-yacht-club)

![terminal photo](/img/stealing-nfts.png)

It was quite easy to download NFTs from the first two sources. But when it came to **Mutant Ape Yacht Club**, it was hard to do so. Because **Opensea** used Google Cloud to host the images, and used **Cloudflare** to protect their website against attackers. This called for a different measure.

### Cryptopunks
```bash
#!/usr/bin/bash
for each in {0000..10000}
do
wget "https://www.larvalabs.com/cryptopunks/cryptopunk$each.png"
done
```

### Wall Street Bulls
```bash
#!/usr/bin/bash
for  i  in {1..1000}
do
wget "https://wallstreetbulls.io/wallstbulls/media/$i.jpg"
done
```

### Mutant Ape Yacht Club
```py
from selenium import webdriver
import wget

base_url = "https://opensea.io/assets/0x60e4d786628fea6478f785a6d7e704777c86a7c6/"
driver = webdriver.Chrome()

for each in  range(10000):
	driver.get(base_url + str(each))
	img_src = driver.find_element_by_xpath("//*[@id='main']/div/div/div/div[2]/div/article/div/div/div/div/img").get_attribute("src")
	if img_src is  not  None:
		wget.download(img_src, str(each) + ".png")

driver.close()
```
## Conclusion
Well, I know these are no way to own/steal NFTs, I just did it for the fun. Scripting the **Mutant Ape Yacht Club** was a learning for sure. This is it, feel free to mix and master these scripts to download favorite NFTs.
