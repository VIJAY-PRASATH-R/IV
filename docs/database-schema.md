# Database Schema – IV Planner & Connector

This document defines the database tables and their fields for the IV Planner & Connector platform.

---

## 👤 Users Table

Stores login and role information for all users.

```
users
-----
id (PK)
name
email
password_hash
role (student / college / provider / admin)
created_at
```

---

## 🏫 Colleges Table

Stores college-specific information.

```
colleges
--------
id (PK)
user_id (FK → users.id)
college_name
location
contact_email
contact_phone
```

---

## 🏭 Service Providers Table

Stores information about companies and service providers.

```
service_providers
-----------------
id (PK)
user_id (FK → users.id)
company_name
industry_type
location
description
approved (true / false)
```

---

## 📅 IV Availability Table

Stores IV slots published by service providers.

```
iv_availability
---------------
id (PK)
provider_id (FK → service_providers.id)
date
branch
capacity
status (OPEN / BOOKED)
```

---

## 📝 IV Requests Table

Stores IV requests sent by colleges.

```
iv_requests
-----------
id (PK)
availability_id (FK → iv_availability.id)
college_id (FK → colleges.id)
requested_students
status (PENDING / APPROVED / REJECTED)
created_at
```

---

## 👨‍🎓 Student Applications Table

Stores applications submitted by students.

```
applications
------------
id (PK)
student_id (FK → users.id)
iv_request_id (FK → iv_requests.id)
status (PENDING / APPROVED / REJECTED)
applied_at
```

---

## 📄 MoU Table

Tracks MoU status between colleges and providers.

```
mou
---
id (PK)
college_id (FK → colleges.id)
provider_id (FK → service_providers.id)
status (UPLOADED / SIGNED / PENDING)
document_path
```

---

## 🧠 Status Rules

```
OPEN → PENDING → APPROVED → COMPLETED
           ↘
          REJECTED
```

---

## 📌 Notes

- Foreign keys ensure data consistency
- Status-driven tables simplify workflow logic
- Schema is designed for scalability
