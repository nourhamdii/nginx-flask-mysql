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

# Exemple de création d'instance EC2 pour héberger le projet
resource "aws_instance" "app_server" {
  ami           = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS us-east-1
  instance_type = "t2.micro"

  tags = {
    Name = "nginx-flask-mysql-server"
  }
}

output "instance_ip" {
  value       = aws_instance.app_server.public_ip
  description = "Adresse IP publique du serveur AWS"
}
