# ERP 管理平台 - API 接口说明（供接口测试 / Postman 使用）

基础 URL：`http://localhost:5000/api`  
除登录外，其余接口需先登录，请求时需携带 Session Cookie（浏览器同源请求自动携带）。

---

## 1. 登录

- **POST** `/api/login`  
- **Content-Type**: `application/json`  
- **请求体**:
  ```json
  { "username": "admin", "password": "admin123" }
  ```
- **成功响应**:
  ```json
  { "success": true, "message": "登录成功", "data": { "user_id": 1, "username": "admin", "real_name": "管理员", "role": "admin" } }
  ```
- **失败**: `success: false`, `message` 为错误说明。

---

## 2. 登出

- **POST** `/api/logout`  
- 清除服务端 Session。

---

## 3. 当前用户信息

- **GET** `/api/user/info`  
- 需登录。返回当前用户信息。

---

## 4. 商品列表

- **GET** `/api/products`  
- 可选查询参数: `category`（类别筛选）  
- 需登录。返回商品列表。

---

## 5. 商品详情

- **GET** `/api/products/<id>`  
- 需登录。

---

## 6. 新增商品

- **POST** `/api/products`  
- **Content-Type**: `application/json`  
- **请求体**:
  ```json
  { "code": "P006", "name": "商品名", "category": "文具", "unit": "个", "price": 10.5, "stock": 100 }
  ```
- `code`、`name` 必填；`price` 非负；`code` 不可重复。

---

## 7. 订单列表

- **GET** `/api/orders`  
- 可选查询参数: `status`（pending/confirmed/shipped/completed/cancelled）  
- 需登录。

---

## 8. 创建订单

- **POST** `/api/orders`  
- **Content-Type**: `application/json`  
- **请求体**:
  ```json
  {
    "customer_name": "某客户",
    "items": [ { "product_id": 1, "quantity": 2 } ]
  }
  ```
- 会校验商品存在性、库存；金额由后端按单价×数量计算。

---

## Postman 使用提示

1. 先调用 **POST /api/login**，保存返回的 Cookie 或使用 Postman 的 “Send cookies automatically”。  
2. 后续请求使用同一环境，即可自动带 Cookie 访问需登录接口。  
3. 可设置环境变量：`base_url = http://localhost:5000`，请求 URL 为 `{{base_url}}/api/...`。  
4. 接口测试报告可参考赛题中的《接口测试报告模板》编写。
