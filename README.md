ideploy
=======
## Usage
### PreBuild tools
#### idepoly.py
>用于build前 替换一些文件和字段

##### 应用场景
* 多渠道build
* 不同包显示不同的icon或者splash
	
##### 配置文件 ci.yml
	replace_from_pics:
	需要替换的文件路径集合  
	replace_to_pics:
	需要被替换的文件路径集合
	
	template_source_files:
	需要替换的文本文件路径集合，需要被替换的内容使用 {{replace_content}}表示，例如 {{id}}
	template_target_files:
	需要被替换的文本文件路径集合 
	定义一个replace_content,例如 replace_content: Hello Yaml
##### 运行
	python idepoly.py (默认加载ci.yml)
	python idepoly.py xx.yml (自定义的yml,格式参考ci.yml)
	
### AfterBuild tools
#### firupload.py
>用于打包完后上传到 [fir](http://fir.im>)

##### 应用场景
	打包好的x.ipa 或者 xx.apk 需要给QA进行测试，可以通过fir进行分发
##### Install
	 sudo easy_install clint
	 sudo easy_install requests
	 sudo easy_install requests_toolbelt
	 
##### config.yml
	appid: 应用id (android: applicationId, ios:bundleId)
	token: fir 提供的 token
	filepath: xx.ipa/xx.apk 的路径
	type: ios/android
	
##### 运行
	python firupload.py

#### pgupload.py
>用于打包完后上传到 [pgyer](http://pgyer.com>)

##### 应用场景
	打包好的x.ipa 或者 xx.apk 需要给QA进行测试，可以通过pgyer进行分发
##### Install
	 sudo easy_install clint
	 sudo easy_install requests
	 sudo easy_install requests_toolbelt

##### pgconfig.yml


##### 运行
	python pgupload.py


blog: [beiliubei](http://www.cnblogs.com/beiliubei/)