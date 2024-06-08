provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_instance" {
  ami             = "ami-00beae93a2d981137" # Ubuntu Server 20.04 LTS (HVM)
  instance_type   = "t2.micro"
  key_name        = var.key_name
  security_groups = [aws_security_group.app_sg.name]
  monitoring      = "true"

  tags = {
    Name        = "bootcamp_m"
    Terraform   = "true"
    Environment = "dev"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y docker.io
              apt-get install -y docker-compose
              systemctl start docker
              systemctl enable docker
              EOF
}

resource "aws_security_group" "app_sg" {
  name        = "bootcamp_m_sg"
  description = "Allow HTTP and SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
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
