本例介绍如何在spring+mybatis框架中实现mysql的主从分离技术
假设主服务ip为139.199.117.182:3306 从服务器ip为111.231.62.99:3306 系统均为centos
step1配置主数据库139.199.117.182:3306
     a.修改主数据库配置文件 vi /etc/my.cnf
     b.在[mysqld]字段加入 如下配置:
                                  server-id=1 #这里要和从服务id不同
                                  log-bin=master-bin #开启bin-log，并指定文件目录和文件名前缀
                                  log-bin-index=master-bin.index
                                  binlog-do-db=petmaker #需要同步的数据库
                                  binlog-ignore-db=mysql #忽略同步mysql数据库
                                  sync_binlog=1 #确保binlog日志写入后与硬盘同步 
                                  skip-slave-start #让slave不随mysql自动启动
                                  binlog_checksum = none  ＃跳过现有的采用checksum的事件，mysql5.6.5以后的版本中				 binlog_checksum=crc32,而低版本都是binlog_checksum=none
                                  binlog_format = mixed   ＃bin-log日志文件格式，设置为MIXED可以防止主键重复。
     c.配置完成后，重启mysql service mysqld restart
     d.通过Navicat 结构同步操作，将主服务结构复制给从服务 #也可通过dump命令复制表 这里就不一一赘述
     e.mysql -uroot -p123456;#登陆主服务器上mysql 
     f.grant replication slave,replication client on *.* to root@'111.231.62.99' identified by "123456";#在master上设置数据同步权限
       Query OK, 0 rows affected (0.02 sec)                                    #若要所有网段则设置root@'%' ；
       mysql> flush privileges;
       Query OK, 0 rows affected (0.00 sec)
     g.show grants for root@'111.231.62.99';
       mysql> show master status;
              +------------------+----------+--------------+------------------+-------------------+
              | File       | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
              +------------------+----------+--------------+------------------+-------------------+
              | master-bin.000007 | 120    |  petmaker   |     mysql   |          |
              +------------------+----------+--------------+------------------+-------------------+
              1 row in set (0.00 sec)
 至此主服务器配置完成


step2 配置从服务器111.231.62.99:3306
      a.修改从服务器配置文件 vi etc/my.cnf
      b.在[mysqld]字段加入 如下配置:
                                   server-id=2 #这里和主服务id不同
                                   relay-log-index=slave-relay-bin.index
                                   relay-log=slave-relay-bin
                                   log-bin=slave-bin #启动MySQ二进制日志系统
                                   replicate-do-db=petMaker #需要同步的数据库名。如果不指明同步哪些库，就去掉这行，表示所有库的同步（除了ignore忽略的库）。
                                   replicate-ignore-db=mysql #不同步mysql数据库
                                   replicate-rewrite-db=petmaker->petMaker #我这里2个服务器上的数据库名不同。所以配置了一下，相同可以跳过
                                   slave-skip-errors=all #跳过所有的错误，继续执行复制操作
      c.mysql -uroot -p123456 登陆从数据库
      d.mysql>stop slave; #执行同步前 先关闭同步
      e.mysql>change master to master_host='139.199.117.182',master_user='root',master_password='123456',master_log_file='master-bin.000007',master_log_pos=120;
        这里需要注意的是master_user 和password 指的都是step1>f步骤中grant的user和password 而不是自己的用户名密码
      f.mysql>start slave;启动同步
      g.mysql> show slave status \G;
      *************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 139.199.117.182
                  Master_User: root
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: master-bin.000005
          Read_Master_Log_Pos: 4713
               Relay_Log_File: slave-relay-bin.000002
                Relay_Log_Pos: 3752
        Relay_Master_Log_File: master-bin.000005
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: petMaker
          Replicate_Ignore_DB: mysql
  ......
1 row in set (0.00 sec)
如上，当IO和SQL线程的状态均为Yes，则表示主从已实现同步了！这里mysql的配置已经完成

step3  我们开始配置框架
a.  mybatis-spring.xml

