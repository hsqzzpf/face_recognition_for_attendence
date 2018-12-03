# 进度 30/11/2018

## 1. AWS server
- 四个接口
### a. /update
- POST
- name, classNo
- 更新某学生状态 从 FALSE 变 TRUE
### b. /add
- POST
- name
- 添加学生， 初始化都为 FALSE
### c. /reset
- POST
- classNo
- 重置该classNO为FALSE
### d. /get
- POST
- classNo
- 获取某门课学生签到情况

## 2. SQLite datebase 完成[DONE]
- 具体实现看 classFragment.java
- 在 class tab 下面有一个 recycleView 里面是数据库实现
- 数据源在 res/raw/courses.json 里面

## 3. 设置界面的人脸识别 -- half way[DONE]
- detect 接口完成
- 还需要实现 addface 接口 和 changeid 接口 

## 4. 尚待完成的其余UI部分
- home 页面的倒计时
- schedule 页面的日历
- class 页面的美化
- class 与 AWS 的数据交流
- setting 页面 第二个 button： 调整class信息

