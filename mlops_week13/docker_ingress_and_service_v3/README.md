## to test the docker image.
docker build -t classifier-k8s:latest .

docker run -it --rm -p 7860:7860 classifier-k8s




### for mac

docker build --platform linux/amd64 -t classifier-k8s .
docker run --platform linux/amd64 -it --rm classifier-k8s:latest

