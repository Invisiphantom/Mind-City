## 项目创建
```bash
npm create vue@latest
cd vue-project
npm install
npm install vue-router
npm run dev
```

## Vue语法

| Grammar               | Description    |
| --------------------- | -------------- |
| import xxx from 'xxx' | 导入模块       |
| export default {}     | 导出模块       |
| ref()                 | 创建响应式数据 |
| reactive()            | 创建响应式对象 |
| computed()            | 创建计算属性   |
| watch()               | 显示创建监听器 |
| watchEffect()         | 隐式创建监听器 |
| onMounted()           | 生命周期钩子   |
| defineProps()         | 接受props      |
| v-for                 | 循环渲染       |
| v-model               | 双向绑定       |




## 项目实例

文件结构
```bash
src
├── components
    └── Person.vue
    └── Game.vue
    └── Name.vue
├── App.vue
└── main.ts
```

main.ts
```ts
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

App.vue
```vue
<template>
    <div>
        <button @click="test">测试</button>
        <Person ref="personRef" />
        <Game />
        <Name />
    </div>
</template>


<script>
import Person from "./components/Person.vue";
import Game from "./components/Game.vue";
import Name from "./components/Name.vue";

export default {
    name: "App",
    components: {
        Person,
        Game,
        Name,
    }
};
</script>

<script setup>
import Person from "./components/Person.vue";
import { ref } from "vue";

let personRef = ref();
function test() {
    console.log(personRef.value.name);
    console.log(personRef.value.age);
}

</script>
```


Person.vue
```vue
<template>
    <div class="person">
        <h1> Person </h1>
        <h2>姓名: {{ name }}</h2>
        <h2>年龄: {{ age }}</h2>
        <h2>地址: {{ address }}</h2>
        <button @click="changeName">修改名字</button>
        <button @click="changeAge">修改年龄</button>
        <button @click="showTel">查看联系方式</button>
    </div>
</template>

<script>
export default {
    name: "Person"
};
</script>

<script setup>
import { ref, watch, defineExpose } from 'vue';

let name = ref("张三");
let age = ref(18);
let tel = 13859431111;
let address = "China";


function changeName() {
    name.value = '李四';
}
function changeAge() {
    age.value += 1;
}
function showTel() {
    alert(tel);
}

const stopWatch = watch(age, (newVal, oldVal) => {
    console.log(`年龄从${oldVal}变为${newVal}`);
    if (newVal > 30) {
        alert("年龄已经超过30岁");
        stopWatch();
    }
});

defineExpose({
    name,
    age
});
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

Game.vue
```vue
<template>
    <div class="game">
        <button @click="addGame">添加游戏</button>
        <ul>
            <li v-for="game in games" :key="game.id" ref="gameRefs">{{ game.name }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "Game"
};
</script>

<script setup>
import { ref, onMounted } from "vue";

let games = ref([
    { id: "game_01", name: "King" },
    { id: "game_02", name: "Yuan" },
    { id: "game_03", name: "Horizon" }
]);

function addGame() {
    games.value.push({ id: "game_04", name: "GTA" });
}

const gameRefs = ref([]);
onMounted(() => {
    console.log(gameRefs.value);
});
</script>

<style scoped>
.game {
    background-color: skyblue;
    box-shadow: 0 0 10px;
    border-radius: 10px;
    margin: 20px;
    border: none;
    padding: 20px;
    font-size: 20px;
    font-weight: bold;
}
</style>
```

Name.vue
```vue
<template>
    <div class="name">
        <div class="input-line">
            姓: <input type="text" v-model="firstName">
        </div>
        <div class="input-line">
            名: <input type="text" v-model="lastName">
        </div>
        <div class="input-line">
            全名: <span>{{ fullName }}</span>
        </div>
    </div>
</template>

<script>
export default {
    name: "Name"
};
</script>

<script setup>
import { ref, computed } from 'vue';

let firstName = ref("Zhang");
let lastName = ref("San");

let fullName = computed(() => {
    return firstName.value + "-" + lastName.value;
});
</script>

<style scoped>
.name {
    background-color: skyblue;
    box-shadow: 0 0 10px;
    border-radius: 10px;
    margin: 20px;
    border: none;
    padding: 20px;
    font-size: 18px;
    font-weight: bold;
}

.input-line {
    display: block;
    margin: 10px 0;
}

input {
    height: 25px;
    border-radius: 3px;
    border: 1px;
    margin-left: 10px;
    font-size: large;
}

span {
    margin-left: 10px;
}
</style>
```