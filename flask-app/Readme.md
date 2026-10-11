# Simple Flask App with Docker

A step-by-step guide to creating a Flask web application and containerizing it with Docker.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started With Flask](#getting-started-with-flask)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Understanding the Flask Application](#understanding-the-flask-application)
  - [Run the Flask Application](#run-the-flask-application)
- [Containerization with Docker](#containerization-with-docker)
  - [Create a Dockerfile](#create-a-dockerfile)
  - [Build a Docker Image](#build-a-docker-image)
  - [Create a Docker Container](#create-a-docker-container)
  - [Testing the Container](#testing-the-container)
- [Share Your Docker Image](#share-your-docker-image)
- [Pulling and Running the Docker Image](#pulling-and-running-the-docker-image)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository provides a step-by-step guide to creating a simple Flask web application and containerizing it using Docker. It covers the entire process, from setting up the Flask app to building and running the Docker container.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)

## Getting Started With Flask

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/chesah_kalu/Simple-Flask-App-Docker.git
```

### Install Dependencies

To install dependencies and modules required for the flask app work, run the command bellow to install the dependencies listed inside the ```requirements.txt``` file

```bash
pip3 install -r requirements.txt
```

### Understanding the Flask Application

Before running the Flask application, let's briefly understand the code in `product_list_app.py`. The Flask application provides a REST API for managing a list of products. It allows you to perform CRUD (Create, Retrieve, Update, Delete) operations on the product data.

#### API Endpoints

The Flask application exposes the following API endpoints:

- `GET /products`: Retrieves all products.
- `GET /products/<id>`: Retrieves a specific product by ID.
- `POST /products`: Creates a new product.
- `PUT /products/<id>`: Updates an existing product by ID.
- `DELETE /products/<id>`: Deletes a product by ID.

#### Application Logic

Here's a high-level overview of how the Flask application works:

- **GET /products**: When you access this endpoint, the application returns a JSON representation of all the products in the `products` list.

- **GET /products/<id>**: This endpoint allows you to retrieve a specific product by providing its ID as a parameter in the URL. If the product with the given ID exists, it is returned as JSON. Otherwise, an error message is returned.

- **POST /products**: To create a new product, you need to send a POST request to this endpoint with a JSON request body containing the `name` and `price` of the product. If the request is valid, the new product is added to the `products` list and returned as JSON with a 201 status code (created).

- **PUT /products/<id>**: To update an existing product, send a PUT request to this endpoint with the product's ID as a parameter in the URL and a JSON request body containing the updated `name` and `price` values. If a product with the provided ID is found, it is updated with the new values and returned as JSON with a 200 status code (OK).

- **DELETE /products/<id>**: To delete a product, send a DELETE request to this endpoint with the product's ID as a parameter in the URL. If a product with the provided ID is found, it is removed from the `products` list, and a success message is returned with a 200 status code (OK).

#### Code Comments

The code in `product_list_app.py` is well-commented, providing detailed explanations of how each endpoint and piece of logic works. You can refer to these comments for a more in-depth understanding of the application's inner workings.

This summary should help you get started with understanding the Flask application and its API endpoints.

### Run the Flask Application

Start the Flask application:

```bash
python3 product_list_app.py
```

The application will be accessible at http://localhost:5070. You can test it by accessing the API endpoints through your web browser or using tools like curl or Postman. You can also use the [Swagger UI](https://swagger.io/tools/swagger-ui/) to test the API endpoints.  



## Containerization with Docker

### Create a Dockerfile

To containerize the flask application, a Dockerfile file has to be created in the project directory.
This Dockerfile [Dockerfile](Dockerfile) :
- Uses the official Python 3.9 image as the base image.
- Sets the working directory to /app in the container.
- Copies the current directory (including your Flask application code) into the container.
- Installs the dependencies specified in requirements.txt (create this file if you haven't).
- Exposes port 5070 (the port your Flask app is running on).
- Specifies the command to run your Flask application.

### Build a Docker Image

In your terminal, navigate to the directory containing your Dockerfile and run the following command to build a Docker image:

```bash
docker build -t product-list-app:v1 .
```
- This command builds a Docker image using the Dockerfile in the current directory.
- The `-t` flag is used to tag the image with a name of your choice. In this case, the image is tagged with the name `product-list-app`.
- The `.` at the end of the command indicates that the Dockerfile is in the current directory.
- The build process may take a few minutes to complete. Once it's done, you should see a message indicating that the build was successful.
- The image is now available locally on your machine. You can view it by running the `docker images` command.
- This image can be used to create containers that run your Flask application.
- `:v1` is the version of the image. This is optional, but it's a good practice to tag your images with a version number. This allows you to update or differentiate images, ensuring you can reference specific versions. When you update your image with same name, you can tag it with a new version
number (e.g., v2). 
- You can list all the images on your machine using the `docker images` command.

### Create a Docker Container

Now that you have a Docker image, you can use it to create a container that runs your Flask application. To do this, run the following command:

```bash
docker run -d -p 5070:5070 product-list-app:v1
```
- This command creates a v1 container using the `product-list-app` image you built earlier.
- The `-d` flag is used to run the container in detached mode (in the background).
- The `-p` flag is used to map the host port 5070 to the container port 5070. This allows you to access the Flask application running inside the container at http://localhost:5070.

### Testing the Container

The container is now running in the background. You can view it by running the `docker ps` command.  You can also view all the containers on your machine using the `docker ps -a` command.
- You can test it by accessing it through your web browser at http://localhost:5070. If you followed the example Dockerfile above, your Flask app should be accessible on port 5070.
- You can also use curl or tools like Postman to make HTTP requests to your Flask API endpoints running in the Docker container.
- You can start, stop, restart and remove the container using the `docker start`, `docker stop`, `docker restart` and `docker rm` commands respectively with the container ID or name.
- This container is now a self-contained unit that can be run on any system that supports Docker. This is the power of containerization. You can now share your Docker image with others, and they can run it as a container on their machine.

## Share Your Docker Image

You can share your Docker image with others by pushing it to a Docker registry like Docker Hub or any other Container registry. To do this, you need to create a repository on Docker Hub and then push your image to it. This will enable others to pull your image and run it as a container on their machine. Which establishes the concept of containerization.

First create a repository on Docker Hub GUI. Fill in the details for your repository, including a name (e.g., "product-list-app"), a description, and visibility settings (public or private). Then, log in to Docker Hub from your terminal using the following command:

```bash
docker login
```
- This command will prompt you to enter your Docker Hub username and password. Once you've entered them, you should see a message indicating that you've successfully logged in.

Next, before pushing your Docker image to Docker Hub, you need to tag it with the repository name you created. 
Tagging is especially useful when you want to update or differentiate images, ensuring you can reference specific versions.

Use the following command to tag your image:

```bash
docker tag product-list-app:v1 <your-docker-hub-username>/product-list-app:v1
```

- This command tags your Docker image with the name of your Docker Hub username and the name of the repository you created earlier.
- The first part is the name of the image you want to tag with its version. Then include the dockerhub username and the last part is the name of the repository you created on Docker Hub, with the version number you want to tag it with.

You can now push your Docker image to Docker Hub using the following command:

```bash
docker push <your-docker-hub-username>/product-list-app:v1
```

- This command pushes your Docker image to Docker Hub specifying the intended repository with its version. Once the push is complete, you should see a message indicating that the push was successful.

You can also push your Docker image to Docker Hub without tagging it. To do this, use the following command:

```bash
docker push <your-docker-hub-username>/repo-name/image-name:tag
```

You can now view your Docker image on Docker Hub. You can also pull it from Docker Hub and run it as a container on your machine.

## Pulling and Running the Docker Image

To pull your Docker image from Docker Hub, use the following command:

```bash
docker pull <the-docker-hub-username>/image-name:tag
```

- This command pulls a Docker image from Docker Hub and saves it locally on your machine.

You can now run the Docker image as a container using the following command:

```bash
docker run -d -p 5070:5070 <your-docker-hub-username>/product-list-app
```

- This command runs your Docker image as a container on your machine. You can access it through your web browser at http://localhost:5070.

That's it! You've containerized your Flask application, and you can now run it on any system that supports Docker.

## Contributing

Feel free to contribute to this project by opening issues or pull requests.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.


