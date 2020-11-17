IMAGE_NAME=my_web_env
IMAGE_TAG=1
IMAGE=$(IMAGE_NAME):$(IMAGE_TAG)

build:
	docker build -t $(IMAGE) .

run:
	docker run --publish 8080:5000 --rm $(IMAGE)

custom:
	docker run --publish 8080:5000 --env GREETING="Hello, AWS" --rm $(IMAGE)
