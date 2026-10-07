user_data = <<-EOF
            #!/bin/bash
            apt-get update -y
            apt-get install -y docker.io docker-compose git
            systemctl start docker
            systemctl enable docker

            # Cloner le dépôt et démarrer les conteneurs
            cd /home/ubuntu
            git clone https://github.com/nourhamdii/nginx-flask-mysql.git app
            cd app
            docker-compose up -d
            EOF
