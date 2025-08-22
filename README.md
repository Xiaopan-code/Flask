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
