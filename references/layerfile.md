# Layerfile — 基因组图谱
# ══════════════════════════════════════════════════════════════════
#
# 这是 Avengers Assemble 的核心数据结构。
# AI（核糖体的大脑）只需要读这个文件，不需要读素材 .py 文件。
#
# 三种格式各司其职：
#   CSV  — 索引映射：AI 做筛选/查询最方便，hex→角色→所属素材
#   JSON — 接口契约：精确的参数签名和约束，机器直接 parse
#   YAML — 素材关系：依赖树、跨文件引用、层级拓扑
#
# 核糖体（Avengers.py）读 JSON 做拼装，AI 读 CSV 做选择，YAML 确定组装顺序。


# ══════════════════════════════════════════════════════════════════
# [1] CSV — 索引映射
# AI 查询入口：快速筛选"我需要哪些 hex"
# ══════════════════════════════════════════════════════════════════
```csv
hex,type,role,file,section,description
0xA1B2C1,variable,output,calculator.py,算术赋值,加法结果
0xA1B2C2,variable,input,calculator.py,算术赋值,加法左操作数
0xA1B2C3,variable,input,calculator.py,算术赋值,加法右操作数
0xA1B2D1,variable,output,calculator.py,算术赋值,减法结果
0xA1B2D2,variable,input,calculator.py,算术赋值,减法左操作数
0xA1B2D3,variable,input,calculator.py,算术赋值,减法右操作数
0xA1B2E1,variable,output,calculator.py,算术赋值,乘法结果
0xA1B2E2,variable,input,calculator.py,算术赋值,乘法左操作数
0xA1B2E3,variable,input,calculator.py,算术赋值,乘法右操作数
0xA1B2F1,variable,output,calculator.py,算术赋值,除法结果
0xA1B2F2,variable,input,calculator.py,算术赋值,除法左操作数
0xA1B2F3,variable,input,calculator.py,算术赋值,除法右操作数
0xA1C3B1,variable,input-output,calculator.py,自增自减,计数器变量
0xA1C3B2,variable,input,calculator.py,自增自减,初始值
0xA1C3B3,variable,input,calculator.py,自增自减,步长值
0xA1D4B1,variable,input-output,calculator.py,类型转换,源变量
0xA1D4B2,variable,input,calculator.py,类型转换,待转换值
0xA1D4C1,variable,output,calculator.py,类型转换,int转换结果
0xA1D4D1,variable,output,calculator.py,类型转换,float转换结果
0xA1D4E1,variable,output,calculator.py,类型转换,str转换结果
0xA1D4F1,variable,output,calculator.py,类型转换,round结果
0xA1D4F2,variable,input,calculator.py,类型转换,round源值
0xA1D4F3,variable,input,calculator.py,类型转换,round精度(小数位数)
0xA1E5B1,variable,output,calculator.py,数学运算,sqrt结果
0xA1E5B2,variable,input,calculator.py,数学运算,sqrt操作数
0xA1E5C1,variable,output,calculator.py,数学运算,abs结果
0xA1E5C2,variable,input,calculator.py,数学运算,abs操作数
0xA1E5D1,variable,output,calculator.py,数学运算,max结果
0xA1E5D2,variable,input,calculator.py,数学运算,max操作数1
0xA1E5D3,variable,input,calculator.py,数学运算,max操作数2
0xA1E5D4,variable,input,calculator.py,数学运算,max操作数3
0xA1E5E1,variable,output,calculator.py,数学运算,min结果
0xA1E5E2,variable,input,calculator.py,数学运算,min操作数1
0xA1E5E3,variable,input,calculator.py,数学运算,min操作数2
0xA1E5E4,variable,input,calculator.py,数学运算,min操作数3
0xA1E5F1,variable,output,calculator.py,数学运算,pow结果
0xA1E5F2,variable,input,calculator.py,数学运算,pow底数
0xA1E5F3,variable,input,calculator.py,数学运算,pow指数
0xA1F6B1,variable,output,calculator.py,取模整除,取模结果
0xA1F6B2,variable,input,calculator.py,取模整除,被除数
0xA1F6B3,variable,input,calculator.py,取模整除,除数
0xA1F6C1,variable,output,calculator.py,取模整除,整除结果
0xA1F6C2,variable,input,calculator.py,取模整除,被除数
0xA1F6C3,variable,input,calculator.py,取模整除,除数
0xF1A2C1,variable,input,console.py,打印,打印内容
0xF1A2C2,variable,input,console.py,打印,打印项1
0xF1A2C3,variable,input,console.py,打印,打印项2
0xF1A2C4,variable,input,console.py,打印,打印项3
0xF1A2C5,variable,input,console.py,打印,打印项4
0xF1A2D1,variable,output,console.py,输入,接收到的输入值
0xF1A2D2,variable,input,console.py,输入,提示文字
0xF1A2E1,variable,input-output,console.py,格式化打印,待插值变量
0xF1A2E2,variable,input,console.py,格式化打印,赋值源
0xF1A2E3,variable,input,console.py,格式化打印,f-string前缀文字
0xF1A2E4,variable,input,console.py,格式化打印,f-string格式说明符
0xF1A2E5,variable,input,console.py,格式化打印,格式精度
0xF1A2F1,variable,input,console.py,格式化打印,f-string前缀文字
0xF1A2F2,variable,input-output,console.py,格式化打印,待格式化变量
0xF1A2F3,variable,input,console.py,格式化打印,格式说明符
0xF1A2F4,variable,input,console.py,格式化打印,f-string前缀文字
0xF1A2F5,variable,input-output,console.py,格式化打印,待格式化变量
0xF1A2F6,variable,input,console.py,格式化打印,格式说明符
0xF1B3C1,variable,input,console.py,stderr输出,stderr打印内容
0xF1B3D1,variable,input,console.py,日志,日志级别(DEBUG/INFO/WARNING/ERROR/CRITICAL)
0xF1B3D2,variable,input,console.py,日志,日志格式字符串
0xF1B3D3,variable,input,console.py,日志,info消息内容
0xF1B3D4,variable,input,console.py,日志,warning消息内容
0xF1B3D5,variable,input,console.py,日志,error消息内容
0xF1B3E1,variable,input-output,console.py,表格打印,数据列表(元组列表)
0xF1B3E2,variable,input,console.py,表格打印,元组字段1
0xF1B3E3,variable,input,console.py,表格打印,元组字段2
0xF1B3E4,variable,input,console.py,表格打印,元组字段1(第二行)
0xF1B3E5,variable,input,console.py,表格打印,元组字段2(第二行)
0xF1B3F1,variable,input-output,console.py,表格打印,循环变量-字段1
0xF1B3F2,variable,input-output,console.py,表格打印,循环变量-字段2
0xF1B3F3,variable,input,console.py,表格打印,字段1宽度
0xF1B3F4,variable,input,console.py,表格打印,字段2宽度
0xC1D2C1,variable,input,control_flow.py,条件判断,比较变量
0xC1D2C2,variable,input,control_flow.py,条件判断,阈值1
0xC1D2C3,variable,output,control_flow.py,条件判断,结果变量
0xC1D2C4,variable,input,control_flow.py,条件判断,分支1返回值
0xC1D2C5,variable,input,control_flow.py,条件判断,阈值2
0xC1D2C6,variable,input,control_flow.py,条件判断,分支2返回值
0xC1D2C7,variable,input,control_flow.py,条件判断,阈值3
0xC1D2C8,variable,input,control_flow.py,条件判断,分支3返回值
0xC1D2C9,variable,input,control_flow.py,条件判断,else返回值
0xC1D2D1,variable,input-output,control_flow.py,for循环(range),循环变量
0xC1D2D2,variable,input,control_flow.py,for循环(range),迭代上限
0xC1D2E1,variable,input,control_flow.py,for循环(可迭代),可迭代对象
0xC1D2E2,variable,input,control_flow.py,for循环(可迭代),列表元素1
0xC1D2E3,variable,input,control_flow.py,for循环(可迭代),列表元素2
0xC1D2E4,variable,input,control_flow.py,for循环(可迭代),列表元素3
0xC1D2E5,variable,input-output,control_flow.py,for循环(可迭代),循环变量
0xC1D2F1,variable,input,control_flow.py,for循环(enumerate),可迭代对象
0xC1D2F2,variable,input,control_flow.py,for循环(enumerate),列表元素1
0xC1D2F3,variable,input,control_flow.py,for循环(enumerate),列表元素2
0xC1D2F4,variable,input,control_flow.py,for循环(enumerate),列表元素3
0xC1D3B1,variable,output,control_flow.py,for循环(enumerate),索引变量
0xC1D3B2,variable,input-output,control_flow.py,for循环(enumerate),值变量
0xC1D3C1,variable,input-output,control_flow.py,while循环,循环变量
0xC1D3C2,variable,input,control_flow.py,while循环,初始值
0xC1D3C3,variable,input,control_flow.py,while循环,终止条件
0xC1D3C4,variable,input,control_flow.py,while循环,步长
0xC1D3D1,variable,input-output,control_flow.py,break,循环变量
0xC1D3D2,variable,input,control_flow.py,break,迭代上限
0xC1D3D3,variable,input,control_flow.py,break,中断条件值
0xC1D3E1,variable,input-output,control_flow.py,continue,循环变量
0xC1D3E2,variable,input,control_flow.py,continue,迭代上限
0xC1D3E3,variable,input,control_flow.py,continue,取模除数
0xC1D3F1,variable,input-output,control_flow.py,嵌套循环,外层循环变量
0xC1D3F2,variable,input,control_flow.py,嵌套循环,外层迭代上限
0xC1D4B1,variable,input-output,control_flow.py,嵌套循环,内层循环变量
0xC1D4B2,variable,input,control_flow.py,嵌套循环,内层迭代上限
0xC1D4C1,variable,output,control_flow.py,异常处理,除法结果
0xC1D4C2,variable,input,control_flow.py,异常处理,被除数
0xC1D4C3,variable,input,control_flow.py,异常处理,除数(可能为0)
0xC1D4C4,variable,input,control_flow.py,异常处理,异常类型
0xC1D4C5,variable,input,control_flow.py,异常处理,异常消息
0xC1D4C6,variable,input-output,control_flow.py,异常处理,异常实例变量名
0xC1D4C7,variable,input,control_flow.py,异常处理,错误前缀文字
0xC1D4C8,variable,input,control_flow.py,异常处理,finally输出
0xF4A5C1,variable,function_name,function.py,基础函数,函数名
0xF4A5C2,variable,input,function.py,基础函数,参数
0xF4A5C3,variable,output,function.py,基础函数,返回值
0xF4A5D1,variable,function_name,function.py,默认参数,函数名
0xF4A5D2,variable,input,function.py,默认参数,必选参数
0xF4A5D3,variable,input,function.py,默认参数,可选参数名
0xF4A5D4,variable,input,function.py,默认参数,默认值
0xF4A5E1,variable,function_name,function.py,多返回值,函数名
0xF4A5E2,variable,input,function.py,多返回值,可迭代输入
0xF4A5F1,variable,output,function.py,lambda,lambda变量名
0xF4A5F2,variable,input,function.py,lambda,lambda参数
0xF4B6C1,variable,output,function.py,lambda双参,lambda变量名
0xF4B6C2,variable,input,function.py,lambda双参,参数1
0xF4B6C3,variable,input,function.py,lambda双参,参数2
0xF4B6D1,variable,function_name,function.py,可变参数,函数名
0xF4B6D2,variable,input,function.py,可变参数,*args
0xF4B6E1,variable,function_name,function.py,关键字参数,函数名
0xF4B6E2,variable,input,function.py,关键字参数,**kwargs
0xF4B6E3,variable,input-output,function.py,关键字参数,键变量
0xF4B6E4,variable,input-output,function.py,关键字参数,值变量
0xF4B6F1,variable,function_name,function.py,装饰器,装饰器函数名
0xF4B6F2,variable,input,function.py,装饰器,被装饰函数
0xF4B7C1,variable,function_name,function.py,装饰器,内层包装函数名
0xF4B7C2,variable,input,function.py,装饰器,包装函数*args
0xF4B7C3,variable,input,function.py,装饰器,包装函数**kwargs
0xF4B7C4,variable,output,function.py,装饰器,开始时间
0xF4B7C5,variable,output,function.py,装饰器,函数执行结果
0xF4B7C6,variable,output,function.py,装饰器,结束时间
0xD1E2C1,variable,input-output,data_structure.py,列表,列表变量
0xD1E2C2,variable,input,data_structure.py,列表,元素1
0xD1E2C3,variable,input,data_structure.py,列表,元素2
0xD1E2C4,variable,input,data_structure.py,列表,元素3
0xD1E2C5,variable,input,data_structure.py,列表,元素4
0xD1E2C6,variable,input,data_structure.py,列表,元素5
0xD1E2C7,variable,input,data_structure.py,列表,追加元素
0xD1E2C8,variable,input,data_structure.py,列表,插入位置索引
0xD1E2C9,variable,input,data_structure.py,列表,移除的目标元素
0xD1E2D1,variable,output,data_structure.py,列表,切片结果
0xD1E2D2,variable,input,data_structure.py,列表,切片起始索引
0xD1E2D3,variable,input,data_structure.py,列表,切片结束索引
0xD1E2E1,variable,output,data_structure.py,列表,列表长度
0xD1E2F1,variable,output,data_structure.py,列表推导式,推导结果列表
0xD1E2F2,variable,input-output,data_structure.py,列表推导式,推导变量
0xD1E2F3,variable,input,data_structure.py,列表推导式,指数
0xD1E2F4,variable,input,data_structure.py,列表推导式,range上限
0xD1E3C1,variable,output,data_structure.py,列表推导式(带条件),过滤结果
0xD1E3C2,variable,input-output,data_structure.py,列表推导式(带条件),推导变量
0xD1E3C3,variable,input,data_structure.py,列表推导式(带条件),range上限
0xD1E3C4,variable,input,data_structure.py,列表推导式(带条件),过滤除数
0xD1E3D1,variable,input-output,data_structure.py,字典,字典变量
0xD1E3D2,variable,input,data_structure.py,字典,键1
0xD1E3D3,variable,input,data_structure.py,字典,值1
0xD1E3D4,variable,input,data_structure.py,字典,键2
0xD1E3D5,variable,input,data_structure.py,字典,值2
0xD1E3D6,variable,input,data_structure.py,字典,新键
0xD1E3D7,variable,input,data_structure.py,字典,新值
0xD1E3E1,variable,output,data_structure.py,字典,get结果(带默认值)
0xD1E3E2,variable,input,data_structure.py,字典,get默认值
0xD1E3E3,variable,output,data_structure.py,字典,所有键列表
0xD1E3E4,variable,output,data_structure.py,字典,所有值列表
0xD1E3E5,variable,input-output,data_structure.py,字典,迭代键变量
0xD1E3E6,variable,input-output,data_structure.py,字典,迭代值变量
0xD1E3F1,variable,output,data_structure.py,字典推导式,推导字典
0xD1E3F2,variable,input-output,data_structure.py,字典推导式,推导变量
0xD1E3F3,variable,input,data_structure.py,字典推导式,值表达式指数
0xD1E3F4,variable,input,data_structure.py,字典推导式,range上限
0xD1E4B1,variable,input,data_structure.py,集合,集合1
0xD1E4B2,variable,input,data_structure.py,集合,元素1
0xD1E4B3,variable,input,data_structure.py,集合,元素2
0xD1E4B4,variable,input,data_structure.py,集合,共享元素1
0xD1E4B5,variable,input,data_structure.py,集合,共享元素2
0xD1E4B6,variable,input,data_structure.py,集合,集合2
0xD1E4B7,variable,input,data_structure.py,集合,独有元素1
0xD1E4B8,variable,input,data_structure.py,集合,独有元素2
0xD1E4C1,variable,output,data_structure.py,集合,并集
0xD1E4C2,variable,output,data_structure.py,集合,交集
0xD1E4C3,variable,output,data_structure.py,集合,差集
0xD1E4D1,variable,output,data_structure.py,元组,元组
0xD1E4D2,variable,input,data_structure.py,元组,元组元素1
0xD1E4D3,variable,input,data_structure.py,元组,元组元素2
0xD1E4D4,variable,output,data_structure.py,元组,解包变量1
0xD1E4D5,variable,output,data_structure.py,元组,解包变量2
0xD1E4E1,variable,input-output,data_structure.py,栈,栈列表
0xD1E4E2,variable,input,data_structure.py,栈,入栈元素
0xD1E4E3,variable,output,data_structure.py,栈,出栈元素
0xD1E4F1,variable,input-output,data_structure.py,队列,deque实例
0xD1E4F2,variable,input,data_structure.py,队列,入队元素
0xD1E4F3,variable,output,data_structure.py,队列,出队元素
0xE1F2C1,variable,output,string.py,基础字符串,字符串长度
0xE1F2C2,variable,input,string.py,基础字符串,源字符串
0xE1F2C3,variable,output,string.py,基础字符串,大写结果
0xE1F2C4,variable,output,string.py,基础字符串,小写结果
0xE1F2C5,variable,output,string.py,基础字符串,strip结果
0xE1F2C6,variable,input,string.py,基础字符串,待清理字符串
0xE1F2D1,variable,input,string.py,f-string格式化,变量1(名字)
0xE1F2D2,variable,input,string.py,f-string格式化,变量1(值)
0xE1F2D3,variable,input,string.py,f-string格式化,变量2(年龄)
0xE1F2D4,variable,input,string.py,f-string格式化,变量2(值)
0xE1F2D5,variable,output,string.py,f-string格式化,拼接结果1
0xE1F2D6,variable,output,string.py,f-string格式化,拼接结果2
0xE1F2D7,variable,input,string.py,f-string格式化,数值变量
0xE1F2D8,variable,input,string.py,f-string格式化,格式说明符
0xE1F2E1,variable,output,string.py,分割与合并,分割结果列表
0xE1F2E2,variable,input,string.py,分割与合并,待分割字符串
0xE1F2E3,variable,input,string.py,分割与合并,分隔符
0xE1F2E4,variable,output,string.py,分割与合并,合并结果字符串
0xE1F2E5,variable,input,string.py,分割与合并,连接符
0xE1F2F1,variable,output,string.py,字符串替换,替换结果
0xE1F2F2,variable,input,string.py,字符串替换,源字符串
0xE1F2F3,variable,input,string.py,字符串替换,被替换子串
0xE1F2F4,variable,input,string.py,字符串替换,替换为子串
0xE1F3B1,variable,output,string.py,字符串查找,find结果(索引/-1)
0xE1F3B2,variable,input,string.py,字符串查找,被搜索字符串
0xE1F3B3,variable,input,string.py,字符串查找,查找目标子串
0xE1F3B4,variable,output,string.py,字符串查找,in判断结果(bool)
0xE1F3C1,variable,output,string.py,正则,findall结果列表
0xE1F3C2,variable,input,string.py,正则,正则模式
0xE1F3C3,variable,input,string.py,正则,被搜索字符串
0xE1F3C4,variable,output,string.py,正则,sub替换结果
0xE1F3C5,variable,input,string.py,正则,sub匹配模式
0xE1F3C6,variable,input,string.py,正则,sub替换为字符串
0xE1F3C7,variable,output,string.py,正则,match结果对象
0xE1F3C8,variable,input,string.py,正则,match正则模式
0xE1F3C9,variable,input,string.py,正则,match目标字符串
0xE1F3D1,variable,output,string.py,字符串转列表,字符列表
0xE1F3D2,variable,input,string.py,字符串转列表,源字符串
0xE1F3E1,variable,input-output,string.py,多行字符串,字符串变量
0xE1F3E2,variable,input,string.py,多行字符串,多行内容
0xE1F3F1,variable,output,string.py,编解码,编码结果(bytes)
0xE1F3F2,variable,input,string.py,编解码,待编码字符串
0xE1F3F3,variable,input,string.py,编解码,编码名称(如utf-8)
0xE1F3F4,variable,output,string.py,编解码,解码结果(str)
0xB1C2C1,variable,input,OS.py,读文件,文件路径
0xB1C2C2,variable,input-output,OS.py,读文件,文件对象变量
0xB1C2C3,variable,output,OS.py,读文件,文件全部内容
0xB1C2D1,variable,input,OS.py,逐行读文件,文件路径
0xB1C2D2,variable,input-output,OS.py,逐行读文件,文件对象变量
0xB1C2D3,variable,input-output,OS.py,逐行读文件,行变量
0xB1C2E1,variable,input,OS.py,写文件,文件路径
0xB1C2E2,variable,input-output,OS.py,写文件,文件对象变量
0xB1C2E3,variable,input,OS.py,写文件,写入内容
0xB1C2F1,variable,input,OS.py,追加写入,文件路径
0xB1C2F2,variable,input-output,OS.py,追加写入,文件对象变量
0xB1C2F3,variable,input,OS.py,追加写入,追加内容
0xB1C3B1,variable,input,OS.py,文件检查,文件路径
0xB1C3B2,variable,input,OS.py,文件检查,存在时的输出
0xB1C3C1,variable,output,OS.py,列目录,目录内容列表
0xB1C3C2,variable,input,OS.py,列目录,目录路径
0xB1C3C3,variable,input-output,OS.py,列目录,迭代变量
0xB1C3D1,variable,input,OS.py,创建目录,目录路径
0xB1C3E1,variable,output,OS.py,路径处理,父目录
0xB1C3E2,variable,input,OS.py,路径处理,文件路径
0xB1C3E3,variable,output,OS.py,路径处理,文件名
0xB1C3E4,variable,output,OS.py,路径处理,文件名(无后缀)
0xB1C3E5,variable,output,OS.py,路径处理,文件后缀
0xB1C3F1,variable,output,OS.py,环境变量,环境变量值
0xB1C3F2,variable,input,OS.py,环境变量,变量名
0xB1C3F3,variable,input,OS.py,环境变量,默认值
0xB1C4B1,variable,input,OS.py,读JSON,JSON文件路径
0xB1C4B2,variable,input-output,OS.py,读JSON,文件对象变量
0xB1C4B3,variable,output,OS.py,读JSON,解析后的dict/list
0xB1C4C1,variable,input,OS.py,写JSON,JSON文件路径
0xB1C4C2,variable,input-output,OS.py,写JSON,文件对象变量
0xB1C4C3,variable,input,OS.py,写JSON,待序列化对象
0xB1C4C4,variable,input,OS.py,写JSON,缩进空格数
0xA1B2C3,variable,input-output,bubble_sort.py,冒泡排序,待排序数组
0xD4E5F6,variable,output,bubble_sort.py,冒泡排序,排序结果
0xD1E2F3,variable,input,binary_search.py,二分查找,有序数组
0xA4B5C6,variable,input,binary_search.py,二分查找,目标值
0xC7D8E9,variable,output,binary_search.py,二分查找,匹配索引
0xF1A2B3,variable,input,fibonacci.py,斐波那契,数列项数
0xC4D5E6,variable,output,fibonacci.py,斐波那契,计算结果
0xE1F2A3,variable,input,dfs_bfs.py,图遍历,图邻接表(dict)
0xB4C5D6,variable,input,dfs_bfs.py,图遍历,起始节点
0xD7E8F9,variable,output,dfs_bfs.py,图遍历,遍历结果(visited集合)
0xB1C2D1,variable,function_name,greedy_algorithm.py,活动选择,函数名
0xB1C2D2,variable,input,greedy_algorithm.py,活动选择,活动列表(含时间区间)
0xB1C2D3,variable,output,greedy_algorithm.py,活动选择,排序后活动列表
0xB1C2D4,variable,input-output,greedy_algorithm.py,活动选择,排序lambda参数
0xB1C2D5,variable,input,greedy_algorithm.py,活动选择,排序用的索引/键
0xB1C2D6,variable,output,greedy_algorithm.py,活动选择,已选活动列表
0xB1C2D7,variable,output,greedy_algorithm.py,活动选择,当前结束时间
0xB1C2D8,variable,input,greedy_algorithm.py,活动选择,结束时间索引/键
0xB1C2D9,variable,input-output,greedy_algorithm.py,活动选择,活动开始时间
0xB1C2E1,variable,input-output,greedy_algorithm.py,活动选择,活动结束时间
0xB1C2E2,variable,input,greedy_algorithm.py,活动选择,起始索引
0xB1C2E3,variable,output,greedy_algorithm.py,活动选择,返回结果
0xB1C2E4,variable,function_name,greedy_algorithm.py,零钱兑换,函数名
0xB1C2E5,variable,input,greedy_algorithm.py,零钱兑换,硬币面额列表
0xB1C2E6,variable,output,greedy_algorithm.py,零钱兑换,排序后面额列表
0xB1C2E7,variable,output,greedy_algorithm.py,零钱兑换,找零结果dict
0xB1C2E8,variable,input-output,greedy_algorithm.py,零钱兑换,当前面额
0xB1C2E9,variable,output,greedy_algorithm.py,零钱兑换,该面额使用数量
0xB1C2F1,variable,output,greedy_algorithm.py,零钱兑换,返回结果
0xC1D2C1,variable,function_name,game_of_life.py,生命游戏,创建网格函数名
0xC1D2C2,variable,function_name,game_of_life.py,生命游戏,随机初始化函数名
0xC1D2C3,variable,input-output,game_of_life.py,生命游戏,行索引
0xC1D2C4,variable,input-output,game_of_life.py,生命游戏,列索引
0xC1D2C5,variable,function_name,game_of_life.py,生命游戏,计算邻居函数名
0xC1D2C6,variable,output,game_of_life.py,生命游戏,网格行数
0xC1D2C7,variable,output,game_of_life.py,生命游戏,网格列数
0xC1D2C8,variable,input-output,game_of_life.py,生命游戏,邻居计数器
0xC1D2C9,variable,input,game_of_life.py,生命游戏,行偏移
0xC1D2D1,variable,input,game_of_life.py,生命游戏,列偏移
0xC1D2D2,variable,output,game_of_life.py,生命游戏,邻居行坐标
0xC1D2D3,variable,output,game_of_life.py,生命游戏,邻居列坐标
0xC1D2D4,variable,function_name,game_of_life.py,生命游戏,下一代函数名
0xC1D2D5,variable,output,game_of_life.py,生命游戏,当前网格行数
0xC1D2D6,variable,output,game_of_life.py,生命游戏,当前网格列数
0xC1D2D7,variable,output,game_of_life.py,生命游戏,新网格
0xC1D2D8,variable,input-output,game_of_life.py,生命游戏,行迭代变量
0xC1D2D9,variable,input-output,game_of_life.py,生命游戏,列迭代变量
0xC1D2E1,variable,output,game_of_life.py,生命游戏,邻居数
0xC1D2E2,variable,function_name,game_of_life.py,生命游戏,打印网格函数名
0xC1D2E3,variable,input-output,game_of_life.py,生命游戏,行迭代变量
0xC1D2E4,variable,output,game_of_life.py,生命游戏,渲染行字符串
0xC1D2E5,variable,input-output,game_of_life.py,生命游戏,单元格状态
0xC1D2E6,variable,input,game_of_life.py,生命游戏,网格行数
0xC1F4B1,variable,input-output,game_of_life.py,生命游戏,网格实例
0xC1F4B2,variable,input,game_of_life.py,生命游戏,网格列数
0xC1F4B3,variable,input,game_of_life.py,生命游戏,迭代次数
0xC1F4B4,variable,input,game_of_life.py,生命游戏,迭代次数赋值源
0xC1F4B5,variable,input-output,game_of_life.py,生命游戏,代数计数器
0xB1E4C1,variable,class_name,account_management.py,账户管理,类名
0xB1E4C2,variable,input,account_management.py,账户管理,数据文件路径
0xB1E4C3,variable,input,account_management.py,账户管理,默认文件路径
0xB1E4C4,variable,input-output,account_management.py,账户管理,账户数据(dict)
0xB1E4C5,variable,function_name,account_management.py,账户管理,加载数据方法
0xB1E4C6,variable,input-output,account_management.py,账户管理,读文件对象
0xB1E4C7,variable,function_name,account_management.py,账户管理,保存数据方法
0xB1E4C8,variable,input-output,account_management.py,账户管理,写文件对象
0xB1E4C9,variable,input,account_management.py,账户管理,JSON缩进
0xB1E4D1,variable,function_name,account_management.py,账户管理,注册方法
0xB1E4D2,variable,input,account_management.py,账户管理,用户名
0xB1E4D3,variable,input,account_management.py,账户管理,密码
0xB1E4D4,variable,input,account_management.py,账户管理,错误消息-已存在
0xB1E4D5,variable,input,account_management.py,账户管理,用户名最小长度
0xB1E4D6,variable,input,account_management.py,账户管理,错误消息-用户名太短
0xB1E4D7,variable,input,account_management.py,账户管理,密码最小长度
0xB1E4D8,variable,input,account_management.py,账户管理,错误消息-密码太短
0xB1E4D9,variable,input,account_management.py,账户管理,密码字段键名
0xB1E4E1,variable,input,account_management.py,账户管理,资料字段键名
0xB1E4E2,variable,output,account_management.py,账户管理,注册成功结果
0xB1E4E3,variable,input,account_management.py,账户管理,成功消息
0xB1E4E4,variable,function_name,account_management.py,账户管理,登录方法
0xB1E4E5,variable,input,account_management.py,账户管理,错误消息-不存在
0xB1E4E6,variable,input,account_management.py,账户管理,错误消息-密码错误
0xB1E4E7,variable,output,account_management.py,账户管理,登录成功结果
0xB1E4E8,variable,input,account_management.py,账户管理,登录成功消息
0xB1E4E9,variable,function_name,account_management.py,账户管理,更新资料方法
0xB1E4F1,variable,input,account_management.py,账户管理,资料字段名
0xB1E4F2,variable,input,account_management.py,账户管理,新值
0xB1E4F3,variable,output,account_management.py,账户管理,更新成功结果
0xB1E4F4,variable,input,account_management.py,账户管理,更新成功消息
0xB1E4F5,variable,function_name,account_management.py,账户管理,删除账户方法
0xB1E4F6,variable,output,account_management.py,账户管理,删除成功结果
0xB1E4F7,variable,input,account_management.py,账户管理,删除成功消息
0xB1E4F8,variable,function_name,account_management.py,账户管理,列出用户方法
0xD0E1F2,reference,output,account_management.py,跨文件引用,→OS.py.0xB1C4B3(JSON读取)
0xD0E1F3,reference,output,account_management.py,跨文件引用,→OS.py.0xB1C4C1(JSON写入)
0x334455,reference,output,account_management.py,跨文件引用,→data_structure.py.0xD1E3D1(dict存储)
0xA1D4C1,variable,class_name,actor_system.py,Actor系统,Actor类名
0xA1D4C2,variable,input,actor_system.py,Actor系统,Actor名称
0xA1D4C3,variable,input,actor_system.py,Actor系统,自定义消息处理器
0xA1D4C4,variable,output,actor_system.py,Actor系统,Actor名称(实例属性)
0xA1D4C5,variable,input-output,actor_system.py,Actor系统,消息队列(deque)
0xA1D4C6,variable,input-output,actor_system.py,Actor系统,消息处理函数
0xA1D4C7,variable,function_name,actor_system.py,Actor系统,默认消息处理器
0xA1D4C8,variable,input-output,actor_system.py,Actor系统,运行状态标志
0xA1D4C9,variable,input,actor_system.py,Actor系统,消息内容
0xA1D4D1,variable,input,actor_system.py,Actor系统,发送者名称
0xA1D4D2,variable,function_name,actor_system.py,Actor系统,发送消息方法
0xA1D4D3,variable,input,actor_system.py,Actor系统,默认发送者
0xA1D4D4,variable,input,actor_system.py,Actor系统,默认发送者值
0xA1D4D5,variable,function_name,actor_system.py,Actor系统,处理消息方法
0xA1D4D6,variable,class_name,actor_system.py,Actor系统,ActorSystem类名
0xA1D4D7,variable,input-output,actor_system.py,Actor系统,Actor注册表(dict)
0xA1D4D8,variable,function_name,actor_system.py,Actor系统,注册Actor方法
0xA1D4D9,variable,input,actor_system.py,Actor系统,待注册Actor实例
0xA1D4E1,variable,input,actor_system.py,Actor系统,目标Actor名称
0xA1D4E2,variable,function_name,actor_system.py,Actor系统,运行Actor方法
0xA1D4E3,variable,input,actor_system.py,Actor系统,待运行Actor名称
0xA1D4E4,variable,function_name,actor_system.py,Actor系统,广播方法
0xA1D4E5,variable,input-output,actor_system.py,Actor系统,迭代变量-Actor名
0xA1D4E6,variable,function_name,actor_system.py,Actor系统,运行所有方法
0xA1D4E7,variable,input-output,actor_system.py,Actor系统,迭代变量-Actor实例
0x112233,reference,output,actor_system.py,跨文件引用,→data_structure.py.0xD1E4F1(消息队列deque)
0x445566,reference,output,actor_system.py,跨文件引用,处理器注册(内部)
0xC1F4C1,variable,input-output,api_server.py,API服务器,数据存储(dict)
0xC1F4C2,variable,input,api_server.py,API服务器,数据集合键名
0xC1F4C3,variable,input,api_server.py,API服务器,记录ID字段名
0xC1F4C4,variable,input,api_server.py,API服务器,记录字段1值
0xC1F4C5,variable,input,api_server.py,API服务器,记录字段2名
0xC1F4C6,variable,input,api_server.py,API服务器,记录字段2值
0xC1F4C7,variable,input,api_server.py,API服务器,记录字段3名
0xC1F4C8,variable,input,api_server.py,API服务器,记录字段3值
0xC1F4C9,variable,input,api_server.py,API服务器,记录2字段2值
0xC1F4D1,variable,input,api_server.py,API服务器,记录2字段3值
0xC1F4D2,variable,input,api_server.py,API服务器,记录2字段4值
0xC1F4D3,variable,class_name,api_server.py,API服务器,请求处理类名
0xC1F4D4,variable,function_name,api_server.py,API服务器,发送JSON响应方法
0xC1F4D5,variable,input,api_server.py,API服务器,响应数据
0xC1F4D6,variable,input,api_server.py,API服务器,HTTP状态码
0xC1F4D7,variable,input,api_server.py,API服务器,默认成功状态码
0xC1F4D8,variable,input,api_server.py,API服务器,响应头名称
0xC1F4D9,variable,input,api_server.py,API服务器,响应头值
0xC1F4E1,variable,input,api_server.py,API服务器,编码名称
0xC1F4E2,variable,input,api_server.py,API服务器,列表端点路径
0xC1F4E3,variable,input,api_server.py,API服务器,详情端点路径前缀
0xC1F4E4,variable,output,api_server.py,API服务器,URL中的ID(int)
0xC1F4E5,variable,input,api_server.py,API服务器,路径分隔符
0xC1F4E6,variable,output,api_server.py,API服务器,匹配的记录
0xC1F4E7,variable,input-output,api_server.py,API服务器,迭代变量-记录
0xC1F4E8,variable,input,api_server.py,API服务器,错误消息键名
0xC1F4E9,variable,input,api_server.py,API服务器,错误消息值
0xC1F4F1,variable,input,api_server.py,API服务器,未找到状态码
0xC1F4F2,variable,input,api_server.py,API服务器,根路径消息键名
0xC1F4F3,variable,input,api_server.py,API服务器,根路径消息值
0xC1F4F4,variable,output,api_server.py,API服务器,请求体长度
0xC1F4F5,variable,input,api_server.py,API服务器,请求头-Content-Length
0xC1F4F6,variable,input-output,api_server.py,API服务器,新记录数据
0xC1F4F7,variable,output,api_server.py,API服务器,新记录ID
0xC1F4F8,variable,input,api_server.py,API服务器,创建成功状态码
0xC1F4F9,variable,input,api_server.py,API服务器,不允许方法消息
0xC1F5B1,variable,input,api_server.py,API服务器,日志格式变量
0xC1F5B2,variable,input-output,api_server.py,API服务器,日志可变参数
0xC1F5B3,variable,function_name,api_server.py,API服务器,启动函数名
0xC1F5B4,variable,input,api_server.py,API服务器,绑定主机
0xC1F5B5,variable,input,api_server.py,API服务器,默认主机
0xC1F5B6,variable,input,api_server.py,API服务器,绑定端口
0xC1F5B7,variable,input,api_server.py,API服务器,默认端口
0xC1F5B8,variable,output,api_server.py,API服务器,HTTPServer实例
0xC1F5B9,variable,input,api_server.py,API服务器,欢迎消息
0xC1F5C1,variable,input,api_server.py,API服务器,关闭消息
0x566778,reference,output,api_server.py,跨文件引用,→OS.py.0xB1C4C3(JSON序列化)
0x889900,reference,output,api_server.py,跨文件引用,→data_structure.py.0xD1E3D1(dict存储)
```


