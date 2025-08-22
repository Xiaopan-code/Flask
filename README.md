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

```python
# 主要功能：
- 初始化Flask应用并加载配置
- 初始化数据库(db)和邮件(mail)扩展
- 配置数据库迁移工具(Migrate)
- 注册问答(qa_bp)和认证(auth_bp)蓝图
- 定义请求钩子(before_request)：在请求处理前加载当前登录用户
- 定义上下文处理器(context_processor)：使user变量在所有模板中可用

### 1. 主应用模块 (app.py)
