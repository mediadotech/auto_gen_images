from fastapi import FastAPI
import cairosvg
from jinja2 import Environment, FileSystemLoader
import tempfile
import os

app = FastAPI(docs_url=None, redoc_url=None)

@app.post('/create')
def create(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str):
    image = convert_ogp(title, content, start_date, start_time, organizer_name, is_greeter, color, 'template/ticket.svg')
    # WIP: upload image file to S3 with above image
    return {'status': 'ok'}


def convert_ogp(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str, template_file: str):
    # Setup default environment param
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    ogp_template = env.get_template(os.path.basename(template_file))

    # Replace template with desired data
    ogp_context = ogp_template.render(title=title, content=content, start_d=start_date, start_t=start_time, name=organizer_name, condition=is_greeter, color=color)

   # Write temporary file and get image bytes later
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(ogp_context)
        f.flush()
        image_bytes = cairosvg.svg2png(url=f.name, write_to="ticket.png")

if __name__ == '__main__':
    import os
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=os.getenv('PORT', 3000))