# ══════════════════════════════════════════════════════════════════
# [2] JSON — 接口契约
# 核糖体（Avengers.py）直接 parse 使用的精确契约
# ══════════════════════════════════════════════════════════════════
```json
{
  "version": "3.1",
  "languages": ["Python", "TypeScript", "Cpp"],
  "default_language": "python",
  "language_dirs": {
    "Python": "Python/",
    "TypeScript": "TypeScript/",
    "Cpp": "Cpp/"
  },
  "interface_points": {
    "0xA1B2C1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "加法结果" },
    "0xA1B2C2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "加法左操作数" },
    "0xA1B2C3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "加法右操作数" },
    "0xA1B2D1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "减法结果" },
    "0xA1B2D2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "减法左操作数" },
    "0xA1B2D3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "减法右操作数" },
    "0xA1B2E1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "乘法结果" },
    "0xA1B2E2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "乘法左操作数" },
    "0xA1B2E3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "乘法右操作数" },
    "0xA1B2F1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "除法结果" },
    "0xA1B2F2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "除法左操作数" },
    "0xA1B2F3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "算术赋值", "desc": "除法右操作数" },
    "0xA1C3B1": { "type": "variable", "role": "input-output", "param_type": "number", "file": "calculator.py", "section": "自增自减", "desc": "计数器变量" },
    "0xA1C3B2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "自增自减", "desc": "初始值" },
    "0xA1C3B3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "自增自减", "desc": "步长值" },
    "0xA1D4B1": { "type": "variable", "role": "input-output", "param_type": "any", "file": "calculator.py", "section": "类型转换", "desc": "源变量" },
    "0xA1D4B2": { "type": "variable", "role": "input", "param_type": "any", "file": "calculator.py", "section": "类型转换", "desc": "待转换值" },
    "0xA1D4C1": { "type": "variable", "role": "output", "param_type": "int", "file": "calculator.py", "section": "类型转换", "desc": "int转换结果" },
    "0xA1D4D1": { "type": "variable", "role": "output", "param_type": "float", "file": "calculator.py", "section": "类型转换", "desc": "float转换结果" },
    "0xA1D4E1": { "type": "variable", "role": "output", "param_type": "str", "file": "calculator.py", "section": "类型转换", "desc": "str转换结果" },
    "0xA1D4F1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "类型转换", "desc": "round结果" },
    "0xA1D4F2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "类型转换", "desc": "round源值" },
    "0xA1D4F3": { "type": "variable", "role": "input", "param_type": "int", "file": "calculator.py", "section": "类型转换", "desc": "round精度" },
    "0xA1E5B1": { "type": "variable", "role": "output", "param_type": "float", "file": "calculator.py", "section": "数学运算", "desc": "sqrt结果" },
    "0xA1E5B2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "sqrt操作数" },
    "0xA1E5C1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "abs结果" },
    "0xA1E5C2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "abs操作数" },
    "0xA1E5D1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "max结果" },
    "0xA1E5D2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "max操作数1" },
    "0xA1E5D3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "max操作数2" },
    "0xA1E5D4": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "max操作数3" },
    "0xA1E5E1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "min结果" },
    "0xA1E5E2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "min操作数1" },
    "0xA1E5E3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "min操作数2" },
    "0xA1E5E4": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "min操作数3" },
    "0xA1E5F1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "pow结果" },
    "0xA1E5F2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "pow底数" },
    "0xA1E5F3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "数学运算", "desc": "pow指数" },
    "0xA1F6B1": { "type": "variable", "role": "output", "param_type": "number", "file": "calculator.py", "section": "取模整除", "desc": "取模结果" },
    "0xA1F6B2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "取模整除", "desc": "被除数" },
    "0xA1F6B3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "取模整除", "desc": "除数" },
    "0xA1F6C1": { "type": "variable", "role": "output", "param_type": "int", "file": "calculator.py", "section": "取模整除", "desc": "整除结果" },
    "0xA1F6C2": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "取模整除", "desc": "被除数" },
    "0xA1F6C3": { "type": "variable", "role": "input", "param_type": "number", "file": "calculator.py", "section": "取模整除", "desc": "除数" },

    "0xF1A2C1": { "type": "variable", "role": "input", "param_type": "any", "file": "console.py", "section": "打印", "desc": "打印内容" },
    "0xF1A2D1": { "type": "variable", "role": "output", "param_type": "str", "file": "console.py", "section": "输入", "desc": "接收到的输入值" },
    "0xF1A2D2": { "type": "variable", "role": "input", "param_type": "str", "file": "console.py", "section": "输入", "desc": "提示文字" },
    "0xF1B3D1": { "type": "literal", "role": "input", "param_type": "str", "file": "console.py", "section": "日志", "desc": "日志级别(logging.DEBUG/INFO/WARNING/ERROR/CRITICAL)" },
    "0xF1B3D2": { "type": "literal", "role": "input", "param_type": "str", "file": "console.py", "section": "日志", "desc": "日志格式字符串" },

    "0xC1D2C1": { "type": "variable", "role": "input", "param_type": "any", "file": "control_flow.py", "section": "条件判断", "desc": "比较变量" },
    "0xC1D2C2": { "type": "variable", "role": "input", "param_type": "any", "file": "control_flow.py", "section": "条件判断", "desc": "阈值1" },
    "0xC1D2C3": { "type": "variable", "role": "output", "param_type": "any", "file": "control_flow.py", "section": "条件判断", "desc": "结果变量" },
    "0xC1D2D1": { "type": "variable", "role": "input-output", "param_type": "int", "file": "control_flow.py", "section": "for循环", "desc": "循环变量" },
    "0xC1D2D2": { "type": "variable", "role": "input", "param_type": "int", "file": "control_flow.py", "section": "for循环", "desc": "迭代上限" },
    "0xC1D3C1": { "type": "variable", "role": "input-output", "param_type": "number", "file": "control_flow.py", "section": "while循环", "desc": "循环变量" },
    "0xC1D3C3": { "type": "variable", "role": "input", "param_type": "number", "file": "control_flow.py", "section": "while循环", "desc": "终止条件" },
    "0xC1D4C1": { "type": "variable", "role": "output", "param_type": "number", "file": "control_flow.py", "section": "异常处理", "desc": "除法结果" },
    "0xC1D4C2": { "type": "variable", "role": "input", "param_type": "number", "file": "control_flow.py", "section": "异常处理", "desc": "被除数" },
    "0xC1D4C3": { "type": "variable", "role": "input", "param_type": "number", "file": "control_flow.py", "section": "异常处理", "desc": "除数" },
    "0xC1D4C4": { "type": "variable", "role": "input", "param_type": "type", "file": "control_flow.py", "section": "异常处理", "desc": "异常类型" },

    "0xF4A5C1": { "type": "variable", "role": "function_name", "param_type": "str", "file": "function.py", "section": "基础函数", "desc": "函数名" },
    "0xF4A5C2": { "type": "variable", "role": "input", "param_type": "any", "file": "function.py", "section": "基础函数", "desc": "参数" },
    "0xF4A5C3": { "type": "variable", "role": "output", "param_type": "any", "file": "function.py", "section": "基础函数", "desc": "返回值" },
    "0xF4A5D1": { "type": "variable", "role": "function_name", "param_type": "str", "file": "function.py", "section": "默认参数", "desc": "函数名" },
    "0xF4A5D2": { "type": "variable", "role": "input", "param_type": "any", "file": "function.py", "section": "默认参数", "desc": "必选参数" },
    "0xF4A5D3": { "type": "variable", "role": "input", "param_type": "str", "file": "function.py", "section": "默认参数", "desc": "可选参数名" },
    "0xF4A5D4": { "type": "variable", "role": "input", "param_type": "any", "file": "function.py", "section": "默认参数", "desc": "默认值" },
    "0xF4A5F1": { "type": "variable", "role": "output", "param_type": "callable", "file": "function.py", "section": "lambda", "desc": "lambda变量名" },
    "0xF4A5F2": { "type": "variable", "role": "input", "param_type": "any", "file": "function.py", "section": "lambda", "desc": "lambda参数" },
    "0xF4B6D1": { "type": "variable", "role": "function_name", "param_type": "str", "file": "function.py", "section": "可变参数", "desc": "函数名" },
    "0xF4B6D2": { "type": "variable", "role": "input", "param_type": "any", "file": "function.py", "section": "可变参数", "desc": "*args" },
    "0xF4B6E1": { "type": "variable", "role": "function_name", "param_type": "str", "file": "function.py", "section": "关键字参数", "desc": "函数名" },
    "0xF4B6E2": { "type": "variable", "role": "input", "param_type": "any", "file": "function.py", "section": "关键字参数", "desc": "**kwargs" },
    "0xF4B6F1": { "type": "variable", "role": "function_name", "param_type": "str", "file": "function.py", "section": "装饰器", "desc": "装饰器函数名" },
    "0xF4B6F2": { "type": "variable", "role": "input", "param_type": "callable", "file": "function.py", "section": "装饰器", "desc": "被装饰函数" },

    "0xD1E2C1": { "type": "variable", "role": "input-output", "param_type": "list", "file": "data_structure.py", "section": "列表", "desc": "列表变量" },
    "0xD1E2C2": { "type": "variable", "role": "input", "param_type": "any", "file": "data_structure.py", "section": "列表", "desc": "元素1" },
    "0xD1E2E1": { "type": "variable", "role": "output", "param_type": "list", "file": "data_structure.py", "section": "列表", "desc": "切片结果" },
    "0xD1E2E2": { "type": "variable", "role": "input", "param_type": "int", "file": "data_structure.py", "section": "列表", "desc": "切片起始索引" },
    "0xD1E2E3": { "type": "variable", "role": "input", "param_type": "int", "file": "data_structure.py", "section": "列表", "desc": "切片结束索引" },
    "0xD1E3D1": { "type": "variable", "role": "input-output", "param_type": "dict", "file": "data_structure.py", "section": "字典", "desc": "字典变量" },
    "0xD1E3D2": { "type": "variable", "role": "input", "param_type": "hashable", "file": "data_structure.py", "section": "字典", "desc": "键1" },
    "0xD1E3D3": { "type": "variable", "role": "input", "param_type": "any", "file": "data_structure.py", "section": "字典", "desc": "值1" },
    "0xD1E4B1": { "type": "variable", "role": "input", "param_type": "set", "file": "data_structure.py", "section": "集合", "desc": "集合1" },
    "0xD1E4E1": { "type": "variable", "role": "input-output", "param_type": "list", "file": "data_structure.py", "section": "栈", "desc": "栈列表" },
    "0xD1E4E2": { "type": "variable", "role": "input", "param_type": "any", "file": "data_structure.py", "section": "栈", "desc": "入栈元素" },
    "0xD1E4F1": { "type": "variable", "role": "input-output", "param_type": "deque", "file": "data_structure.py", "section": "队列", "desc": "deque实例" },

    "0xE1F2C1": { "type": "variable", "role": "output", "param_type": "int", "file": "string.py", "section": "基础字符串", "desc": "字符串长度" },
    "0xE1F2C2": { "type": "variable", "role": "input", "param_type": "str", "file": "string.py", "section": "基础字符串", "desc": "源字符串" },
    "0xE1F3C2": { "type": "variable", "role": "input", "param_type": "str", "file": "string.py", "section": "正则", "desc": "正则模式" },
    "0xE1F3C3": { "type": "variable", "role": "input", "param_type": "str", "file": "string.py", "section": "正则", "desc": "被搜索字符串" },

    "0xB1C2C1": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "读文件", "desc": "文件路径" },
    "0xB1C2C2": { "type": "variable", "role": "input-output", "param_type": "file", "file": "OS.py", "section": "读文件", "desc": "文件对象变量" },
    "0xB1C2C3": { "type": "variable", "role": "output", "param_type": "str", "file": "OS.py", "section": "读文件", "desc": "文件全部内容" },
    "0xB1C2E1": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "写文件", "desc": "文件路径" },
    "0xB1C2E3": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "写文件", "desc": "写入内容" },
    "0xB1C3B1": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "文件检查", "desc": "文件路径" },
    "0xB1C3C1": { "type": "variable", "role": "output", "param_type": "list[str]", "file": "OS.py", "section": "列目录", "desc": "目录内容列表" },
    "0xB1C3D1": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "创建目录", "desc": "目录路径" },
    "0xB1C4B1": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "读JSON", "desc": "JSON文件路径" },
    "0xB1C4B3": { "type": "variable", "role": "output", "param_type": "dict|list", "file": "OS.py", "section": "读JSON", "desc": "解析后的dict/list" },
    "0xB1C4C1": { "type": "variable", "role": "input", "param_type": "str", "file": "OS.py", "section": "写JSON", "desc": "JSON文件路径" },
    "0xB1C4C3": { "type": "variable", "role": "input", "param_type": "dict|list", "file": "OS.py", "section": "写JSON", "desc": "待序列化对象" },
    "0xB1C4C4": { "type": "variable", "role": "input", "param_type": "int", "file": "OS.py", "section": "写JSON", "desc": "缩进空格数" },

    "0xA1B2C3_s": { "type": "variable", "role": "input-output", "param_type": "list", "file": "bubble_sort.py", "section": "冒泡排序", "desc": "待排序数组", "alias": "0xA1B2C3" },
    "0xD4E5F6": { "type": "variable", "role": "output", "param_type": "list", "file": "bubble_sort.py", "section": "冒泡排序", "desc": "排序结果" },

    "0xD1E2F3_s": { "type": "variable", "role": "input", "param_type": "list", "file": "binary_search.py", "section": "二分查找", "desc": "有序数组", "alias": "0xD1E2F3" },
    "0xA4B5C6": { "type": "variable", "role": "input", "param_type": "any", "file": "binary_search.py", "section": "二分查找", "desc": "目标值" },
    "0xC7D8E9": { "type": "variable", "role": "output", "param_type": "int", "file": "binary_search.py", "section": "二分查找", "desc": "匹配索引(-1未找到)" },

    "0xF1A2B3": { "type": "variable", "role": "input", "param_type": "int", "file": "fibonacci.py", "section": "斐波那契", "desc": "数列项数" },
    "0xC4D5E6": { "type": "variable", "role": "output", "param_type": "int", "file": "fibonacci.py", "section": "斐波那契", "desc": "计算结果" },

    "0xE1F2A3": { "type": "variable", "role": "input", "param_type": "dict", "file": "dfs_bfs.py", "section": "图遍历", "desc": "图邻接表" },
    "0xB4C5D6": { "type": "variable", "role": "input", "param_type": "hashable", "file": "dfs_bfs.py", "section": "图遍历", "desc": "起始节点" },
    "0xD7E8F9": { "type": "variable", "role": "output", "param_type": "set", "file": "dfs_bfs.py", "section": "图遍历", "desc": "遍历结果" },

    "0xB1C2D1": { "type": "variable", "role": "function_name", "param_type": "str", "file": "greedy_algorithm.py", "section": "活动选择", "desc": "函数名" },
    "0xB1C2D2": { "type": "variable", "role": "input", "param_type": "list[tuple]", "file": "greedy_algorithm.py", "section": "活动选择", "desc": "活动列表(含时间区间)" },
    "0xB1C2E3": { "type": "variable", "role": "output", "param_type": "list[tuple]", "file": "greedy_algorithm.py", "section": "活动选择", "desc": "已选活动列表" },
    "0xB1C2E4": { "type": "variable", "role": "function_name", "param_type": "str", "file": "greedy_algorithm.py", "section": "零钱兑换", "desc": "函数名" },
    "0xB1C2E5": { "type": "variable", "role": "input", "param_type": "list[int]", "file": "greedy_algorithm.py", "section": "零钱兑换", "desc": "硬币面额列表" },
    "0xB1C2F1": { "type": "variable", "role": "output", "param_type": "dict", "file": "greedy_algorithm.py", "section": "零钱兑换", "desc": "找零结果" },

    "0xC1D2C1_g": { "type": "variable", "role": "function_name", "param_type": "str", "file": "game_of_life.py", "section": "生命游戏", "desc": "创建网格函数名", "alias": "0xC1D2C1" },
    "0xC1D2C2_g": { "type": "variable", "role": "function_name", "param_type": "str", "file": "game_of_life.py", "section": "生命游戏", "desc": "随机初始化函数名", "alias": "0xC1D2C2" },
    "0xC1D2E6": { "type": "variable", "role": "input", "param_type": "int", "file": "game_of_life.py", "section": "生命游戏", "desc": "网格行数" },
    "0xC1F4B2": { "type": "variable", "role": "input", "param_type": "int", "file": "game_of_life.py", "section": "生命游戏", "desc": "网格列数" },
    "0xC1F4B3": { "type": "variable", "role": "input", "param_type": "int", "file": "game_of_life.py", "section": "生命游戏", "desc": "迭代次数" },

    "0xB1E4C1": { "type": "variable", "role": "class_name", "param_type": "str", "file": "account_management.py", "section": "账户管理", "desc": "类名" },
    "0xB1E4C2": { "type": "variable", "role": "input", "param_type": "str", "file": "account_management.py", "section": "账户管理", "desc": "数据文件路径" },
    "0xB1E4C3": { "type": "literal", "role": "input", "param_type": "str", "file": "account_management.py", "section": "账户管理", "desc": "默认文件路径" },
    "0xB1E4C4": { "type": "variable", "role": "input-output", "param_type": "dict", "file": "account_management.py", "section": "账户管理", "desc": "账户数据" },
    "0xB1E4D2": { "type": "variable", "role": "input", "param_type": "str", "file": "account_management.py", "section": "账户管理", "desc": "用户名" },
    "0xB1E4D3": { "type": "variable", "role": "input", "param_type": "str", "file": "account_management.py", "section": "账户管理", "desc": "密码" },
    "0xD0E1F2": { "type": "reference", "role": "output", "param_type": null, "file": "account_management.py", "section": "跨文件引用", "desc": "→OS.py.0xB1C4B3(JSON读取)", "target_file": "OS.py", "target_hex": "0xB1C4B3" },
    "0xD0E1F3": { "type": "reference", "role": "output", "param_type": null, "file": "account_management.py", "section": "跨文件引用", "desc": "→OS.py.0xB1C4C1(JSON写入)", "target_file": "OS.py", "target_hex": "0xB1C4C1" },
    "0x334455": { "type": "reference", "role": "output", "param_type": null, "file": "account_management.py", "section": "跨文件引用", "desc": "→data_structure.py.0xD1E3D1(dict存储)", "target_file": "data_structure.py", "target_hex": "0xD1E3D1" },

    "0xA1D4C1_a": { "type": "variable", "role": "class_name", "param_type": "str", "file": "actor_system.py", "section": "Actor系统", "desc": "Actor类名", "alias": "0xA1D4C1" },
    "0xA1D4C2": { "type": "variable", "role": "input", "param_type": "str", "file": "actor_system.py", "section": "Actor系统", "desc": "Actor名称" },
    "0xA1D4C5": { "type": "variable", "role": "input-output", "param_type": "deque", "file": "actor_system.py", "section": "Actor系统", "desc": "消息队列" },
    "0xA1D4D6": { "type": "variable", "role": "class_name", "param_type": "str", "file": "actor_system.py", "section": "Actor系统", "desc": "ActorSystem类名" },
    "0xA1D4D7": { "type": "variable", "role": "input-output", "param_type": "dict", "file": "actor_system.py", "section": "Actor系统", "desc": "Actor注册表" },
    "0x112233": { "type": "reference", "role": "output", "param_type": null, "file": "actor_system.py", "section": "跨文件引用", "desc": "→data_structure.py.0xD1E4F1(消息队列deque)", "target_file": "data_structure.py", "target_hex": "0xD1E4F1" },

    "0xC1F4C1": { "type": "variable", "role": "input-output", "param_type": "dict", "file": "api_server.py", "section": "API服务器", "desc": "数据存储" },
    "0xC1F4C2": { "type": "literal", "role": "input", "param_type": "str", "file": "api_server.py", "section": "API服务器", "desc": "数据集合键名" },
    "0xC1F4D3": { "type": "variable", "role": "class_name", "param_type": "str", "file": "api_server.py", "section": "API服务器", "desc": "请求处理类名" },
    "0xC1F4E2": { "type": "literal", "role": "input", "param_type": "str", "file": "api_server.py", "section": "API服务器", "desc": "列表端点路径" },
    "0xC1F4E3": { "type": "literal", "role": "input", "param_type": "str", "file": "api_server.py", "section": "API服务器", "desc": "详情端点路径前缀" },
    "0xC1F5B3": { "type": "variable", "role": "function_name", "param_type": "str", "file": "api_server.py", "section": "API服务器", "desc": "启动函数名" },
    "0xC1F5B4": { "type": "variable", "role": "input", "param_type": "str", "file": "api_server.py", "section": "API服务器", "desc": "绑定主机" },
    "0xC1F5B6": { "type": "variable", "role": "input", "param_type": "int", "file": "api_server.py", "section": "API服务器", "desc": "绑定端口" },
    "0x566778": { "type": "reference", "role": "output", "param_type": null, "file": "api_server.py", "section": "跨文件引用", "desc": "→OS.py.0xB1C4C3(JSON序列化)", "target_file": "OS.py", "target_hex": "0xB1C4C3" },
    "0x889900": { "type": "reference", "role": "output", "param_type": null, "file": "api_server.py", "section": "跨文件引用", "desc": "→data_structure.py.0xD1E3D1(dict存储)", "target_file": "data_structure.py", "target_hex": "0xD1E3D1" }
  },
  "cross_file_references": [
    { "source_hex": "0xD0E1F2", "target_file": "OS.py", "target_hex": "0xB1C4B3", "desc": "JSON文件读取" },
    { "source_hex": "0xD0E1F3", "target_file": "OS.py", "target_hex": "0xB1C4C1", "desc": "JSON文件写入" },
    { "source_hex": "0x334455", "target_file": "data_structure.py", "target_hex": "0xD1E3D1", "desc": "dict存储结构" },
    { "source_hex": "0x112233", "target_file": "data_structure.py", "target_hex": "0xD1E4F1", "desc": "消息队列deque" },
    { "source_hex": "0x566778", "target_file": "OS.py", "target_hex": "0xB1C4C3", "desc": "JSON序列化" },
    { "source_hex": "0x889900", "target_file": "data_structure.py", "target_hex": "0xD1E3D1", "desc": "dict数据存储" }
  ]
}
```


