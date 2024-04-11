# WorldOfGame - CI\CD project
### Refined and expanded my expertise in DevOps through ongoing practice and hands-on exercises, starting from my DevOps course and continuing beyond.

In this project, I've delved into the creation of CI/CD pipelines, leveraging Python for scripting and Microsoft Playwright for testing. 
Additionally, I've explored Docker containers and images, along with Docker Hub, and ventured into different cloud service providers and OS architectures, which I'll discuss in detail later on.

## What this pipeline is doing?

The pipeline implemented in this project comprises the following stages:

1. **Checkout**:
    - Pulls this repository.

2. **Install Dependencies**:
    - Sets up a virtual environment.
    - Activates the virtual environment and installs dependencies from the requirements file.
    - Installs pytest-playwright plugin and Playwright for testing the output of a Python game (tests performed over a mockup file).
    - Creates a dummy scores file for testing purposes.

3. **Build**:
    - Constructs the Docker image using a compose file, which utilizes a Dockerfile.
    - The Dockerfile sets up a Python environment with Flask installed, copies Python scripts and a text file into the container, and executes a script (MainScores.py - an HTTP server serving scores from a file) upon container startup.

4. **Run**:
    - Runs the container mentioned in the previous stage - an HTTP server serving scores from a file.

5. **Test**:
    - Executes the Playwright test (e2e.py) in the virtual environment. The pipeline fails if the exit code is 1.

6. **Finalize**:
    - Concludes the pipeline by shutting down the Flask container.
    - Utilizes Jenkins Pipeline syntax with the withCredentials block to securely access Docker Hub credentials.
    - Logs into Docker Hub using the provided username and password.
    - Pushes the Docker images defined in a docker-compose.yml file to Docker Hub.


# Journey of Optimizing Jenkins Nodes with Cloud Providers

In the quest for optimal Jenkins node management, I embarked on a journey through various cloud service providers. Here's a technical dive into my experiences and the solutions I implemented.

## AWS EC2: The Beginning

Initially, I leveraged AWS EC2 as the cornerstone of my Jenkins infrastructure. A single EC2 instance served as the primary Jenkins node, handling both management tasks and job executions.

## Transition to GCP: Dockerized Efficiency

Seeking enhanced flexibility and efficiency, I migrated to Google Cloud Platform (GCP). Here, I adopted a setup comprising a single compute instance running Ubuntu Linux on AMD64 architecture. Within this environment, I deployed two Docker containers housing Jenkins, utilizing the official Jenkins image from Docker Hub ([jenkins/jenkins](https://hub.docker.com/r/jenkins/jenkins)). 

## Exploring OCI: Architectural Diversification

In a quest for experimentation and diversification, I turned to Oracle Cloud Infrastructure (OCI). Here, I encountered a unique challenge: the compute instance was based on a distinct OS architecture (Linux/ARM64). Consequently, I had to devise a tailored solution by provisioning a new Docker container specifically configured for my Jenkins Agent.

# Another challenge I encounter and how I solved it - yes I "DinD"

## I "DinD" it - DinD stnads for Docker-in-Docker....
For further reading you can follow the blogpost written by [Jérôme Petazzoni](https://github.com/jpetazzo) at [this link](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)

### How I DinD it
So, my pipeline, when running within a containarized Jenkins Agent, will have to create and run additional container (as mentioned above in stage 4 of my pipeline).
To allow it to perform this task youll have to follow Jérôme's instructions:
> Simply put, when you start your CI container (Jenkins or other), instead of hacking something together with Docker-in-Docker, start it with:
```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock ...
```
> Now this container will have access to the Docker socket, and will therefore be able to start containers. 
Except that instead of starting “child” containers, it will start “sibling” containers.

If youre lazy like myself, just keep on reading... Do not worry! I got your back... :)
In the next section ("To make things even simplier") I have provided you with prebuilt compose file that mount that container for you!

# Simplifying Future Deployments

To enhance future deployments and alleviate setup complexities, I took proactive measures. 
I have pushed a multi-architecture image to docker hub, I did it using the experimental feature of docker called docker "manifest".
Basically, on each one of the platform I worked on (GCP and OCI) I have created and pushed the relevant architecture image, and than, using the manifest feature, I have combined them under same manifest and pushed them as a single repository and tag in my dockerhub (mulik6/myjenkinslave:latest).
> "Docker manifests are particularly useful for multi-platform and multi-architecture applications, where the same application needs to run on different types of hardware or operating systems. The manifest ensures that Docker pulls the correct image for the platform it is running on, ensuring compatibility and consistency across different environments."

You can pulled this image at [mulik6/myjenkinslave](https://hub.docker.com/r/mulik6/myjenkinslave/tags), ensuring seamless replication of my Jenkins Agent node configurations.

# To make things even simplier
I have created and pushed a Docker Compose file within the [Utilities](https://github.com/Mulik6/WorldOfGame/tree/master/Utilities) directory (jenkins_ms_manifested_compose.yml).
This Docker Compose file sets up a Jenkins environment with a master instance (jenkins_master) and a slave instance (jenkins_slave). 
The master is exposed on ports 8080 and 50000, and the slave mounts the Docker socket to enable container management.
Moreover, the 'jenkins_master' container will be pulled from the 'jenkins/jenkins:lts-jdk17' rpeository, and the 'jenkins_slave' will be pulled from my previously created rpeository 'mulik6/myjenkinslave:latest'.

--------

## Jenkins Agent Linux Prerequisites

```bash
apt update -y
apt upgrade -y

# Install python, PIP and virtual env:
apt install -y python3
apt install -y python3-pip
apt install -y python3-venv

# Install docker:
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run

# Install docker compose:
apt update -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
### For Linux/arm64
```bash
add-apt-repository "deb [arch=arm64] https://download.docker.com/linux/ubuntu focal stable"
```
### For Linux/AMD64
```bash
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
apt install -y apt-transport-https ca-certificates curl software-properties-common
apt install -y docker-ce

curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
