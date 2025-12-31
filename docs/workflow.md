# Workflow – IV Planner & Connector

This document explains the complete workflow of the IV Planner & Connector platform, including authentication and role-based operations.

---

## 🔐 Authentication Workflow

```
User opens the platform
 ↓
User selects a role (Student / College / Provider / Admin)
 ↓
User enters login credentials
 ↓
System authenticates user credentials
 ↓
System verifies selected role
 ↓
User is redirected to the corresponding role-based dashboard
```

---

## 🏭 Service Provider Workflow

```
Service Provider logs in
 ↓
Service Provider accesses Provider Dashboard
 ↓
Service Provider adds IV availability
    - Date
    - Branch
    - Capacity
 ↓
Availability is stored in the database
 ↓
Availability status is set to OPEN
 ↓
Availability becomes visible to Colleges
```

---

## 🏫 College / IV Coordinator Workflow

```
College logs in
 ↓
College accesses College Dashboard
 ↓
College browses available Service Providers
 ↓
College creates an IV plan
 ↓
College sends IV request to Service Provider
 ↓
IV request status is set to PENDING
```

---

## 🔄 IV Request Approval Workflow (Service Provider)

```
Service Provider views incoming IV requests
 ↓
Service Provider reviews IV request details
 ↓
Service Provider approves or rejects the request
 ↓
If Approved:
    Status is set to APPROVED
    Availability is updated
 ↓
If Rejected:
    Status is set to REJECTED
 ↓
College is notified of the decision
```

---

## 👨‍🎓 Student Workflow

```
Student logs in
 ↓
Student accesses Student Dashboard
 ↓
Student browses:
    - Industrial Visits
    - Internships
    - Mentorship opportunities
 ↓
Student applies for a selected opportunity
 ↓
Application status is set to PENDING
 ↓
College reviews the application
 ↓
Application status is updated to APPROVED or REJECTED
 ↓
Student is notified of the result
```

---

## 👑 Admin Workflow

```
Admin logs in
 ↓
Admin accesses Admin Dashboard
 ↓
Admin reviews Service Provider registrations
 ↓
Admin approves or rejects Service Providers
 ↓
Admin adds unregistered companies to the platform
 ↓
Admin monitors overall platform activity
```

---

## 📌 Status Lifecycle

```
OPEN → PENDING → APPROVED → COMPLETED
           ↘
          REJECTED
```

---

## 🧠 Notes

- All interactions are mediated by the platform
- Role-based access controls user permissions
- Status-driven workflow ensures consistency and traceability
