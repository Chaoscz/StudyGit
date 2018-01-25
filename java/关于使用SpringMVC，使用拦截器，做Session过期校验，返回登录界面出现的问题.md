# 关于使用SpringMVC，使用拦截器，做Session过期校验，返回登录界面出现的问题

1.使用了iframe，在ifame中出现登录界面

解决方法

```javascript
<script language="javascript"> 
if(top.location!==self.location){ 
WarningTxt1 = "content页面被iframe了！"; 
WarningTxt2 = "我们跳出iframe，直接访问content页面吧！"; 
alert(WarningTxt1); 
alert(WarningTxt2); 
top.location.href=self.location.href; 
} 
</script> 
```

