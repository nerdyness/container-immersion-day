IMAGE_NAME=my_secrets
IMAGE_TAG=1
IMAGE=$(IMAGE_NAME):$(IMAGE_TAG)

build:
	docker build -t $(IMAGE) .

run:
	docker run -v ~/.aws/:/root/.aws --publish 8080:80 --rm $(IMAGE)

custom:
	docker run -v ~/.aws/:/root/.aws --publish 8080:80 --env GREETING="Hello, AWS" --rm $(IMAGE)
