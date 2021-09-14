# 実際のコードとは異なります（あくまでサンプルです）

import cairosvg
from jinja2 import Environment, FileSystemLoader
import tempfile
import os

def convert_ogp(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str, template_file: str):
    # テンプレファイルと引数からテキストを生成
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    ogp_template = env.get_template(os.path.basename(template_file))
    ogp_context = ogp_template.render(title=title, content=content, start_d=start_date, start_t=start_time, name=organizer_name, condition=is_greeter, color=color)
    # ogp_context = '<svg xmlns="http://www.w3.org/2000/svg" width="965" height="430" viewBox="0 0 965 430"><rect width="965" height="430" rx="20" fill="#dcdce6"/></svg>'

   # TemporaryFileとして書き出して後byteでもらう
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(ogp_context)
        f.flush()
        image_bytes = cairosvg.svg2png(url=f.name, write_to="ticket.png")
    return image_bytes