import requests
from bs4 import BeautifulSoup as b
import csv

csvFile = open("ScrapeData.csv", "w")

csv_writer = csv.writer(csvFile)
csv_writer.writerow(['headline', 'summary', 'video_link'])

url = "https://coreyms.com/"
source = requests.get(url).text
soup = b(source, "lxml")



for article in soup.find_all("article"):
    headline = article.h2.a.text
    print(headline)

    summary = article.find("div", class_="entry-content").p.text
    print(summary)


    try:
        vidsrc = article.find("iframe", class_ = "youtube-player")["src"]
        vid_id = vidsrc.split("/")[4].split("?")[0]

        yt_link = f"https://youtube.com/watch?v={vid_id}"

    except:
        yt_link = "No link detected."
    print(yt_link)

    print("-----------------------------------------------------------------------------")
    csv_writer.writerow([headline, summary, yt_link])

csvFile.close()
#credits CoreyMS
