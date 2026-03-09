from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

storylink_tags = soup.select(selector="span.titleline>a")
story_scores = soup.select(selector = "span.score")

tags = []
for index, tag in enumerate(storylink_tags):
    tags.append({
        "headline":tag.text,
        "storylink":tag.get("href"),
        "points" : int(story_scores[index].text.split(" ")[0])
    })


ordered_tags = sorted(tags, key=lambda x: x['points'], reverse=True)

print(ordered_tags[0]['headline'])