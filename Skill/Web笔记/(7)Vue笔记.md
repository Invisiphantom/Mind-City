## 项目创建
```bash
npm create vue@latest
cd vue-project
npm install
npm run dev

src
├── components
├── App.vue
└── main.ts
```

```ts
// main.ts
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```


## Vue语法




ref响应式
reactive响应式
```vue
<template>
    <div class="person">
        <h2>姓名: {{ name }}</h2>
        <h2>年龄: {{ age }}</h2>
        <h2>地址: {{ address }}</h2>
        <button @click="changeName">修改名字</button>
        <button @click="changeAge">修改年龄</button>
        <button @click="showTel">查看联系方式</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'

let name = ref("张三")
let age = ref(18)
let tel = 13859431111
let address = "复旦南区"

function changeName() {
    name.value = '李四'
}
function changeAge() {
    age.value += 1
}
function showTel() {
    alert(tel)
}
</script>

<style scoped>
.person {
    background-color: skyblue;
    box-shadow: 0 0 10px;
    border-radius: 10px;
    margin: 20px;
    border: none;
    padding: 20px;
}
button {
    font-family: 'Microsoft YaHei';
    margin: 0 5px;
}
</style>
```

v-for 循环遍历
v-bind 单向绑定
v-model 双向绑定