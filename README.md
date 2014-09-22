ideploy
=======

## Usage
### ci.yml
	replace_from_pics:
	需要替换的文件路径集合  
	replace_to_pics:
	需要被替换的文件路径集合
	
	template_source_files:
	需要替换的文本文件路径集合，需要被替换的内容使用 {{replace_content}}表示，例如 {{id}}
	template_target_files:
	需要被替换的文本文件路径集合 
	定义一个replace_content,例如 replace_content: Hello Yaml
	
	
## Example
### ci.yml
	replace_from_pics:
  	- from/a.txt

	replace_to_pics:
  	- to/a.txt


	template_source_files:
  	- template/template-a.txt

	template_target_files:
  	- template/a.txt

	id: helloworld
	xx: Helloworld xx
### In: template/template-a.txt
	id1
	{{id}}
	id2
	{{id}}
	xx
	{{xx}}
	
### Out: template/a.txt
	id1
	helloworld
	id2
	helloworld
	xx
	helloworld xx