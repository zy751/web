<template>
	<view class="container">
		<view v-for="(item,index) in list" :key="index">{{item}}</view>
		<text @click="pushList">{{msg}}</text>
	</view>
</template>

<script>
	var _self,timer
	export default{
		data(){
			var list=new Array(40).fill(Math.floor(Math.random()*100))
			return{
				msg:'加载更多',
				list:list,
				num:0,
				NEW:['aha','heihei','hello']
			}
		},
		onLoad() {
			_self=this
			
		},
		onPullDownRefresh() {
			this.refreshList()
		},
		onReachBottom() {
			if(timer!=null){
				clearTimeout(timer)
			}
			timer=setTimeout(function(){_self.pushList()},1000)	
		},
		methods:{
			refreshList(){
				_self.num++
				_self.list=['hello'+_self.num]
				uni.stopPullDownRefresh()
			},
			pushList(){
				if(_self.msg==='加载完毕'){
					return false
				}
				_self.msg='加载中'
				console.log(_self.msg)
				uni.showNavigationBarLoading()
				if(_self.num>10){
					_self.msg='加载完毕'
					console.log(_self.msg)
					uni.hideNavigationBarLoading()
					return false
				}
				_self.list.push(_self.num++)
				uni.hideNavigationBarLoading()
				_self.msg='加载更多'
				console.log(_self.msg)
			}
		}
		
	}
</script>

<style>
</style>
