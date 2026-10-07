terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Security Group autorisant HTTP (80) et SSH (22)
resource "aws_security_group" "web_sg" {
  name        = "nginx-flask-sg"
  description = "Allow HTTP and SSH traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami                    = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS us-east-1
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  # Script d'initialisation pour installer Docker & lancer l'application
  user_data = <<-EOF
              #!/bin/bash
              apt-get update -y
              apt-get install -y docker.io docker-compose git
              systemctl start docker
              systemctl enable docker
              EOF

  tags = {
    Name = "nginx-flask-mysql-server"
  }
}

output "instance_ip" {
  value       = aws_instance.app_server.public_ip
  description = "Adresse IP publique du serveur AWS"
}
