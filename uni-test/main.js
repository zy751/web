import Vue from 'vue'
import App from './App'
import common from './common/common.js'

Vue.config.productionTip = false
Vue.prototype.$common=common//使得可以直接使用在common里的全局变量
App.mpType = 'app'

const app = new Vue({
	...App
})
app.$mount()
