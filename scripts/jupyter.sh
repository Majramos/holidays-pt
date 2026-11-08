#!/usr/bin/env bash

set -euo pipefail

script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd "$script_directory/.." && pwd)"
image_name="holidays-pt-jupyter:latest"
container_name="holidays-pt-jupyter"
user_id="$(id -u)"
group_id="$(id -g)"

build_image() {
    podman build \
        --build-arg "UID=$user_id" \
        --build-arg "GID=$group_id" \
        --tag "$image_name" \
        --file "$script_directory/Containerfile.jupyter" \
        "$project_root"
}

run_container() {
    podman run \
        --rm --interactive --tty --userns=keep-id \
        --name "$container_name" \
        --publish 2345:8888 \
        --volume "$project_root:/home/pyuser/notebook:Z" \
        "$image_name"
}

clean_resources() {
    if podman container exists "$container_name"; then
        podman rm --force "$container_name"
    fi

    if podman image exists "$image_name"; then
        podman rmi "$image_name"
    fi
}

if (( $# != 1 )); then
    printf 'Usage: %s {build|run|clean}\n' "$0" >&2
    exit 2
fi

case "$1" in
    build)
        build_image
        ;;
    run)
        if ! podman image exists "$image_name"; then
            read -r -p "The image does not exist. Build it now? [y/N] " answer
            case "$answer" in
                [Yy]|[Yy][Ee][Ss])
                    build_image
                    ;;
                *)
                    printf 'The image was not built.\n' >&2
                    exit 1
                    ;;
            esac
        fi
        run_container
        ;;
    clean)
        clean_resources
        ;;
    *)
        printf 'Usage: %s {build|run|clean}\n' "$0" >&2
        exit 2
        ;;
esac
