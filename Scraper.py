# Title : a-size-large product-title-word-break
# Info : a-expander-content a-expander-partial-collapse-content a-expander-content-expanded
from bs4 import BeautifulSoup
from typing import Any
import numpy as np
import requests

def Scrape() -> dict[str, Any]:
    URL: str = "https://www.amazon.com/ASUS-IPS-Level-Display-i5-12500H-FX707ZC-ES52/dp/B0CRD335BV/ref=sr_1_1?dib=eyJ2IjoiMSJ9.P2GDYGeYwXtubMtru0LBHMYunvC6ZCsDEnpQP6NgDlzgcKn8OheH7fmrEsyVXWaKccpiygRyKmVIn5iClPBg_3vGxW869zxK0PBPgLCYh-qIJZcNaF-rJ9jNoQd-l4txYUO7ZBlRLqQSjPxH5ZorrmOImvF5291d_t_QuFVAH3n_dUPjgdJYBE5jaFmsgE3JDOGtkns4n9YNXjr65eE3c6OxPClxPC5PO9nZkhuyjiQ.QUrJGT3UJ5zbDeAtXbJnFb1e0kie8hTfAww_EwbQGDI&dib_tag=se&keywords=gaming+laptop&qid=1720107714&rnid=2421885011&sr=8-1"

    RESPONSE: requests.Response = requests.get(URL)
    SOUP: BeautifulSoup = BeautifulSoup(RESPONSE.content, "html.parser")
    REVIEWS: Any = SOUP.find("div", attrs={"class":"card-padding"})

    with open("t.html", "w+", encoding="UTF-8") as file:
        file.write(str(SOUP))

    Title = SOUP.find("span", attrs={"class":"a-size-large product-title-word-break"})
    All_Stars: Any = REVIEWS.find_all("span", attrs={'class':'a-icon-alt'})
    All_Short_Reviews: Any = REVIEWS.find_all("a", attrs={'class':'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'})

    Title = str(Title).split('<span class="a-size-large product-title-word-break" id="productTitle">')[1]
    Title = str(Title).split("</span>")[0]

    Stars: list = []
    Summary_Reviews: list = []

    for i in range(len(All_Stars)):
        Full_Html: str = str(All_Stars[i])

        REVIEW_TEXT: str | list[str] = Full_Html.split('<span class="a-icon-alt">')[1]
        REVIEW_TEXT: str | list[str] = REVIEW_TEXT.split("</span>")[0]

        Stars.append(REVIEW_TEXT)
        
        Rating = Stars[i].split("out of")[0]
        Stars[i] = float(Rating)


    for i in range(len(All_Short_Reviews)):
        Full_Html: str = str(All_Short_Reviews[i])
        
        SPAN_TAG: str = Full_Html.split("\n")[1].split("<span>")[1]
        REVIEW_TEXT: str | list[str] = SPAN_TAG.split("</span>")[0]
        Summary_Reviews.append(REVIEW_TEXT)
        

    MEAN_RATING = np.mean(Stars)
    
    Stars_And_Summary: zip[tuple] = zip(Stars, Summary_Reviews)

    return {
        "Title" : f"{Title}",
        "Stars And Summary" : list(Stars_And_Summary),
        "Mean Rating" : MEAN_RATING}
