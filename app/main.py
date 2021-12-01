from fastapi import FastAPI
import cairosvg
from jinja2 import Environment, FileSystemLoader
import tempfile
import os
from pydantic import BaseModel
import base64
import urllib

class Item(BaseModel):
    title: str
    content: str
    start_date: str
    start_time: str
    organizer_name: str
    is_greeter: bool
    color: str
    avatar: str
    thumbnail: str

app = FastAPI(docs_url=None, redoc_url=None)

@app.post('/create')
async def create(item: Item):
    print("Request Param")
    print(item)
    image = convert_ogp(item.title, item.content, item.start_date, item.start_time, item.organizer_name, item.is_greeter, item.color, item.avatar, item.thumbnail, 'templates/ticket.svg')
    return base64.b64encode(image)


def get_image_url(url):
    default_url = "https://d5s0godkksmnh.cloudfront.net/profile_images/default-avatar.png"
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("Error occured: ")
        print(url)
        return default_url
    return url


def convert_ogp(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str,avatar: str, thumbnail: str, template_file: str):
    # テンプレファイルと引数からテキストを生成
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    ogp_template = env.get_template(os.path.basename(template_file))
    title1, title2, title3 = title[:14], title[14:27], title[27:]
    title1 = title1.replace("&", "&amp;")
    title1 = title1.replace(">", "&gt;")
    title1 = title1.replace("<", "&lt;")
    title2 = title2.replace("&", "&amp;")
    title2 = title2.replace(">", "&gt;")
    title2 = title2.replace("<", "&lt;")
    escape_chars = ":/"
    avatar = urllib.parse.quote_plus(avatar, escape_chars)
    thumbnail = urllib.parse.quote_plus(thumbnail, escape_chars)

    if (title3 != "") :
         title2 = title2 + " ..."
    content, content2 = content[:18], content[18:]
    if (content2 != "") :
         content = content + " ..."

    name, name2 = organizer_name[:7], organizer_name[7:]
    if (name2 != "") :
         name = name + " ..."

    avatar_url = get_image_url(avatar)
    thumbnail_url = get_image_url(thumbnail)

    ogp_context = ogp_template.render(title=title1, title2 = title2, content=content, start_d=start_date,
                                      start_t=start_time, name=name, condition=is_greeter, avatar=avatar_url, thumbnail=thumbnail_url, color=color)

    with tempfile.NamedTemporaryFile('w') as f:
        f.write(ogp_context)
        f.flush()
        image_bytes = cairosvg.svg2png(url=f.name, scale=0.3)
    return image_bytes

if __name__ == '__main__':
    import os
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=os.getenv('PORT', 3000))
