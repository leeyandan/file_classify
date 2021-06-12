# 文件分类脚本

## 一、命令行调用

```shell
python classify_by_date_type.py -i I:\DCIM\101MEDIA -o H:\航拍素材 -g 2021-06-05

python classify_by_date_type.py -i I:\DCIM\100MEDIA -o H:\航拍素材\test -g 2021-06
```

* 解释：
	* -i 输入文件夹路径，默认当前文件夹
	* -o 输出文件路径，默认当前文件夹
	* -g 日期（例如2021-06-12）只读取该日期之后的文件，不指定的话就读取所有的文件

## 二、待开发支持的功能
目前是按修改日期-文件类型进行分类
1. 支持自定义输出文件夹的层次，
	- a. 类型分类
	- b. 日期分类 
	- c. 日期-类型分类 
	- d. 类型-日期分类
	- t for type , d for date 。
	- -c td表示先后顺序 
2. 支持将多个文件夹的文件汇总，然后再分类整理
