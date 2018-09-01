#!/env/bin sh
export REGISTRY=simonfong6
export REPOSITORY=life-tracker
export TAG=base
docker run -it \
    --mount type=bind,source="$(pwd)"/..,target=/app \
    $REGISTRY/$REPOSITORY:$TAG