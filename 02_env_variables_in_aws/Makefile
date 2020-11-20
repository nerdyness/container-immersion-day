IMAGE_NAME=my_web_env
IMAGE_TAG=1
IMAGE=$(IMAGE_NAME):$(IMAGE_TAG)
ECR_NAME=immersion_day

ecr:
	aws ecr create-repository --repository-name $(ECR_NAME)

build:
	docker build -t $(IMAGE) .

run:
	docker run --publish 8080:80 --rm $(IMAGE)

custom:
	docker run --publish 8080:80 --env GREETING="Hello, AWS" --rm $(IMAGE)
