# golang-心跳机制实现示例

## 关键代码
```go
//服务端​
//全局变量
var ids = make(map[string]chan byte)
​
func ResponseHeartBeat(id string) {
    if _, ok := ids[id]; ok {
        //保活心跳请求
        ids[id] <- 0
    } else {
        //上线触发器
        ids[id] = make(chan byte)
        go HeartBeat(ids, id, 10)
  }
}
​
/**
 *@brief: 心跳事件触发器
 *@param: ids 全局注册表
 *@param: id
 *@param: 超时时间
 */
func HeartBeat(ids map[string]chan byte, id string, n int64) {
  online := true
    for online {
    select {
        case  <- ids[id]:
          //保活触发器
        case <- time.After(time.Duration(n) * time.Second):
          //下线触发器
          online = false
          delete(ids, id)
          //下线触发通知系列功能操作，可采用观察者模式
    }
  }
}
```

## 原文链接
* [Golang心跳机制实现示例](https://blog.csdn.net/cugriver/article/details/100751238)
