# Docker verification

Fill this in after you build and run your container (see README.md,
"Part 2 — Dockerfile"). This is how we confirm your container actually works, since an
automated grader running in a sandbox may not always have Docker-in-Docker
available.

## Build

Paste the command you ran and its final output line (the one showing the
built image ID/tag):

```
docker build -t week6-detector .
=> => naming to docker.io/library/week6-detector:latest
```

## Run

Paste the command you used to start the container (should map a host port
to the container's 8080):

```
docker run --rm -p 8080:8080 week6-detector
```

## Verify

Paste the exact `curl` commands and their JSON output for both endpoints,
run against the running container (not against `python src/app.py` directly
— the point is to prove the *container* works):

```
curl.exe http://localhost:8080/health

{"status":"ok"}

curl.exe -F "image=@data/fixtures/camera_A_daylight/000.jpg" http://localhost:8080/detect

{"count":6,"detections":[{"bbox":[63,10,38,20],"category_id":4,"id":0,"image_id":0,"score":0.98},{"bbox":[82,61,40,23],"category_id":10,"id":1,"image_id":0,"score":0.98},{"bbox":[59,113,42,17],"category_id":0,"id":2,"image_id":0,"score":0.98},{"bbox":[187,120,35,13],"category_id":7,"id":3,"image_id":0,"score":0.98},{"bbox":[216,139,31,11],"category_id":5,"id":4,"image_id":0,"score":0.98},{"bbox":[232,155,30,17],"category_id":6,"id":5,"image_id":0,"score":0.98}]}
```
