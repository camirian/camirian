# Context: Lightweight Python Image Synthesizer
FROM mcr.microsoft.com/devcontainers/python:1-3.10-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Layer 1: Inject the exact TrueType fonts the banner generator relies on
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-liberation2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Layer 2: Lock the image processing dependency natively (Pillow)
RUN pip install --no-cache-dir Pillow==10.4.0
