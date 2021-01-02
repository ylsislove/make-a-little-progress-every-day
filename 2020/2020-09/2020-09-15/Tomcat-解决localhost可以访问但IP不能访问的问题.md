# Tomcat-解决localhost可以访问但IP不能访问的问题

本人用的是 Win10，tomcat8.5，解决办法亲测有效。

## localhost 不能访问的解决办法
1. 在 conf/server.xml 中找到

    ```xml
    <Engine defaultHost="localhost" name="Catalina">
    ```

    确认 defaultHost 是不是 localhost

2. 在 conf/server.xml 中找到

    ```xml
    <Host appBase="webapps" autoDeploy="true" name="localhost" unpackWARs="true">
    ```

    确认 name 属性值是不是 localhost

## IP 不能访问的解决办法

我看网上有点人说什么 Win7啊，电脑防火墙啊，杀毒软件之类的问题。我想，现在绝大多数人应该都用的是 Win10 吧，而搞程序的应该也不会用市面上的那种坑爹的杀毒软件，所以我上面说的这些问题，电脑防火墙啊，杀毒软件之类，一般人也都不是这方面的问题。那 Tomcat 的 localhost 能访问，但 IP 不能访问的真正的解决办法是什么呢，往下看~~

1. 打开命令符窗口【cmd+R】输入：ping localhost 如果是::1 ，则 tomcat 是用的 ipv6

2. 将 tomcat 绑定成 ipv4 的方法是：找到

    ```xml
    <Connector URIEncoding="UTF-8" connectionTimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443" />
    ```

    在里面添加属性：address="0.0.0.0"。重启，搞定，在浏览器输入本机IP地址也可以直接访问。