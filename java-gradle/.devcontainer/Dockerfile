FROM eclipse-temurin:21-jdk

# Create a non-root user (VS Code expects this)
RUN useradd -m vscode

# Install unzip for Gradle wrapper
RUN apt-get update && apt-get install -y unzip

USER vscode
