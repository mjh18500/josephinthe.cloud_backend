🌐 Visitor Counter Backend (Azure Function + API Management)

This backend powers the visitor counter for my cloud portfolio site: josephinthe.cloud.

It’s a serverless Azure Function App exposed securely through Azure API Management (APIM), with a persistent database to track visitor counts.

🚀 Project Overview

The backend handles each site visit by:

Receiving an API call from the frontend (React + Vite + TypeScript).

Incrementing a counter stored in the database.

Returning the updated visitor count in real time to be displayed on the site.

This project demonstrates cloud-native, production-grade design:

✅ Serverless Functions – event-driven execution, cost-efficient.

✅ Azure API Management – secure API gateway with rate limiting and CORS configuration.

✅ Database Persistence – ensures visitor counts survive restarts and scale events.

✅ Infrastructure as Code (Terraform) – fully automated deployments.

✅ CI/CD (GitHub Actions) – test and deploy changes seamlessly.

🛠 Tech Stack

Language: Python

Cloud Platform: Microsoft Azure

Services Used:

Azure Function App (HTTP Trigger)

Azure API Management

Azure CosmosDB / Table API

Azure Storage Account (logs & configs)

CI/CD: GitHub Actions

IaC: Terraform

🧪 Key Features

Visitor Counter API

✅ Returns updated visitor count

✅ Persists values in DB

✅ Handles malformed requests gracefully (returns error response)

✅ Edge-case handling: initializes counter if missing

✅ CI pipeline runs on each push

🔒 Security

API is protected with subscription keys through Azure APIM.

Keys are stored securely as GitHub Secrets and injected into CI/CD pipelines.

CORS policies configured to only allow my frontend domain.

🌟 Why I Built This

I wanted a project that demonstrates real-world cloud engineering skills.

This backend shows:

How to securely expose a Function App via APIM

How to persist state in a stateless architecture

How to automate infrastructure deployments with Terraform

How to test and validate APIs with CI/CD pipelines

In other words, it’s a production-ready microservice that happens to run a fun feature (tracking site visitors).

📈 Results

Visitors to josephinthe.cloud see a live counter that updates instantly.

Backend scales automatically with traffic.

