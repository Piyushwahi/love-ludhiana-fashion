# REST API Standards & Guidelines

This document details the REST API specifications and response standards for the **Love Ludhiana Fashion** platform.

---

## 1. Request URL Structure & Versioning

* All routes must be versioned. The current active version is `v1`.
* Base path: `/api/v1/`
* Route patterns use plural nouns for collections and identifiers for single resources:
  - `GET /api/v1/products` (List products)
  - `GET /api/v1/products/{id}` (Get single product details)
  - `POST /api/v1/products` (Create a product - Admin only)
  - `PUT /api/v1/products/{id}` (Update a product - Admin only)
  - `DELETE /api/v1/products/{id}` (Delete a product - Admin only)

---

## 2. Standardized JSON Responses

All API responses must follow a consistent structure.

### Success Response Format
Returns HTTP status `200 OK` or `201 Created`.
```json
{
  "success": true,
  "message": "Resource retrieved successfully",
  "data": {
    "id": "7ca64731-0164-4bf8-b649-166bf1c70e2a",
    "name": "Toddler Floral Cotton Dress",
    "price": 1499.00
  },
  "timestamp": "2026-06-28T14:00:00Z"
}
```

### Paginated List Response Format
List endpoints must implement pagination. Offset calculations are handled implicitly by the backend via `page` and `page_size`.
```json
{
  "success": true,
  "message": "Products list retrieved successfully",
  "data": [
    {
      "id": "7ca64731-0164-4bf8-b649-166bf1c70e2a",
      "name": "Toddler Floral Cotton Dress",
      "price": 1499.00
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 120,
    "total_pages": 6,
    "has_next": true,
    "has_previous": false
  }
}
```

### Error Response Format
Error responses must return standard HTTP status codes (e.g. `400`, `401`, `403`, `404`, `422`, `429`, `500`) alongside structured error payloads.
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "price",
        "message": "Input should be greater than 0",
        "type": "greater_than"
      }
    ]
  }
}
```

---

## 3. Query Parameter Standards

* **Pagination**: Use `page` (1-indexed) and `page_size`.
* **Sorting**: Use `sort_by=field_name` and `sort_order=asc|desc`.
* **Search**: Use `search=query_string` for searching text matches in columns.
* **Filtering**: Use matching query keys (e.g., `category_id=uuid` or `is_active=true`).
