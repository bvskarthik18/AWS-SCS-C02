# Setting Up EventBridge Rule for EC2 Instance State Changes using Terraform

In this hands-on lab, we will walk through the process of setting up an **EventBridge rule** to get notified when the state of an EC2 instance changes. We will use **Terraform** to automate the setup, ensuring reproducibility and consistency in our infrastructure. By the end of this lab, you'll have a working setup that sends notifications to an email address whenever the state of an EC2 instance changes (e.g., from running to stopped).

## Table of Contents
1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Terraform Resources Overview](#terraform-resources-overview)
4. [Setup Instructions](#setup-instructions)
5. [Outputs](#outputs)
6. [Additional Considerations](#additional-considerations)
7. [License](#license)

## Overview
This setup automates the creation of AWS resources required to monitor EC2 instance state changes and send notifications via Amazon SNS. Terraform is used to define and provision all the necessary infrastructure, including:
- A security group for the EC2 instance.
- A key pair for SSH access.
- An EC2 instance.
- An SNS topic and subscription to send notifications.
- A CloudWatch Event rule to capture EC2 instance state changes.

### Flow:
1. **EC2 Instance State Change** → Captured by **CloudWatch Event Rule**.
2. CloudWatch triggers an **SNS Topic**, sending a notification to a specified email endpoint.

## Directory Structure

```ruby
EventBridgeRule_TF/ │ ├── README.md # This file ├── main.tf # Terraform configuration for resource provisioning ├── output.tf # Output values from Terraform ├── terraform.tfvars # Variables for AWS credentials and configuration ├── variables.tf # Input variable definitions for Terraform
```
