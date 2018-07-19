项目放在这里的根目录

首先引入数据库连接配置文件config创建db(名称取易于理解的).ini
编写读取配置文件的公共模块common
named_tuples.py -- 用于定义必须的名称元组
conf_utils.py -- 用于读取并返回配置文件的信息
mysql_client.py -- 用于数据库连接和操作
csv_utils.py -- 用于将数据处理结果写入CSV文件
compress_utils.py -- 用于压缩CSV文件
email_utils.py -- 用于邮件发送