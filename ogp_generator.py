# 実際のAPIはもっとちゃんと作ってます（イメージを掴むためのサンプルです）
from fastapi import FastAPI
from pydantic import BaseModel

# さっきのOGP生成関数
from sample_image import convert_ogp
# import upload

# docは公開する必要ない（しちゃ🙅）なので使いません
app = FastAPI(docs_url=None, redoc_url=None)


@app.post('/create')
def create(title: str, content: str, start_date: str, start_time: str, organizer_name: str, is_greeter: bool, color: str):
    image_byte = convert_ogp(title, content, start_date, start_time, organizer_name, is_greeter, color, 'tem.svg')
    # print(age)
    # image_byte = convert_ogp(form.area, form.age, form.period, 'templates/ogp.svg.j2')    
    # 取得したimageを何かしらの方法でアップロード
    # upload(image_byte)
    return {'status': 'ok'}


if __name__ == '__main__':
    import os
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=os.getenv('PORT', 3000))