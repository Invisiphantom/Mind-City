文档需要包含：需求分析、概要设计、详细设计、部署方法4个部分。
1. 需求分析：回答系统是干什么的。
2. 概要设计：简要回答系统有哪些功能。
3. 详细设计：描述系统核心模块的具体实现（如，数据库表、字段的作用，核心功能的实现方法、流程）。
4. 部署方法：回答第三方如何将该系统（在不需要作者本人指导的情况下）运行起来。


# 需求分析


电商平台是用来进行电子商务交易的网上平台。
它提供了一个在线市场，让买家可以浏览和购买各种商品或服务，同时让卖家可以在平台上展示和销售他们的产品或服务。
电商平台通常提供了购物车、支付处理、订单跟踪、客户服务等功能，以促进交易的顺利进行。
通过电商平台，消费者可以随时随地通过互联网购买所需的商品或服务，而卖家也能够拓展销售渠道，触及更广泛的客户群体。

# 概要设计

电商平台主要包括以下功能：
1. 账户登录
2. token验证
3. 商城主页
4. 一级目录分类页面
5. 二级目录分类页面
6. 商品详情页面
7. 购物车页面
8. 订单生成页面
9. 商品支付界面
10. 支付宝沙箱支付环境
11. 结算界面

# 详细设计


## 长页面顶吸导航交互

https://www.vueusejs.com/core/useScroll/

核心逻辑：根据滚动距离判断当前show类名是否显示
大于78显示，小于78，不显示

```vue
<script setup>
import { useScroll } from '@vueuse/core'
const { y } = useScroll(window)
</script>

<template>
  <div class="app-header-sticky" :class="{show:y>78}">
    <div class="container">
      <RouterLink class="logo" to="/" />
      <!-- 导航区域 -->
      <ul class="app-header-nav">
        <li class="home">
          <RouterLink to="/">首页{{y}}</RouterLink>
        </li>
         ...
</template>
```


自定义图片懒加载指令

https://www.vueusejs.com/core/useIntersectionObserver/

核心逻辑：只有图片进入视口时，才加载图片

```js
import { useIntersectionObserver } from '@vueuse/core'

export const lazyPlugin = {
  install(app) {
    app.directive('img-lazy', {
      mounted(el, binding) {
        const { stop } = useIntersectionObserver(el,
          ([{ isIntersecting }]) => {
            if (isIntersecting) {
              el.src = binding.value
              stop()
            }
          },
        )
      }
    })
  }
}
```


商品列表无限加载

https://www.vueusejs.com/core/useInfiniteScroll/

核心逻辑: 当滚动到底部时，加载下一页数据

```js
// 列表无限加载
const disabled = ref(false)
const load = async () => {
  // 获取下一页的数据
  reqData.value.page++
  const res = await getSubCategoryAPI(reqData.value)
  //新加载的数据与老数据进行拼接合并
  goodList.value = [...goodList.value, ...res.result.items]
  // 加载完毕 停止监听
  if (res.result.items.length === 0) {
    disabled.value = true
  }
}
```

```html
<div class="body" v-infinite-scroll="load" :infinite-scroll-disabled="disabled">
  <GoodsItem v-for="good in goodList" :good="good" :key="good.id"></GoodsItem>
</div>
```

商品详情页图片细节预览

https://www.vueusejs.com/core/useMouseInElement/

核心逻辑: 鼠标移入图片区域时，显示放大镜效果

```js
// 2. 获取鼠标相对位置
const target = ref(null)
const { elementX, elementY, isOutside } = useMouseInElement(target)
// 3. 控制滑块跟随鼠标移动（监听elementX/Y变化，一旦变化 重新设置left/top）
const left = ref(0)
const top = ref(0)
const positionX = ref(0)
const positionY = ref(0)
watch([elementX, elementY, isOutside], () => {

  // 如果鼠标没有移入到盒子里面 直接不执行后面的逻辑
  if (isOutside.value) return

  // 有效范围内控制滑块距离
  // 横向
  if (elementX.value > 100 && elementX.value < 300) {
    left.value = elementX.value - 100
  }
  // 纵向
  if (elementY.value > 100 && elementY.value < 300) {
    top.value = elementY.value - 100
  }

  // 处理边界
  if (elementX.value > 300) { left.value = 200 }
  if (elementX.value < 100) { left.value = 0 }

  if (elementY.value > 300) { top.value = 200 }
  if (elementY.value < 100) { top.value = 0 }

  // 控制大图的显示
  positionX.value = -left.value * 2
  positionY.value = -top.value * 2
})
```