# ══════════════════════════════════════════════════════════════════
# [3] YAML — 素材关系
# 描述素材之间的依赖、层级、跨文件引用关系
# 核糖体用这个确定组装顺序
# ══════════════════════════════════════════════════════════════════
```yaml
# 素材层级结构
layers:
  Level1:
    desc: "原子操作 — Python 基础语法最小单元"
    materials:
      calculator:
        file: Python/Level1/calculator.py
        desc: "算术运算、类型转换、数学函数"
        hex_count: 26
        sections:
          - 算术赋值
          - 自增自减
          - 类型转换
          - 数学运算
          - 取模整除
        depends_on: []
        imported_by: [Level2.bubble_sort, Level2.binary_search, Level2.fibonacci, Level2.greedy_algorithm]

      console:
        file: Python/Level1/console.py
        desc: "打印、输入、格式化输出、日志、表格打印"
        hex_count: 26
        sections:
          - 打印
          - 输入
          - 格式化打印
          - stderr输出
          - 日志
          - 表格打印
        depends_on: []
        imported_by: [Level2.game_of_life, Level3.api_server]

      control_flow:
        file: Python/Level1/control_flow.py
        desc: "if-else、for、while、break、continue、嵌套循环、try-except"
        hex_count: 30
        sections:
          - 条件判断
          - for循环(range)
          - for循环(可迭代)
          - for循环(enumerate)
          - while循环
          - break
          - continue
          - 嵌套循环
          - 异常处理
        depends_on: []
        imported_by: [Level2.all]

      function:
        file: Python/Level1/function.py
        desc: "函数定义、默认参数、多返回值、lambda、*args/**kwargs、装饰器"
        hex_count: 22
        sections:
          - 基础函数
          - 默认参数
          - 多返回值
          - lambda
          - lambda双参
          - 可变参数
          - 关键字参数
          - 装饰器
        depends_on: []
        imported_by: [Level2.all, Level3.all]

      data_structure:
        file: Python/Level1/data_structure.py
        desc: "列表、字典、集合、元组、栈、队列"
        hex_count: 41
        sections:
          - 列表
          - 列表推导式
          - 列表推导式(带条件)
          - 字典
          - 字典推导式
          - 集合
          - 元组
          - 栈
          - 队列
        depends_on: []
        imported_by: [Level2.all, Level3.all]

      string:
        file: Python/Level1/string.py
        desc: "字符串操作、格式化、分割、正则、编解码"
        hex_count: 29
        sections:
          - 基础字符串
          - f-string格式化
          - 分割与合并
          - 字符串替换
          - 字符串查找
          - 正则
          - 字符串转列表
          - 多行字符串
          - 编解码
        depends_on: []
        imported_by: [Level2.all, Level3.all]

      OS:
        file: Python/Level1/OS.py
        desc: "文件读写、路径处理、环境变量、JSON序列化"
        hex_count: 24
        sections:
          - 读文件
          - 逐行读文件
          - 写文件
          - 追加写入
          - 文件检查
          - 列目录
          - 创建目录
          - 路径处理
          - 环境变量
          - 读JSON
          - 写JSON
        depends_on: []
        imported_by: [Level3.account_management, Level3.api_server]

  Level2:
    desc: "算法层 — 通用算法模式"
    materials:
      bubble_sort:
        file: Python/Level2/bubble_sort.py
        desc: "冒泡排序（原地排序）"
        hex_count: 2
        depends_on: [Level1.control_flow, Level1.data_structure]
        imported_by: []

      binary_search:
        file: Python/Level2/binary_search.py
        desc: "二分查找 + 左边界查找"
        hex_count: 3
        depends_on: [Level1.control_flow]
        imported_by: []

      fibonacci:
        file: Python/Level2/fibonacci.py
        desc: "斐波那契：递归、DP、记忆化、生成器"
        hex_count: 2
        depends_on: [Level1.function]
        imported_by: []

      dfs_bfs:
        file: Python/Level2/dfs_bfs.py
        desc: "DFS递归/迭代、BFS、最短路径"
        hex_count: 3
        depends_on: [Level1.data_structure]
        imported_by: []

      greedy_algorithm:
        file: Python/Level2/greedy_algorithm.py
        desc: "活动选择（区间调度）、零钱兑换"
        hex_count: 13
        depends_on: [Level1.data_structure, Level1.function]
        imported_by: []

      game_of_life:
        file: Python/Level2/game_of_life.py
        desc: "Conway 生命游戏（网格、邻居计算、迭代、渲染）"
        hex_count: 24
        depends_on: [Level1.console, Level1.control_flow]
        imported_by: []

  Level3:
    desc: "业务架构 — 完整业务模块"
    materials:
      account_management:
        file: Python/Level3/account_management.py
        desc: "账户管理系统（注册/登录/更新/删除/列出）"
        hex_count: 30
        depends_on: [Level1.OS, Level1.data_structure]
        cross_references:
          - source_hex: "0xD0E1F2"
            target_file: OS.py
            target_hex: "0xB1C4B3"
            desc: "JSON文件读取"
          - source_hex: "0xD0E1F3"
            target_file: OS.py
            target_hex: "0xB1C4C1"
            desc: "JSON文件写入"
          - source_hex: "0x334455"
            target_file: data_structure.py
            target_hex: "0xD1E3D1"
            desc: "dict存储结构"
        imported_by: []

      actor_system:
        file: Python/Level3/actor_system.py
        desc: "Actor 并发模型（消息队列、Actor注册、广播）"
        hex_count: 24
        depends_on: [Level1.data_structure]
        cross_references:
          - source_hex: "0x112233"
            target_file: data_structure.py
            target_hex: "0xD1E4F1"
            desc: "消息队列deque"
        imported_by: []

      api_server:
        file: Python/Level3/api_server.py
        desc: "REST API 服务器（GET/POST/CRUD）"
        hex_count: 35
        depends_on: [Level1.OS, Level1.data_structure, Level1.string]
        cross_references:
          - source_hex: "0x566778"
            target_file: OS.py
            target_hex: "0xB1C4C3"
            desc: "JSON序列化"
          - source_hex: "0x889900"
            target_file: data_structure.py
            target_hex: "0xD1E3D1"
            desc: "dict数据存储"
        imported_by: []

# ── 多语言素材目录 ──
# hex 编号跨语言通用，不同语言目录下同名文件共享相同的 hex 接口点
# 核糖体根据目标语言选择对应目录下的素材进行拼装
languages:
  Python:
    dir: Python/
    ext: .py
    desc: "Python 3 — 原始语言，完整支持"
    status: complete
  TypeScript:
    dir: TypeScript/
    ext: .ts
    desc: "TypeScript (Node.js) — 按意图翻译，惯用写法"
    status: complete
  Cpp:
    dir: Cpp/
    ext: .cpp
    desc: "C++17 — 按意图翻译，STL 惯用法"
    status: complete

# TypeScript 素材映射（与 Python 一一对应，hex 不变）
TypeScript:
  Level1:
    calculator: { file: TypeScript/Level1/calculator.ts, hex_count: 26 }
    console: { file: TypeScript/Level1/console.ts, hex_count: 26 }
    control_flow: { file: TypeScript/Level1/control_flow.ts, hex_count: 30 }
    function: { file: TypeScript/Level1/function.ts, hex_count: 22 }
    data_structure: { file: TypeScript/Level1/data_structure.ts, hex_count: 41 }
    string: { file: TypeScript/Level1/string.ts, hex_count: 29 }
    OS: { file: TypeScript/Level1/OS.ts, hex_count: 24 }
  Level2:
    bubble_sort: { file: TypeScript/Level2/bubble_sort.ts, hex_count: 2 }
    binary_search: { file: TypeScript/Level2/binary_search.ts, hex_count: 3 }
    fibonacci: { file: TypeScript/Level2/fibonacci.ts, hex_count: 2 }
    dfs_bfs: { file: TypeScript/Level2/dfs_bfs.ts, hex_count: 3 }
    greedy_algorithm: { file: TypeScript/Level2/greedy_algorithm.ts, hex_count: 13 }
    game_of_life: { file: TypeScript/Level2/game_of_life.ts, hex_count: 24 }
  Level3:
    account_management: { file: TypeScript/Level3/account_management.ts, hex_count: 30 }
    actor_system: { file: TypeScript/Level3/actor_system.ts, hex_count: 24 }
    api_server: { file: TypeScript/Level3/api_server.ts, hex_count: 35 }

# C++ 素材映射（与 Python 一一对应，hex 不变）
Cpp:
  Level1:
    calculator: { file: Cpp/Level1/calculator.cpp, hex_count: 26 }
    console: { file: Cpp/Level1/console.cpp, hex_count: 26 }
    control_flow: { file: Cpp/Level1/control_flow.cpp, hex_count: 30 }
    function: { file: Cpp/Level1/function.cpp, hex_count: 22 }
    data_structure: { file: Cpp/Level1/data_structure.cpp, hex_count: 41 }
    string: { file: Cpp/Level1/string.cpp, hex_count: 29 }
    OS: { file: Cpp/Level1/OS.cpp, hex_count: 24 }
  Level2:
    bubble_sort: { file: Cpp/Level2/bubble_sort.cpp, hex_count: 2 }
    binary_search: { file: Cpp/Level2/binary_search.cpp, hex_count: 3 }
    fibonacci: { file: Cpp/Level2/fibonacci.cpp, hex_count: 2 }
    dfs_bfs: { file: Cpp/Level2/dfs_bfs.cpp, hex_count: 3 }
    greedy_algorithm: { file: Cpp/Level2/greedy_algorithm.cpp, hex_count: 13 }
    game_of_life: { file: Cpp/Level2/game_of_life.cpp, hex_count: 24 }
  Level3:
    account_management: { file: Cpp/Level3/account_management.cpp, hex_count: 30 }
    actor_system: { file: Cpp/Level3/actor_system.cpp, hex_count: 24 }
    api_server: { file: Cpp/Level3/api_server.cpp, hex_count: 35 }
```