```
   <!-- 数据源配置, 使用 Druid 数据库连接池 -->
	 <bean name="baseDataSource" class="com.alibaba.druid.pool.DruidDataSource" >
	   <property name="driverClassName" value="${jdbc.driver}" />
	  	<property name="initialSize" value="${dbcp.initialSize}" />
        <property name="minIdle" value="${dbcp.minIdle}" />
        <property name="maxActive" value="${dbcp.maxActive}" />
        <!-- 配置获取连接等待超时的时间 -->
        <property name="maxWait" value="${dbcp.maxWait}" />
        <!-- 这里建议配置为TRUE，防止取到的连接不可用。获取链接的时候，不校验是否可用，开启会有损性能--> 
        <property name="testOnBorrow" value="${dbcp.testOnBorrow}" />
        <!-- 归还链接到连接池的时候校验链接是否可用 -->
        <property name="testOnReturn" value="${dbcp.testOnReturn}" />
        <!-- 此项配置为true即可，不影响性能，并且保证安全性。意义为：申请连接的时候检测，如果空闲时间大于timeBetweenEvictionRunsMillis，执行validationQuery检测连接是否有效 -->
        <property name="testWhileIdle" value="${dbcp.testWhileIdle}" />
        <!-- 配置间隔多久才进行一次检测，检测需要关闭的空闲连接，单位毫秒 -->
        <property name="timeBetweenEvictionRunsMillis" value="${dbcp.timeBetweenEvictionRunsMillis}" />
        <!-- 配置一个连接在池中最小生存的时间，单位毫秒 -->
        <property name="minEvictableIdleTimeMillis" value="${dbcp.minEvictableIdleTimeMillis}" />
        <!-- 链接使用超过时间限制是否回收 -->
        <property name="removeAbandoned" value="${dbcp.removeAbandoned}" />
        <!-- 超过时间限制时间（单位秒），目前为5分钟，如果有业务处理时间超过5分钟，可以适当调整。 -->
        <property name="removeAbandonedTimeout" value="${dbcp.removeAbandonedTimeout}" />
        <!-- #链接回收的时候控制台打印信息，测试环境可以加上true，线上环境false。会影响性能。 -->
        <property name="logAbandoned" value="${dbcp.logAbandoned}" />
        <!-- 验证连接有效与否的SQL，不同的数据配置不同 --> 
         <property name="validationQuery" value="${dbcp.validationQuery}" />
         <!-- 配置监控统计拦截的filters，用于在界面中统计sql和开启druid防火墙。注意： -->
        <!-- 监控中有jdbcSqlStat，原因是：com.alibaba.druid.statJdbcDataSourceStat中的createSqlStat方法中，
            用了一个map来存放所有的sql语句，这样会导致线上触发FullGC，可将此处注释掉 -->
        <property name="filters" value="wall,stat" />
        <!-- 映射慢sql -->
         <property name="proxyFilters">
            <list>
                <ref bean="statfilter"/>
                <ref bean="logFilter"/>
            </list>
        </property>
	</bean>
  <!--主数据库-->
    <bean name="masterDataSource" parent="baseDataSource" init-method="init" destroy-method="close">
        <property name="url" value="${master.jdbc.url}" />
        <property name="username" value="${master.jdbc.user}" />
        <property name="password" value="${master.jdbc.password}" />
    </bean> 
    <!--从数据库-->
     <bean name="slaveDataSource" parent="baseDataSource" init-method="init" destroy-method="close">
        <property name="url" value="${slave.jdbc.url}" />
        <property name="username" value="${slave.jdbc.user}" />
        <property name="password" value="${slave.jdbc.password}" />
    </bean> 
    
```


     <!-- 动态数据源，根据service接口上的注解来决定取哪个数据源 -->
    <bean id="dataSource" class="com.luke.util.DynamicDataSource">  
        <property name="targetDataSources">      
          <map key-type="java.lang.String">      
              <!-- write or slave -->    
             <entry key="slave" value-ref="slaveDataSource"/>      
             <!-- read or master   -->  
             <entry key="master" value-ref="masterDataSource"/>      
          </map>               
        </property>   
        <property name="defaultTargetDataSource" ref="masterDataSource"/>      
    </bean>
    <!-- 慢SQL记录  -->
    <bean id="statfilter" class="com.alibaba.druid.filter.stat.StatFilter">
        <!-- 开启合并sql -->
        <property name="mergeSql" value="true" />
        <!-- 开启慢查询语句,200毫秒 -->
        <property name="slowSqlMillis" value="1000" />
        <property name="logSlowSql" value="true" />
    </bean>
    
    <bean id="logFilter" class="com.alibaba.druid.filter.logging.Log4jFilter">
        <property name="resultSetLogEnabled" value="false" />
        <property name="statementExecutableSqlLogEnable" value="true" />
    </bean>
    
    <!-- mybatis -->
    <bean id="sqlsessionfactory" class="org.mybatis.spring.SqlSessionFactoryBean">
    	<property name="dataSource" ref="dataSource"></property>
      <property name="configLocation" value="classpath:spring-mybatis.xml"></property>
    	<property name="mapperLocations" value="classpath:com/luke/xml/*.xml"></property> 
    </bean>
    <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    	<!--注意不要用ref  -->
    	<property name="sqlSessionFactoryBeanName" value="sqlsessionfactory"></property>
    	<property name="basePackage" value="com.luke.dao"></property>
    </bean>
    <!-- 事务管理-->
     <bean id="transactionManager"  
        class="org.springframework.jdbc.datasource.DataSourceTransactionManager">  
        <property name="dataSource" ref="dataSource" />  
    </bean> 
     <tx:annotation-driven transaction-manager="transactionManager" proxy-target-class="true" order="1"/>
     <!-- 为业务逻辑层的方法解析@DataSource注解  为当前线程的HandleDataSource注入数据源 -->    
    <bean id="dataSourceAspect" class="com.luke.util.DataSourceAspect" />    
    <aop:config proxy-target-class="true">    
        <aop:aspect id="dataSourceAspect" ref="dataSourceAspect" order="2">    
            <aop:pointcut id="tx" expression="execution(* com.luke.service.impl..*.*(..)) "/>    
            <aop:before pointcut-ref="tx" method="before" />                
        </aop:aspect>    
    </aop:config>

