# Overview

This project was developed for demonstration purposes and showcases the basic functionality of an API service integrated
with a PostGIS database, Redis for caching, and Nginx for serving static files and acting as a reverse proxy.

While the project demonstrates a functional implementation, it is important to note that several key aspects required
for a production-ready application are either missing or intentionally simplified.

## Areas for Improvement

- The current implementation lacks user authentication and authorization mechanisms, which are critical for securing the
  application and managing user permissions.
- Some application settings are not configured with production readiness in mind. This includes settings related to
  security, performance, and scalability.
- The "locate" endpoint does not limit the amount of data it returns, which could lead to performance issues and
  excessive
  data transfer in production environments.
- The current cache invalidation algorithm is simplistic, relying on a timeout mechanism. This approach can be optimized
  to better align with application use cases and improve cache efficiency.
- There is no integration of static code analysis tools to check for code style adherence and potential security
  vulnerabilities. Implementing tools like flake8, black, and bandit would enhance code quality and security.
- The database entities for "language" and "currency" are currently implemented as simple fields. These should ideally
  be
  normalized into separate tables to ensure data consistency and facilitate easier management.
- The application lacks comprehensive validation for incoming data, which is essential to ensure data integrity and
  prevent erroneous or malicious data from being processed.

# Local development

It involves running a server for local development in a container, only the database and all other services manually as
needed

```bash
python3.11 -m venv .venv
pip install -r dependencies/requirements.txt
export DATABASE_URL=postgis://bootcamp_db:bootcamp_password@localhost:5432/bootcamp_db
export ENVIRONMENT=test pytest
docker-compose -f docker-compose.infra.yml up
pytest
```

# Infrastructure

The current implementation of the infrastructure is purely for demonstration purposes; a real application should consist
of a much more complex infrastructure, for example:

- EC2 - running containers;
- RDS - managing the PostGIS database;
- ElastiCache - managing cache;
- S3 - store static files;
- ALB - distributing traffic across your EC2 instances;
- CloudFront - CDN and caching static content;
- IAM - managing permissions and roles;
- VPC: network isolation and security;
- Route 53 - DNS management.

# e2e tests

Set server API_HOST env variable and run:

```bash
export API_HOST=you_host_value
./e2e_tests.sh
```