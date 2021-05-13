# vue-如何解决watch中新值和旧值是一样的问题

最好的解决办法是用 watch 指向监听的基本类型，代码如下

```js
<template>
  <section>
    <input  v-model="obj.a">
  </section>
</template>

<script>
export default {
  data () {
    return {
      obj: {
        a: 1
      }
    }
  },
  watch: {
    'obj.a': { // watch指向监听的基本类型
      handler (newVal, oldVal) {
        console.log('newVal', newVal)
        console.log('oldVal', oldVal)
      },
      deep: true
    }
  }
}
</script>
```

## 原文链接
* [vue中，如何解决watch的新值和旧值是一样的？](https://juejin.cn/post/6898347237173100558)
