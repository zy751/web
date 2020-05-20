<template>
	<view class="container">
		<view v-if="!msg">
			<image :src="imagesrc" style="width: 50%;" mode="aspectFit"></image>
		</view>
		<view v-else>
			<text style="color: #FF0000;">{{msg}}</text>
		</view>
		<view v-for="(path,index) in tempFilePaths" :key=index>{{path}}</view>
		<button type="primary" @click="chooseImage">选择图片</button>
		<button @click="previewImage" type="primary">预览图片</button>
	</view>
</template>

<script>
	var _self
	export default{
		data(){
			return {
				msg:'',
				imagesrc:'',
				percent:0,
				tempFilePaths:[],				
			}
		},
		onLoad() {
			_self=this
			this.imagesrc=uni.getStorageSync('userinfo').imageSrc
			if(!(this.imagesrc)){
				this.msg='未微信登录，获得不到你的图像'
				console.log(this.msg&&true)
				}
			console.log(this.imagesrc)
		},
		methods:{
			chooseImage(){
				uni.chooseImage({
					count:2,
					sizeType:['processed'],
					success(res) {
						_self.tempFilePaths=res.tempFilePaths
					}
				})
			},
			previewImage(){
				uni.previewImage({
					urls:_self.tempFilePaths,
					
				})
			}
		}
	}
</script>

<style>
</style>
