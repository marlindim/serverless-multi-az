Serverless Multi-AZ Architecture on AWS

This project demonstrates how to design and deploy a highly available, fault-tolerant architecture using AWS with Terraform.
It covers:

1.Multi-AZ VPC and subnets

2.EC2 instances behind Auto Scaling and Load Balancer

3.Serverless components (AWS Lambda + DynamoDB)

4.Architecture Overview

5.VPC: Created with public subnets across multiple Availability Zones.

6.Security Groups: Allow HTTP (80) and SSH (22) access.

7.EC2 Instances: Deployed with Apache installed, serving a static page.

8.Auto Scaling Group (ASG): Automatically scales EC2 instances across AZs.

9.Load Balancer (ALB): Distributes traffic across EC2 instances.

10.Serverless Component: AWS Lambda triggered by S3 bucket upload, storing data in DynamoDB.



Prerequisites:

Terraform v1.x+ installed

AWS CLI configured with credentials and correct region

A public key at ~/.ssh/id_rsa.pub for EC2 access (or update the path in main.tf)


Deployment:

1.Initialize Terraform:
terraform init

2.Validate configuration:
terraform validate

3.Plan the infrastructure:
terraform plan -out plan.tfplan

4.Apply the infrastructure:
terraform apply plan.tfplan

5.Access the EC2 public IP or Load Balancer DNS name:
curl http://<public_ip_or_alb_dns>

Cleanup

To destroy all the resources and avoid ongoing AWS costs:
terraform destroy


