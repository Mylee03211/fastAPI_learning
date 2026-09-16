# 常用状态码查询

# # 成功状态码
# 200 OK                    # 请求成功
# 201 Created              # 资源创建成功
# 204 No Content           # 成功但无内容返回
# 206 Partial Content      # 部分内容（分页、断点续传）
#
# # 重定向
# 301 Moved Permanently    # 永久重定向
# 302 Found               # 临时重定向
# 304 Not Modified        # 资源未修改（缓存）
#
# # 客户端错误
# 400 Bad Request         # 请求格式错误
# 401 Unauthorized        # 未认证
# 403 Forbidden          # 已认证但无权限
# 404 Not Found          # 资源不存在
# 405 Method Not Allowed  # HTTP 方法不允许
# 409 Conflict           # 资源冲突
# 422 Unprocessable Entity # 数据验证失败
# 429 Too Many Requests   # 请求过于频繁
#
# # 服务器错误
# 500 Internal Server Error # 服务器内部错误
# 502 Bad Gateway          # 网关错误
# 503 Service Unavailable  # 服务不可用