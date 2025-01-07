# Setting Up EventBridge Rule for EC2 Instance State Changes using Terraform

In this hands-on lab, we will walk through the process of setting up an **EventBridge rule** to get notified when the state of an EC2 instance changes. We will use **Terraform** to automate the setup, ensuring reproducibility and consistency in our infrastructure. By the end of this lab, you'll have a working setup that sends notifications to an email address whenever the state of an EC2 instance changes (e.g., from running to stopped).

## Table of Contents
1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Terraform Resources Overview](#terraform-resources-overview)
4. [Setup Instructions](#setup-instructions)
5. [Outputs](#outputs)
6. [Additional Considerations](#additional-considerations)
7. [Conclusion](#conclusion)

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
EventBridgeRule_TF/
├── README.md
├── main.tf # Terraform configuration for resource provisioning
├── output.tf # Output values from Terraform
├── terraform.tfvars # Variables for AWS credentials and configuration
├── variables.tf # Input variable definitions for Terraform
```


## Terraform Resources Overview

### **main.tf**
The `main.tf` file is the heart of the Terraform configuration, where we define the following resources:

1. **AWS Provider Configuration**: Defines the region, access key, and secret key for AWS.
2. **Security Group**: Creates a security group for the EC2 instance with inbound SSH access on port 22.
3. **EC2 Instance**: Provisions an EC2 instance using a predefined AMI (Amazon Machine Image).
4. **SNS Topic**: Defines an SNS topic to send notifications when EC2 state changes.
5. **SNS Topic Subscription**: Creates an email subscription to the SNS topic. The endpoint is specified as a variable (your email address).
6. **CloudWatch Event Rule**: Monitors EC2 instance state changes and triggers when a change occurs (e.g., running to stopped).
7. **CloudWatch Event Target**: Sends events to the SNS topic.

### **output.tf**
This file specifies the outputs of the Terraform plan, such as:
- The **instance ID** of the EC2 instance.
- The **ARN of the SNS topic**.
- The **ARN of the CloudWatch rule**.

### **terraform.tfvars**
This file contains the environment-specific values such as your AWS access key, secret key, region, and the email address that will receive notifications.

### **variables.tf**
Defines input variables required for the Terraform configuration:
- `access_key`: AWS access key.
- `secret_key`: AWS secret key.
- `region`: AWS region where the resources will be created.
- `endpoint`: Email address for the SNS subscription.

## Setup Instructions

### Prerequisites:
1. **Terraform**: Install Terraform on your local machine. (Visit [Terraform Installation Guide](https://learn.hashicorp.com/tutorials/terraform/install-cli) for details).
2. **AWS Account**: Make sure you have an active AWS account and the necessary IAM permissions to create EC2, SNS, and CloudWatch resources.
3. **AWS CLI**: Ensure that AWS CLI is configured on your machine with access keys.

### Steps to Deploy the Infrastructure:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-name/EventBridgeRule_TF.git
   cd EventBridgeRule_TF
   ```
2. **Configure your AWS credentials: Open terraform.tfvars and add your AWS access key, secret key, region, and email endpoint:**
   ```plaintext
   access_key = "<Enter your AWS Account Access Key>"
   secret_key = "<Enter your AWS Account Secret Key>"
   region = "<Enter your Region>"
   endpoint = "<Enter your mail ID>"

   ```
3. **Initialize Terraform: Initialize Terraform by running:**
   ```bash
   terraform init
   ```
4. **Plan the Terraform deployment: To review the infrastructure Terraform will create, run:**
   ```bash
   terraform plan
   ```
5. **Apply the Terraform configuration: Deploy the resources with:**
   ```bash
   terraform apply
   ```
   Terraform will ask for confirmation to proceed. Type yes to approve.
6. **Verify the setup: After applying the plan, Terraform will output key details such as the EC2 instance ID, SNS topic ARN, and CloudWatch Event Rule ARN.**
7. **Test the setup: To test the setup, start or stop the EC2 instance manually via the AWS Console or using the AWS CLI. You should receive an email notification when the state of the instance changes.**

## Outputs

After running `terraform apply`, Terraform will provide the following outputs:

- `instance_id`: The ID of the EC2 instance.
- `topic_arn`: The ARN (Amazon Resource Name) of the SNS topic.
- `event_name`: The ARN of the CloudWatch event rule.

```bash
Outputs:

instance_id = "i-0bb9f7f1ebd123abc"
topic_arn = "arn:aws:sns:us-west-2:123456789012:MyServerMonitor"
event_name = "arn:aws:events:us-west-2:123456789012:rule/MyEC2StateChangeEvent"

```

## Additional Considerations

- **Security**: Ensure that your AWS credentials (access keys) are kept secure. Consider using environment variables or AWS IAM roles for enhanced security.
- **SNS Subscription**: You will need to confirm your email subscription before receiving notifications. Check your inbox for a confirmation email from AWS SNS and confirm the subscription.
- **IAM Permissions**: Ensure your AWS IAM user has sufficient permissions to create EC2 instances, SNS topics, CloudWatch event rules, and related resources.

## Conclusion

In this tutorial, we’ve successfully set up an EventBridge rule using Terraform to monitor EC2 instance state changes and send email notifications. This solution automates the process, making it easy to track EC2 status changes in your AWS environment. By leveraging Terraform, we ensure that the setup is reproducible and consistent. With this setup, you can stay informed about important EC2 events without manually checking the instance state.
