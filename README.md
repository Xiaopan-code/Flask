# 基于 Flask 的问答小项目

这是一个跟着 B 站知了传课视频学习开发的简单问答项目，基于 Flask 框架实现。
https://www.bilibili.com/video/BV17r4y1y7jJ?spm_id_from=333.788.videopod.episodes&vd_source=ba3042342a76becbea5662dbd33620b7

## 项目功能与技术点

该项目主要涉及以下技术和功能：
- URL 传参
- 邮件发送功能
- AJAX 异步交互
- ORM 与数据库操作
- Jinja2 模板引擎使用
- Cookie 和 Session 管理

# 问答系统项目说明

## 项目概述
该项目是一个基于Flask框架开发的问答系统，实现了用户注册、登录、提问、回答、搜索等核心功能，采用MySQL数据库存储数据，使用WTForms进行表单验证，通过蓝图(Blueprint)实现代码模块化组织。

## 模块说明

### 1. 主应用模块 (app.py)
项目入口文件，负责初始化Flask应用、配置加载、扩展初始化及蓝图注册
```
# 主要功能：
- 初始化Flask应用并加载配置
- 初始化数据库(db)和邮件(mail)扩展
- 配置数据库迁移工具(Migrate)
- 注册问答(qa_bp)和认证(auth_bp)蓝图
- 定义请求钩子(before_request)：在请求处理前加载当前登录用户
- 定义上下文处理器(context_processor)：使user变量在所有模板中可用
```

### 2. 数据模型模块 (models.py)
定义数据库模型，映射数据库表结构
```
# 主要模型：
- UserModel：用户模型，存储用户信息(id, username, password, email, join_time)
- EmailCaptchaModel：邮箱验证码模型，存储邮箱与验证码对应关系
- QuestionModel：问题模型，存储问题信息及与用户的关联关系
- AnswerModel：回答模型，存储回答信息及与问题、用户的关联关系

# 关系说明：
- UserModel与QuestionModel：一对多关系(一个用户可发布多个问题)
- UserModel与AnswerModel：一对多关系(一个用户可发布多个回答)
- QuestionModel与AnswerModel：一对多关系(一个问题可有多条回答)
```

### 3. 认证模块 (auth.py)
处理用户注册、登录、退出及邮箱验证码相关功能
 ```
# 主要路由函数：
- /auth/login：处理用户登录(GET显示页面，POST验证登录)
- /auth/register：处理用户注册(GET显示页面，POST验证并创建用户)
- /auth/logout：用户退出登录(清空session)
- /auth/captcha/email：生成并发送邮箱验证码
- /auth/mail/test：邮件发送测试接口
```

### 4. 问答模块 (qa.py)
```
# 主要路由函数：
- /：首页，展示所有问题(按创建时间倒序)
- /qa/public：发布问题(需登录，GET显示页面，POST提交数据)
- /qa/detail/<qa_id>：查看问题详情
- /answer/public：提交回答(需登录，POST方法)
- /search：搜索问题(按标题关键字搜索)
```

### 5. 表单验证模块 (forms.py)
```
# 主要表单：
- RegisterForm：注册表单验证(邮箱、验证码、用户名、密码等)
- LoginForm：登录表单验证(邮箱、密码)
- QuestionForm：问题表单验证(标题、内容)
- AnswerForm：回答表单验证(内容、问题ID)

# 验证规则：
- 格式验证(邮箱格式、长度限制等)
- 逻辑验证(两次密码一致、邮箱未被注册等)
- 自定义验证(验证码正确性等)
```

### 6. 工具模块
```
- **decorators.py**：定义装饰器，实现登录验证功能
  - login_required：用于保护需要登录才能访问的路由

- **exts.py**：初始化扩展实例，解决循环引用问题
  - 初始化 SQLAlchemy (db) 和 Mail (mail) 实例

- **config.py**：项目配置文件
  - 应用密钥 (SECRET_KEY)
  - 数据库连接配置
  - 邮箱服务配置 (SMTP 服务器、端口、账号等)
```

## 功能流程说明

1. **用户注册流程**：
   - 访问注册页面，填写信息
   - 获取邮箱验证码
   - 提交表单，验证通过后创建用户

2. **用户登录流程**：
   - 访问登录页面，输入邮箱和密码
   - 验证通过后，将用户 ID 存入 session

3. **提问流程**：
   - 登录用户访问提问页面
   - 填写问题标题和内容
   - 提交后保存到数据库，返回首页

4. **回答流程**：
   - 登录用户在问题详情页填写回答
   - 提交后保存到数据库，返回问题详情页

5. **搜索流程**：
   - 在搜索框输入关键字
   - 系统查询标题包含关键字的问题并展示

## 技术栈
- 后端框架：Flask
- 数据库：MySQL + SQLAlchemy (ORM)
- 表单验证：WTForms
- 邮件服务：Flask-Mail
- 数据库迁移：Flask-Migrate
- 密码加密：werkzeug.security
