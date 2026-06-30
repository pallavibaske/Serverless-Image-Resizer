# 🖼️ Serverless Image Resizer

## 🎯 Project Overview

This project automatically resizes images uploaded to an Amazon S3 bucket using AWS Lambda.

When a user uploads an image, Amazon S3 triggers an AWS Lambda function, which resizes the image and stores the resized version in another S3 bucket.

---

## 🛠 AWS Services Used

- AWS Lambda
- Amazon S3
- AWS IAM
- Python
- Pillow (Python Library)

---

## 🏗 Architecture

The solution follows an event-driven serverless architecture where S3 events trigger a Lambda function to resize uploaded images automatically.

---

## 🔄 Workflow

1. User uploads an image to the source S3 bucket.
2. Amazon S3 triggers the Lambda function.
3. Lambda resizes the image using the Pillow library.
4. The resized image is saved to the destination S3 bucket.

---

## ✨ Features

- Serverless Architecture
- Automatic Image Resizing
- Event-driven Processing
- Scalable Solution

---

## 📂 Repository Structure

Serverless-Image-Resizer

├── README.md

├── Architecture/

├── Screenshots/

└── Lambda-Code/

---

## 📚 Learning Outcomes

- AWS Lambda
- Amazon S3
- Event Notifications
- Image Processing
- Serverless Computing

---

## 👩‍💻 Author

**Pallavi Baske**

LinkedIn:
https://www.linkedin.com/in/pallavi-baske-6a0b80216

GitHub:
https://github.com/pallavibaske
