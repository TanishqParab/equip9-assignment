variable "aws_region" {
  description = "AWS region"
  default     = "ap-south-1"
}

variable "aws_ami_id" {
  description = "AMI ID for the EC2 instance"
  default     = "ami-0fd05997b4dff7aac" # Amazon Linux 2023
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ssh_public_key_path" {
  description = "Path to the SSH public key file"
  default     = "~/.ssh/deployer-key.pub"
}
