# JAVA+POI导出并通过流下载

*注意：下载不能通过AJAX*

这是在SSM框架下写的。

```java
//service层
@Override
public HSSFWorkbook getExl(Map<String, Object> map) {
		
		//创建工作簿
		HSSFWorkbook wb = new HSSFWorkbook();
  		//在工作簿上创建一个sheet页
		HSSFSheet sheet = wb.createSheet();
  		//在sheet页上创建一行
		HSSFRow row = sheet.createRow(0);
  		//在一行上创建3个单元个，作为表头
  		//创建第0个单元格
		HSSFCell c = row.createCell(0);
  		//为第0个表格插入数据
		c.setCellValue("操作事件");
  		//创建第1个单元格
		c= row.createCell(1);
  		//为第1个表格插入数据
		c.setCellValue("操作时间");
  		//创建第2个单元格
		c= row.createCell(2);
 		 //为第2个表格插入数据
		c.setCellValue("操作时长");
  		//从数据库获取数据
		List<ClientOpeLog> lc = clientOpeLogOperation.getAllClientOpeLog(map);
  		//通过循环创建数据
		for (int i = 0; i < lc.size(); i++) {
            //每次增加一行，这里从第1行开始（真实的第一行是第0行，就是我们表头）
			HSSFRow row1 = sheet.createRow(i+1);
          	//创建单元格，并添加数据
			HSSFCell c1 = row1.createCell(0);
			c1.setCellValue(lc.get(i).getEvents());
			c1= row1.createCell(1);
			c1.setCellValue(lc.get(i).getOperateTime());
			c1= row1.createCell(2);
			c1.setCellValue(lc.get(i).getOperateTime());
		}
  		//将工作簿返回
		return wb;
	}
```

```java
//controller层
@RequestMapping("/export")
	public void export(String assetno,String startTime,String endTime,String title,HttpServletResponse response){
      	//查询的参数
		Map<String,Object> map = new HashMap<>();
		map.put("assetno", assetno);
		map.put("startTime", startTime);
		map.put("endTime", endTime);
		
		BufferedOutputStream bos  = null;
		try {
          	//清空response
			 response.reset();
          //将响应流（个人叫法）作为参数放入缓存输入流
			bos = new BufferedOutputStream(response.getOutputStream());
          //设置响应头，告诉浏览器这是下载
			response.setHeader("Content-Type","application/force-download;charset=UTF-8");
			response.setHeader("Content-Type","application/vnd.ms-excel");
			response.setHeader("Content-Disposition","attachment;filename="+URLEncoder.encode(title, "utf-8")+".xls");
			HSSFWorkbook wb = clientOpeLogServcie.getExl(map);
          
			wb.write(bos);
			bos.flush();
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				bos.close();
			} catch (IOException e) {
			}
		}
	}
```

```javascript
//js部分
var assetNo = select.assetNo;
var url = '../log/export?assetno='+assetNo+'&startTime='+startTime+'&endTime='+endTime+'&title='+select.deviceName;
		
location.href = url;
```

