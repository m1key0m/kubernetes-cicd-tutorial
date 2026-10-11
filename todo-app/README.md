# ToDo App - Python

## Description

This is a simple ToDo list web application built with Flask, a Python web framework.

![todo-img](static/todo-img.png)

## Prerequisites

- Python 3.11.5

## Getting Started

1. Clone this repository to your local machine.

   ```
   git clone https://github.com/faizan35/todo-app-python.git
   ```

2. Navigate to the project directory.

   ```
   cd todo-app-python
   ```

3. Install dependencies.

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application.

   ```
   python app.py
   ```

5. Open your browser and go to [http://localhost:5000](http://localhost:5000) to access the ToDo app.

## Usage

- Add a new task by entering it in the input field and clicking the "Add" button.
- Complete a task by clicking the "Complete" button next to the task.
- Delete a task by clicking the "Delete" button next to the task.

## Docker

Build and run the Docker container.

```bash
docker build -t todo-app .
docker run -d -p 5000:5000 todo-app
```

## DockerHub

1. Pull the image from DockerHub.

   ```bash
   docker pull faizan44/todo-app
   ```

2. Run the Docker container.

   ```bash
   docker run -d -p 5000:5000 faizan44/todo-app
   ```

Access the app at [http://localhost:5000](http://localhost:5000).

## Deploy on Kubernetes

1. You must have a k8s cluster.
2. Clone this repo. `git clone https://github.com/faizan35/todo-app-python.git`
3. Navigate inside the `k8s` dir in the repo.
4. Create the namespace `kubectl create namespace todo`
5. Execute this command

   ```sh
   kubectl apply -f .
   ```

6. The application should be running on Port `30080`.

## Monitoring

sudo snap install helm --classic

helm repo update

---

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