登录界面自定义规则校验

```js
const rules = {
  account: [
    { required: true, message: '用户名不能为空', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '密码不能为空', trigger: 'blur' },
    { min: 6, max: 14, message: '密码长度要求6-14个字符', trigger: 'blur' }
  ],
  agree: [
    {
      validator(rule, value, callback) {
        if (value) callback()
        else callback(new Error('请勾选协议'))
      }
    }
  ]
}
```

```html
<div class="account-box">
  <div class="form">
    <el-form ref="formRef" :model="form" :rules="rules" label-position="right" label-width="60px" status-icon>
      <el-form-item label="账户" prop="account">
        <el-input v-model="form.account" />
      </el-form-item>
      <el-form-item prop="password" label="密码">
        <el-input v-model="form.password" show-password />
      </el-form-item>
      <el-form-item prop="agree" label-width="22px">
        <el-checkbox v-model="form.agree" size="large">
          我已同意隐私条款和服务条款
        </el-checkbox>
      </el-form-item>
      <el-button size="large" class="subBtn" @click="doLogin">点击登录</el-button>
    </el-form>
  </div>
</div>
```

登录合并购物车

核心逻辑: 合并未登录状态下的购物车数据到登录状态下

```js
export const useUserStore = defineStore('user', () => {

  // 1. 定义管理用户数据的state
  const userInfo = ref({})
  const cartStore = useCartStore()

  // 2. 定义获取接口数据的action函数
  const getUserInfo = async (user) => {
    const res = await loginAPI(user)
    userInfo.value = res.result
    // 将未登录状态下的购物车列表合并到登录状态下
    await mergeCartAPI(cartStore.cartList.map(item => {
      return {
        skuId: item.skuId,
        selected: item.selected,
        count: item.count
      }
    }))
    // 更新购物车列表
    cartStore.updateLoginCartList()
  }

  // 退出时清除用户信息
  const clearUserInfo = () => {
    userInfo.value = {}
    cartStore.clearCart()
  }

  return {
    userInfo,
    getUserInfo,
    clearUserInfo,
  }
}, { persist: true })
```

调用支付宝沙箱环境

```js
// 支付地址
const baseURL = 'http://pcapi-xiaotuxian-front-devtest.itheima.net/'
const backURL = 'http://127.0.0.1:5173/paycallback'
const redirectUrl = encodeURIComponent(backURL)
const payUrl = `${baseURL}pay/aliPay?orderId=${route.query.id}&redirect=${redirectUrl}`
```

```html
<div class="item">
  <p>支付平台</p>
  <a class="btn wx" href="javascript:;"></a>
  <a class="btn alipay" :href="payUrl"></a>
</div>
```

支付宝账号: 
askgxl8276@sandbox.com
登录密码: 111111
支付密码: 111111





# 部署方法

## PostgreSQL环境配置

```bash
sudo apt install postgresql postgresql-contrib libecpg-dev
systemctl status postgresql
psql --version

sudo cat /etc/shadow
sudo passwd postgres
su postgres -c psql
ALTER USER postgres WITH PASSWORD '123456';

sudo vi /etc/postgresql/14/main/pg_hba.conf
# Database administrative login by Unix domain socket
local  all  postgres  peer -> md5
sudo systemctl reload postgresql

psql -U postgres -W

CREATE USER ethan WITH PASSWORD '123456' SUPERUSER;
CREATE DATABASE ethan OWNER ethan;
psql
```


## vue环境配置

```bash
git clone https://github.com/Invisiphantom/vue-project.git
cd vue-project
npm install
npm run dev
```