#!/bin/bash


deploy_dev(){
    gunicorn \
        --bind 0.0.0.0:8000 \
        --reload donationpage.service:app \
        --timeout 600 --max-requests 1000 \
        --log-level debug
        --workers=2
}

deploy_dev