# 3-1 需求分析及整体结构创建
![](https://cdn.nlark.com/yuque/0/2023/png/274425/1675417667651-eb841c73-5b36-48a5-a8ee-118dbeaaeb0d.png =400x)

- HomeCategory
- HomeBanner
- HomeNew
- HomeHot
- HomeProduct

Home/index.vue
```vue
<script setup>
import HomeCategory from "@/views/Home/components/HomeCategory.vue"
import HomeBanner from "@/views/Home/components/HomeBanner.vue"
import HomeNew from "@/views/Home/components/HomeNew.vue"
import HomeHot from "@/views/Home/components/HomeHot.vue"
import HomeProduct from "@/views/Home/components/HomeProduct.vue"
</script>

<template>
  <div class="container">
    <HomeCategory />
    <HomeBanner />
  </div>
  <HomeNew/>
  <HomeHot/>
  <HomeProduct/>
</template>
```

# 3-2-实现Category左侧分类

HomeCategory.vue
```vue
<script setup>
import {useCategoryStore} from "@/stores/categoryStore"
const categoryStore = useCategoryStore()
</script>

<template>
  <div class="home-category">
    <ul class="menu">
      <li v-for="item in categoryStore.categoryList" :key="item.id">
        <RouterLink to="/">{{item.name}}</RouterLink>
        <RouterLink v-for="i in item.children.slice(0,2)" :key="i.id" to="/">{{i.name}}</RouterLink>
        <!-- 弹层layer位置 -->
        <div class="layer">
          <h4>分类推荐 <small>根据您的购买或浏览记录推荐</small></h4>
          <ul>
            <li v-for="i in item.goods" :key="i.id">
              <RouterLink to="/">
                <img alt="" :src="i.picture" />
                <div class="info">
                  <p class="name ellipsis-2">{{i.name}}</p>
                  <p class="desc ellipsis">{{i.desc}}</p>
                  <p class="price"><i>¥</i>{{i.price}}</p>
                </div>
              </RouterLink>
            </li>
          </ul>
        </div>
      </li>
    </ul>
  </div>
</template>


<style scoped lang='scss'>
.home-category {
  width: 250px;
  height: 500px;
  background: rgba(0, 0, 0, 0.8);
  position: relative;
  z-index: 99;

  .menu {
    li {
      padding-left: 40px;
      height: 55px;
      line-height: 55px;

      &:hover {
        background: $xtxColor;
      }

      a {
        margin-right: 4px;
        color: #fff;

        &:first-child {
          font-size: 16px;
        }
      }

      .layer {
        width: 990px;
        height: 500px;
        background: rgba(255, 255, 255, 0.8);
        position: absolute;
        left: 250px;
        top: 0;
        display: none;
        padding: 0 15px;

        h4 {
          font-size: 20px;
          font-weight: normal;
          line-height: 80px;

          small {
            font-size: 16px;
            color: #666;
          }
        }

        ul {
          display: flex;
          flex-wrap: wrap;

          li {
            width: 310px;
            height: 120px;
            margin-right: 15px;
            margin-bottom: 15px;
            border: 1px solid #eee;
            border-radius: 4px;
            background: #fff;

            &:nth-child(3n) {
              margin-right: 0;
            }

            a {
              display: flex;
              width: 100%;
              height: 100%;
              align-items: center;
              padding: 10px;

              &:hover {
                background: #e3f9f4;
              }

              img {
                width: 95px;
                height: 95px;
              }

              .info {
                padding-left: 10px;
                line-height: 24px;
                overflow: hidden;

                .name {
                  font-size: 16px;
                  color: #666;
                }

                .desc {
                  color: #999;
                }

                .price {
                  font-size: 22px;
                  color: $priceColor;

                  i {
                    font-size: 16px;
                  }
                }
              }
            }
          }
        }
      }

      // 关键样式  hover状态下的layer盒子变成block
      &:hover {
        .layer {
          display: block;
        }
      }
    }
  }
}
</style>
```

# 3-3 实现Banner轮播图

apis/home.js
```javascript
import http from "@/utils/http"

// 获取轮播图数据
export function getBannerAPI(){
    return http.get('/home/banner')
}
```

HomeBanner.vue
```vue
<script setup>
import { getBannerAPI } from '@/apis/home'

const bannerList = ref([])

const getBanner = async () => {
  const res = await getBannerAPI()  
  bannerList.value = res.result
}
onMounted(() => getBanner())
</script>

<template>
  <div class="home-banner">
    <el-carousel height="500px">
      <el-carousel-item v-for="item in bannerList" :key="item.id">
        <img :src="item.imgUrl" alt="">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<style scoped lang='scss'>
.home-banner {
  width: 1240px;
  height: 500px;
  position: absolute;
  left: 0;
  top: 0;
  z-index: 98;

  img {
    width: 100%;
    height: 500px;
  }
}
</style>
```


# 3-4 实现新鲜好物

HomePanel.vue
```vue
<script setup>
defineProps({
  title: {
    type: String,
    default: ''
  },
  subTitle: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <div class="home-panel">
    <div class="container">

      <div class="head">
        <h3>{{ title }}<small>{{ subTitle }}</small></h3>
      </div>

      <slot/>

    </div>
  </div>
</template>

<style scoped lang='scss'>
.home-panel {
  background-color: #fff;

  .head {
    padding: 40px 0;
    display: flex;
    align-items: flex-end;

    h3 {
      flex: 1;
      font-size: 32px;
      font-weight: normal;
      margin-left: 6px;
      height: 35px;
      line-height: 35px;

      small {
        font-size: 16px;
        color: #999;
        margin-left: 20px;
      }
    }
  }
}
</style>
```

## 插槽数据渲染

### home.js
```js
// 获取人气推荐
export const getHotAPI = () => {
    return http.get('/home/hot')
}

// 获取新鲜好物
export const getNewAPI = () => {
    return http.get('/home/new')
}

// 获取产品列表
export const getGoodsAPI = () => {
    return http.get('/home/goods')
}
```

### HomeHot.vue
```vue
<script setup>
import HomePanel from "@/views/Home/components/HomePanel.vue"
import { getHotAPI } from '@/apis/home'
const hotList = ref([])
const getHotList = async () => {
  const res = await getHotAPI()  
  hotList.value = res.result
}
onMounted(()=>getHotList())
</script>

<template>
<HomePanel title="人气推荐" sub-title="人气爆款 不容错过">
  <ul class="goods-list">
    <li v-for="item in hotList" :key="item.id">
      <RouterLink to="/">
        <img :src="item.picture" alt="">
        <p class="name">{{ item.title }}</p>
        <p class="desc">{{ item.alt }}</p>
      </RouterLink>
    </li>
  </ul>
</HomePanel>
</template>

<style scoped lang='scss'>
.goods-list {
  display: flex;
  justify-content: space-between;
  height: 426px;

  li {
    width: 306px;
    height: 406px;
    transition: all .5s;

    &:hover {
      transform: translate3d(0, -3px, 0);
      box-shadow: 0 3px 8px rgb(0 0 0 / 20%);
    }

    img {
      width: 306px;
      height: 306px;
    }

    p {
      font-size: 22px;
      padding-top: 12px;
      text-align: center;
    }

    .desc {
      color: #999;
      font-size: 18px;
    }
  }
}
</style>
```

### HomeNew.vue
```vue
<script setup>
import HomePanel from "@/views/Home/components/HomePanel.vue"

import { getNewAPI } from '@/apis/home'
const newList = ref([])
const getNewList = async () => {
  const res = await getNewAPI()  
  newList.value = res.result
}
onMounted(()=>getNewList())
</script>

<template>
<HomePanel title="新鲜好物" sub-title="新鲜出炉 品质靠谱">
  <ul class="goods-list">
    <li v-for="item in newList" :key="item.id">
      <RouterLink :to="`/detail/${item.id}`">
        <img :src="item.picture" alt="" />
        <p class="name">{{ item.name }}</p>
        <p class="price">&yen{{ item.price }}</p>
      </RouterLink>
    </li>
  </ul>
</HomePanel>
</template>

<style scoped lang='scss'>
.goods-list {
  display: flex;
  justify-content: space-between;
  height: 406px;

  li {
    width: 306px;
    height: 406px;
    background: whitesmoke;
    transition: all .5s;

    &:hover {
      transform: translate3d(0, -3px, 0);
      box-shadow: 0 3px 8px rgb(0 0 0 / 20%);
    }

    img {
      width: 306px;
      height: 306px;
    }

    p {
      font-size: 22px;
      padding-top: 12px;
      text-align: center;
      text-overflow: ellipsis;
      overflow: hidden;
      white-space: nowrap;
    }

    .price {
      color: $priceColor;
    }
  }
}
</style>
```

### HomeProduct.vue
```vue
<script setup>
import HomePanel from './HomePanel.vue'
import { getGoodsAPI } from '@/apis/home'

const goodsProduct = ref([])
const getGoods = async () => {
  const { result } = await getGoodsAPI()
  goodsProduct.value = result
}
onMounted( ()=> getGoods() )
</script>

<template>
  <div class="home-product">
    <HomePanel v-for="cate in goodsProduct" :title="cate.name"  :key="cate.id">
      <div class="box">
        <RouterLink class="cover" to="/">
          <img v-img-lazy="cate.picture" />
          <strong class="label">
            <span>{{ cate.name }}馆</span>
            <span>{{ cate.saleInfo }}</span>
          </strong>
        </RouterLink>
        <ul class="goods-list">
          <li v-for="good in cate.goods" :key="good.id">
            <RouterLink to="/" class="goods-item">
              <GoodsItem :good="good"></GoodsItem>
            </RouterLink>
          </li>
        </ul>
      </div>
    </HomePanel>
  </div>
</template>


<style scoped lang='scss'>
.home-product {
  background: #fff;
  margin-top: 20px;

  hr {
    margin: 0;
    border: none;
    border-top: 4px solid #F5F5F5;
  }

  .box {
    display: flex;

    .cover {
      width: 240px;
      height: 610px;
      margin-right: 10px;
      position: relative;

      .cat-img {
        width: 240px;
        height: 240px;
        margin-top: 20px;
        overflow: hidden;

        img {
          width: 100%;
          height: auto;
          object-fit: cover;
        }
      }

      .label {
        width: 188px;
        height: 66px;
        display: flex;
        font-size: 18px;
        color: #fff;
        line-height: 66px;
        font-weight: normal;
        position: absolute;
        left: 0;
        top: 50%;
        transform: translate3d(0, -50%, 0);

        span {
          text-align: center;

          &:first-child {
            width: 76px;
            background: rgba(0, 0, 0, 0.9);
          }

          &:last-child {
            flex: 1;
            background: rgba(0, 0, 0, 0.7);
          }
        }
      }
    }

    .goods-list {
      width: 990px;
      display: flex;
      flex-wrap: wrap;

      li {
        width: 240px;
        height: 300px;
        margin-right: 10px;
        margin-bottom: 10px;

        &:nth-last-child(-n + 4) {
          margin-bottom: 0;
        }

        &:nth-child(4n) {
          margin-right: 0;
        }
      }
    }

  }
}
</style>
```