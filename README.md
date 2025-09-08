# Serverless Multi-AZ Architecture with Terraform

## 📌 Project Overview
This project demonstrates a highly available and fault-tolerant architecture deployed on **AWS** using **Terraform**.  
It includes:
- A **VPC** with public and private subnets across multiple **Availability Zones**.
- **Auto Scaling Group (ASG)** and **Application Load Balancer (ALB)** for web traffic distribution.
- A **serverless application** using **AWS Lambda** triggered by S3 events.
- A **serverless database** using **Amazon DynamoDB**.

---

## 🏗️ Architecture
![Architecture Diagram](./architecture-diagram.png)  
*(Add your Draw.io or Lucidchart diagram here)*

**Key Components:**
1. **VPC & Networking**
   - Multi-AZ setup with public/private subnets.
   - Internet Gateway & NAT Gateway for outbound internet access.
2. **Compute Layer**
   - Auto Scaling Group (EC2 instances) behind an Application Load Balancer.
   - Launch Template to configure EC2 instances.
3. **Serverless Layer**
   - AWS Lambda function triggered by S3 file uploads.
   - DynamoDB for serverless database storage.
4. **High Availability**
   - Resources spread across **two Availability Zones**.
   - Load balancing and scaling for fault tolerance.

---

## ⚙️ Terraform Setup

### 1. Initialize Terraform
```bash
terraform init
