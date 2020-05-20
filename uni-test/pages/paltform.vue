<template>
	<view class="container">
		<!--#ifdef MP-WEIXIN -->
		<view>wxin</view>
		<button type="primary" @click="choose">Choose hobbit</button>
		<text>你的爱好是{{hobbit}}</text>
		<!--#endif -->
		
		<!--#ifdef APP-PLUS -->
		<view>H5</view>
		<!--#endif -->
		<view>哈哈</view>
	</view>
</template>

<script>
	export default{
		data(){
			return {
				hobbit:'',
				itemList:['唱歌','跳舞','喝茶']
			}
		},
		methods:{
			choose(){
				var _self=this
				uni.showActionSheet({
					itemList:['唱歌','跳舞','喝茶'],
					success(res) {
						_self.hobbit=_self.itemList[res.tapIndex]
						// _self.hobbit=res.
					}
				})
			}
		}
	}
</script>

<style>
</style>
