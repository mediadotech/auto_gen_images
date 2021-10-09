# 実際のコードとは異なります（あくまでサンプルです）

import cairosvg
from jinja2 import Environment, FileSystemLoader
import tempfile
import os
from wand.image import Image
from wand.display import display


def convert_ogp(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str,avatar: str, thumbnail: str, template_file: str):
    # テンプレファイルと引数からテキストを生成
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    ogp_template = env.get_template(os.path.basename(template_file))
    title1, title2, title3 = title[:14], title[14:27], title[27:]
    if (title3 != "") :
         title2 = title2 + " ..."
    content, content2 = content[:18], content[18:]
    if (content2 != "") :
         content = content + " ..."

    ogp_context = ogp_template.render(title=title1, title2 = title2, content=content, start_d=start_date,
                                      start_t=start_time, name=organizer_name, condition=is_greeter, avatar=avatar, thumbnail=thumbnail, color=color)
    # ogp_context = '<svg xmlns="http://www.w3.org/2000/svg" width="965" height="430" viewBox="0 0 965 430"><rect width="965" height="430" rx="20" fill="#dcdce6"/></svg>'

    # f = open("myfile.svg", "a")
    # f.write(ogp_context)

   # TemporaryFileとして書き出して後byteでもらう
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(ogp_context)
        f.flush()
        image_bytes = cairosvg.svg2png(url=f.name, write_to="ticket.png", scale=0.5)
        # image_bytes = cairosvg.svg2png(url=f.name, scale=0.3)
    return image_bytes    


convert_ogp(title="異次元プレイで魅せる超絶技",
            content="異次元プレイで魅せる超",
            start_date="2020.09.22",
            start_time="10:30",
            organizer_name="津野 和範",
            is_greeter=True,
            color="#FFAF20",
            avatar="https://cdn.dribbble.com/users/1787323/screenshots/16239421/media/5abdea189c3ffdd5b0754681edae6765.png",
            thumbnail="https://d3by9h2nygf0qp.cloudfront.net/997b6baf-02af-44e2-92e3-870a8a61cf2d/Marcus_Miller_la_Villette_2019.png",
            template_file="templates/test.svg")
