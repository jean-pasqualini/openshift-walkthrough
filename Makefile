build:
	docker build --file ./docker/Dockerfile -t docker.io/username/cat-game:latest ./
push:
	docker push docker.io/username/cat-game:latest
run:
	docker run -p "5000:5000" --rm -it docker.io/username/cat-game:latest 
