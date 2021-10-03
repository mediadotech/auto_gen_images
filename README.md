
# Run sample in docker

## Build image using Dockerfile
```bash
$ docker build -t your_image_name .
```

## Run the image

```bash
$ docker run -d --name your_container_name -p 3000:3000 your_image_name
```
