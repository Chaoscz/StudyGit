1.创建一个WebSocket配置类（这里也可以用配置文件来实现其实），实现接口来配置Websocket请求的路径和拦截器。

```java
package com.guoguang.websocket;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.WebSocketHandler;
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer  {

	@Override
	public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
		 registry.addHandler(myHandler(), "/myHandler").addInterceptors(new WebSocketInterceptor());
	}
	
	@Bean
    public WebSocketHandler myHandler() {
        return new MyHandler();
    }

}

```

2.拦截器主要是用于用户登录标识（userId）的记录，便于后面获取指定用户的会话标识并向指定用户发送消息，在下面的拦截器中，我在session中获取会话标识（这个标识是在登录时setAttribute进去的，后面代码会说到），你也可以通过H5在`new WebSocket(url)`中，在url传入标识参数，然后通过`serverHttpRequest.getServletRequest().getParameterMap()`来获取标识信息。

```java
package com.guoguang.websocket;

import java.util.Map;

import javax.servlet.http.HttpSession;

import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import org.springframework.http.server.ServletServerHttpRequest;
import org.springframework.web.socket.WebSocketHandler;
import org.springframework.web.socket.server.HandshakeInterceptor;

public class WebSocketInterceptor implements HandshakeInterceptor {

    @Override
    public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler handler, Map<String, Object> map) throws Exception {
        if (request instanceof ServletServerHttpRequest) {
            ServletServerHttpRequest serverHttpRequest = (ServletServerHttpRequest) request;
            HttpSession session = serverHttpRequest.getServletRequest().getSession();
            if (session != null) {
                map.put("userId", session.getAttribute("userId"));
            }

        }
        return true;
    }

    @Override
    public void afterHandshake(ServerHttpRequest serverHttpRequest, ServerHttpResponse serverHttpResponse, WebSocketHandler webSocketHandler, Exception e) {

    }
}
```

3.实现Websocket建立连接、发送消息、断开连接等时候的处理类。

注意：普通类无法在使用了@Service的类中来注入，在@Controller可以注入（亲测!!!!）

```java
package com.guoguang.websocket;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.springframework.stereotype.Service;
import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

@Service
public class MyHandler extends TextWebSocketHandler {
    //在线用户列表
    private static final Map<String, WebSocketSession> users;
    //用户标识
    private static final String CLIENT_ID = "userId";

    static {
        users = new HashMap<>();
    }

    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        System.out.println("成功建立连接");
        String userId = getClientId(session);
        System.out.println(userId);
        if (userId != null) {
            users.put(userId, session);
        }
    }

    @Override
    public void handleTextMessage(WebSocketSession session, TextMessage message) {
        System.out.println(message.getPayload());

        WebSocketMessage message1 = new TextMessage("server:"+message);
        try {
            session.sendMessage(message1);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 发送信息给指定用户
     * @param clientId
     * @param message
     * @return
     */
    public boolean sendMessageToUser(String clientId, TextMessage message) {
        if (users.get(clientId) == null) return false;
        WebSocketSession session = users.get(clientId);
        System.out.println("sendMessage:" + session);
        if (!session.isOpen()) return false;
        try {
            session.sendMessage(message);
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    /**
     * 广播信息
     * @param message
     * @return
     */
    public boolean sendMessageToAllUsers(TextMessage message) {
        boolean allSendSuccess = true;
        Set<String> clientIds = users.keySet();
        WebSocketSession session = null;
        for (String clientId : clientIds) {
            try {
                session = users.get(clientId);
                if (session.isOpen()) {
                    session.sendMessage(message);
                }
            } catch (IOException e) {
                e.printStackTrace();
                allSendSuccess = false;
            }
        }

        return  allSendSuccess;
    }


    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) throws Exception {
        if (session.isOpen()) {
            session.close();
        }
        System.out.println("连接出错");
        users.remove(getClientId(session));
    }

    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        System.out.println("连接已关闭：" + status);
        users.remove(getClientId(session));
    }

    @Override
    public boolean supportsPartialMessages() {
        return false;
    }

    /**
     * 获取用户标识
     * @param session
     * @return
     */
    private String getClientId(WebSocketSession session) {
        try {
        	String clientId = (String) session.getAttributes().get(CLIENT_ID);
            return clientId;
        } catch (Exception e) {
            return null;
        }
    }
}
```

a.在`afterConnectionEstablished`连接建立成功之后，记录用户的连接标识，便于后面发信息，这里我是记录将id记录在Map集合中。

b.在`handleTextMessage`中可以对H5 Websocket的send方法进行处理

c.`sendMessageToUser`向指定用户发送消息，传入用户标识和消息体

d.`sendMessageToAllUsers`向左右用户广播消息，只需要传入消息体

e.`handleTransportError`连接出错处理，主要是关闭出错会话的连接，和删除在Map集合中的记录

f.`afterConnectionClosed`连接已关闭，移除在Map集合中的记录。

g.`getClientId`我自己封装的一个方法，方便获取用户标识



JS部分

```javascript
 <script type="text/javascript" >
    $(function(){
    	var theme = "${user.theme}";
        replaceAll(theme);
        var websocket;
        
        function connectWebSocket(){
        	if ('WebSocket' in window) {
                console.log('WebSocket');
                websocket = new WebSocket("ws://"+window.location.host+"/ibms/myHandler"); 
            } 
        	
            websocket.onopen = function (evnt) {
                console.log("链接服务器成功!");
            };
            websocket.onmessage = function (evnt) {
            	var nowNum = $("#messagenum").html();
            	if(nowNum==""){
            		nowNum=0;
            	}
            	nowNum = parseInt(nowNum) +1 ;
            	$("#messagenum").html(nowNum);
            	$("#message1").html(nowNum);
            	$.messager.show({
					timeout :5000,
					title :'提示信息',
					msg :event.data
				});
               
            };
            websocket.onerror = function (evnt) {
            	console.log("服务器链接错误:"+event.data);
            };
            websocket.onclose = function (evnt) {
                console.log("与服务器断开了链接!");
                setTimeout(function(){
                	connectWebSocket();
                },5000);
            }
        }
        connectWebSocket();
        
    });
    

    </script>
```

