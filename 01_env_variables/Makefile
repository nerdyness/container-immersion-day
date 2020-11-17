IMAGE_NAME=my_env
IMAGE_TAG=1
IMAGE=$(IMAGE_NAME):$(IMAGE_TAG)

build:
	docker build -t $(IMAGE) .

run:
	docker run --rm $(IMAGE)

custom:
	docker run --rm --env GREETING="Hello, AWS" $(IMAGE)
