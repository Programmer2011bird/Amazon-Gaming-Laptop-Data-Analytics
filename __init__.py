from Scraper import Scrape

def Return_Data():
    Info = Scrape()
    Title = Info["Title"]
    Stars_Summary = Info["Stars And Summary"]
    Mean_Rating = Info["Mean Rating"]
    
    print("-" * 140)
    print(f" ---- Title ---- : {Title}")
    print("-" * 140)
    print(" ---- Summary Reviews ---- ")

    for i in range(len(Stars_Summary)):
        Star_And_Summary = Stars_Summary[i]
        Rating = Star_And_Summary[0]
        Summary = Star_And_Summary[1]
        
        print(f"{Summary} : {Rating}")
    
    print("-" * 140)
    print(f" ---- Mean Rating : {Mean_Rating} ---- ")
    print("-" * 140)

if __name__ == "__main__":
    Return_Data()