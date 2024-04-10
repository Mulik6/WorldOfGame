# WorldOfGame - CI\CD project

### DevOps-Experts Course Project 2022
### Created as Part of my DevOps course for practice purposes.

In this project, I've delved into the creation of CI/CD pipelines, leveraging Python for scripting and Microsoft Playwright for testing. 
Additionally, I've explored Docker containers and images, along with Docker Hub, and ventured into different cloud service providers and OS architectures, which I'll discuss in detail later on.

## TL;DR

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

Initially, I leveraged AWS EC2 as the cornerstone of my Jenkins infrastructure. A single EC2 instance served as the primary Jenkins node, handling both management tasks and job executions seamlessly.

## Transition to GCP: Dockerized Efficiency

Seeking enhanced flexibility and efficiency, I migrated to Google Cloud Platform (GCP). Here, I adopted a setup comprising a single compute instance running Ubuntu Linux on AMD64 architecture. Within this environment, I deployed two Docker containers housing Jenkins, utilizing the official Jenkins image from Docker Hub ([jenkins/jenkins](https://hub.docker.com/r/jenkins/jenkins)). This configuration streamlined resource allocation and facilitated smoother Jenkins operations.

## Exploring OCI: Architectural Diversification

In a quest for experimentation and diversification, I turned to Oracle Cloud Infrastructure (OCI). Here, I encountered a unique challenge: the compute instance was based on a distinct OS architecture (Linux/ARM64). Consequently, I had to devise a tailored solution by provisioning a new Docker container specifically configured for the Jenkins Agent.

## Simplifying Future Deployments

To enhance future deployments and alleviate setup complexities, I took proactive measures. Both Jenkins Agent containers utilized in my deployments are now available on Docker Hub. You can access them at [mulik6/myjenkinslave](https://hub.docker.com/r/mulik6/myjenkinslave/tags), ensuring seamless replication of my optimized Jenkins node configurations.

This journey underscores the importance of adaptability and innovation in optimizing CI/CD infrastructure across diverse cloud environments. Through strategic adjustments and proactive solutions, I've unlocked efficiency and scalability in Jenkins node management.


