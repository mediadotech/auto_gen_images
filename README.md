
# Run sample in docker

## Build image using Dockerfile
```bash
$ docker build -t your_image_name .
```

## Run the image

```bash
$ docker run -d --name your_container_name -p 3000:3000 your_image_name
```

# Sample request body

```
{
    "title": "異次元のプレイで魅せる超絶技",
    "content": "Official髭男dism LIVE TOUR 2021ダイ...",
    "start_date": "2020.09.22",
    "start_time": "10:30",
    "organizer_name": "津野 和範",
    "is_greeter": false,
    "color": "#FFAF20",
    "avatar": "",
    "thumbnail": ""
}
```