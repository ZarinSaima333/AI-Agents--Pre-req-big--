I can run ollama either by ollama in my pc or i can use it by docker.

Using ollam by docker:
1)installing docker desktop
2)To ckeck if everything running proprely docker, docker --version in terminal
3)ollama docker then docker hub 


ollama/ollama(image name)

1)docker run ollama/ollama
2)docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
after running this ill get an id.
27a930f0df5dba8be2d45a975f058123a7dc0f85f6bc50289a4d12967d2283df

4)openwebui: interface layer to run ollama, Open WebUI can be easily deployed using Docker containers, providing a self-hosted, feature-rich interface for interacting with various large language models (LLMs). It will run on [localhost](http://localhost:3000/)
search openwebui docker->docker
*docker pull ghcr.io/open-webui/open-webui:main
*docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
b766be9ab54a60f516af47b22050ead39459166b8aa0c7aa1543b67fd6d3b6e6

3.admin setup. settings theke choose a model (download sign)

3.1. ollama-> model-> gemma
3.2. gemma:2b admin pannel e (Pull a model from Ollama.com) (download)