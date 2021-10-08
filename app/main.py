from fastapi import FastAPI
import cairosvg
from jinja2 import Environment, FileSystemLoader
import tempfile
import os
from pydantic import BaseModel
import base64

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
    image = convert_ogp(item.title, item.content, item.start_date, item.start_time, item.organizer_name, item.is_greeter, item.color, 'templates/ticket.svg')
    return base64.b64encode(image)


def convert_ogp(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str, template_file: str):
    # Setup default environment param
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    ogp_template = env.get_template(os.path.basename(template_file))
    title1, title2, title3 = title[:14], title[14:27], title[27:]
    if (title3 != "") :
         title2 = title2 + " ..."
    content, content2 = content[:18], content[18:]
    if (content2 != "") :
         content = content + " ..."

    ogp_context = ogp_template.render(title=title1, title2 = title2, content=content, start_d=start_date,
                                      start_t=start_time, name=organizer_name, condition=is_greeter, color=color)
   # Write temporary file and get image bytes later
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(ogp_context)
        f.flush()
        # cairosvg.svg2png(url=f.name, write_to="ticket.png", scale=0.6)
        image_bytes = cairosvg.svg2png(url=f.name, scale=0.3)
    return image_bytes    

if __name__ == '__main__':
    import os
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=os.getenv('PORT', 3000))