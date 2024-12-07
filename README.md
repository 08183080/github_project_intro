# 项目介绍
Github项目介绍器

输入： github项目链接\
输出： github项目的可信介绍

# 运行方法
## 安装依赖
```
pip install -r requirements.txt
```

## 运行
### 有gui的
```
python crawl_ai_app.py
```
## 纯界面的
```
python crawl_ai.py
```

# 项目日志
- [x] 12/7，发现原来**crawl4ai**的底部诸多大模型路由是用的litellm，成功让deepseek适配craw4ai
- [x] 12/7，跑通软件的v2版本，craw4ai爬取项目界面，然后再让ai后处理介绍。不过也可以纯代码去爬，更快些。后续再写原生的。

# TO DO
- [ ] 项目生成可执行文件
- [ ] 结合reflex项目，将项目部署到云端  