I can run ollama either by ollama in my pc or i can use it by docker.

Using ollam by docker:
1)installing docker desktop
2)To ckeck if everything running proprely docker, docker --version in terminal
3)ollama docker then docker hub 


ollama/ollama(image name)

1)docker run ollama/ollama
2)docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
after running this ill get an id.

4)openwebui: interface layer to run ollama