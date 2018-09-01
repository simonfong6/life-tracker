#!/env/bin sh
export REGISTRY=simonfong6
export REPOSITORY=life-tracker
export TAG=base
docker run -it \
    --mount type=bind,source="$(pwd)"/..,target=/app \
    -p 8080:8080 \
    $REGISTRY/$REPOSITORY:$TAG