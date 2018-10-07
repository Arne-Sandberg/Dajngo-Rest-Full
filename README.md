# Dajngo-Rest-Full
Repositório dos tutoriais sobre Django Rest Full e suas relações ( Neo4j,  )

1) para poder clonar o repositorio é preciso se conectar ao github 

Gere a chave
	  - $ ssh-keygen -t rsa -C "robson.lopes@edu.unifor.br"
		- você quer que ele crie nesse repositório ? sim
		- Defina a senha, (melhor colocar nada)

settings do github
	- va no github > canto superior direito (na foto) > settings 
	- SSH anf GPG Keys
	- click > New ssh key

Copie o codigo do id_rsa
	- /home/great/.ssh/  >   id_rsa.pub  
  - $ cat /home/great/.ssh/id_rsa.pub

Conecte ao github  
	 - $ ssh -T git@github.com
	 - ao se conectar pelo git a imagem da chave fica verde
   - OBS: eu tive o erro $ permission denied (publickey).
   - Para resolver isso eu tive que gerar uma nova chave, e conectar novamente ao github reiniciar o computador. 