b.AOP实现数据源的动态切换 DataSource.java

```
package com.luke.util;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**  

- RUNTIME  
- 编译器将把注释记录在类文件中，在运行时 VM 将保留注释，因此可以反射性地读取。  
- */  
  @Retention(RetentionPolicy.RUNTIME)  
  @Target(ElementType.METHOD) 
  public @interface DataSource
  {
	String value();
  }
```

c.DataSourceAspect.java

```
package com.luke.util;

import java.lang.reflect.Method;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.reflect.MethodSignature;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DataSourceAspect
{
	 protected static final Logger logger = LoggerFactory.getLogger(DataSourceAspect.class);
    /**
     * 在dao层方法获取datasource对象之前，在切面中指定当前线程数据源
     */
    public void before(JoinPoint point)
    {

        Object target = point.getTarget();
        String method = point.getSignature().getName();
        Class<?>[] classz = target.getClass().getInterfaces();                        // 获取目标类的接口， 所以@DataSource需要写在接口上
        Class<?>[] parameterTypes = ((MethodSignature) point.getSignature())
                .getMethod().getParameterTypes();
        try
        {
            Method m = classz[0].getMethod(method, parameterTypes);
            if (m != null && m.isAnnotationPresent(DataSource.class))
            {
                DataSource data = m.getAnnotation(DataSource.class);
                logger.info("用户选择数据库库类型：" + data.value());
                HandleDataSource.putDataSource(data.value());                        // 数据源放到当前线程中
            }

        } catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    }
```

d.DynamicDataSource.java

```
package com.luke.util;

import org.springframework.jdbc.datasource.lookup.AbstractRoutingDataSource;

public class DynamicDataSource extends AbstractRoutingDataSource
{

/**

- 获取与数据源相关的key 此key是Map<String,DataSource> resolvedDataSources 中与数据源绑定的key值
- 在通过determineTargetDataSource获取目标数据源时使用
  */
  @Override
  protected Object determineCurrentLookupKey()
  {
  return HandleDataSource.getDataSource();
  }

}
```

e.HandleDataSource.java

```
package com.luke.util;

public class HandleDataSource
{
    public static final ThreadLocal<String> holder = new ThreadLocal<String>();

/**

- 绑定当前线程数据源
- 
- @param key
  */
  public static void putDataSource(String datasource)
  {
  holder.set(datasource);
  }

/**

- 获取当前线程的数据源
- 
- @return
  */
  public static String getDataSource()
  {
  return holder.get();
  }

}
```

f.service接口上应用@DataSource实现数据源的指定

```
package com.luke.service;

import java.util.List;

import com.luke.model.UserDoctorInfo;
import com.luke.util.DataSource;
import com.luke.util.ResultBean;
public interface IDoctorService {
	 @DataSource("slave")
	List<UserDoctorInfo> queryDocInfo(String docType);
	 @DataSource("master")
	ResultBean likeDoc(String userDtcId);
	 @DataSource("master")
	ResultBean insertRecord(String userDtcId, String userUnionId);

}

```

至此，所有配置完成。

参考：https://www.cnblogs.com/lidj/p/7337535.html

​	   https://blog.csdn.net/yoon0205/article/details/50605540

​	   https://www.cnblogs.com/wade-lt/p/9008058.html