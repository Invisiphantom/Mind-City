import GoodsItem from './GoodsItem/index.vue'
import ImageView from './ImageView/index.vue'
import Sku from './Sku/index.vue'
export const componentPlugin = {
    install(app) {
        app.component('GoodsItem', GoodsItem)
        app.component('ImageView', ImageView)
        app.component('Sku', Sku)
    }
}