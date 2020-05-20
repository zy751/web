<template>
	<view class="container" >
		<view v-if="!islogin">
			<text>用户名:</text><input  type="text" v-model="username" placeholder="请输入用户名" />
			<text>密码:</text><input v-model="pwd" password="true" placeholder="请输入密码"/>
			<button type="primary" @click="checkdata">登录</button>
			<!-- #ifdef MP-WEIXIN -->
				<button open-type="getUserInfo" @getuserinfo="getUserInfo" type="primary">微信登录</button>
				<button @click="loginV" type="primary">游客登录</button>
			<!-- #endif -->
			<!-- #ifdef APP-PLUS -->
				<button type="warn" open-type='getUserInfo' @tap="wxLogin">微信登录</button>
			<!-- #endif -->
			
		</view>
		<view v-else>
			<view>{{username}}</view>
			<button type="primary" @click="backtoindex">返回首页</button>
			<button type="warn" @click="resetL">注销</button>
		</view>
	</view>
</template>

<script>
		export default{
			data(){
				return {
					pwd:'',
					username:'',
					islogin:false
				}
			},
			onShow() {
				this.islogin=global.isLogin()&&true
				if(this.islogin){
					this.username=global.isLogin().username
				}
			},
			methods:{
				loginV(){
					uni.navigateTo({
						url:'index/index'
					})
				},
				wxLogin(){
					uni.getProvider({
						service:'oauth',
						success(res) {
							if(res.provider.indexOf('weixin')>-1){
								uni.login({
									provider:'weixin',
									success(Loginres) {
										uni.getUserInfo({
											provider:'weixin',
											success(getres) {
												uni.setStorage({
													key:'userinfo',
													data:{
														username:getres.userInfo.nickName,
														imageSrc:getres.userInfo.avatarUrl
													}
												})
												uni.navigateTo({
													url:'index/index'
												})
											}
										})
										
									}
								})
							}
						}
					})
				},
				backtoindex(){
					uni.navigateTo({
						url:'./index/index'
					})
				},
				getUserInfo(res){
					if(!res.detail.iv){
						uni.showToast({
							title:'未授权，登录失败',
							icon:'none'
						})
						return
					}
					uni.login({
						provider:'weixin',
						success(Loginres) {
							if(Loginres.code){
								var APPID='wx2a8b288dba2fad3c'
								var SECRET='2a6c99a14fd8d8044c2ff40ff5f94289'
								var JSCODE=Loginres.code
								uni.request({
									url:`https://api.weixin.qq.com/sns/jscode2session?appid=${APPID}&secret=${SECRET}&js_code=${JSCODE}&grant_type=authorization_code`,
									success(urlres) {
										uni.setStorage({
												key:'userinfo',
												data:{
													username:res.detail.userInfo.nickName,
													imageSrc:res.detail.userInfo.avatarUrl
												}
											})
											uni.navigateTo({
												url:'/pages/index/index'
											})
									}
								})
							}
						}
					})

				},
				resetL(){
					console.log(plus.oauth.AuthService)
					plus.storage.clear()
					uni.clearStorage()
					uni.reLaunch({
						url:'./audioplay'
					})
				},
				checkdata(){
					if(this.username.length<1){
						uni.showToast({
							icon:'none',
							title:'请输入用户名'
						})
						return
					}else if(this.pwd.length<1){
						uni.showToast({
							icon:'none',
							title:'请输入密码'
						})
						return
					}
					else if(this.username==='zy'&&this.pwd==='1234'){
						uni.setStorage({
							key:'userinfo',
							data:{
								username:this.username
							}
						})
						uni.navigateTo({
							url:'/pages/index/index'
						})
					}
					else{
						uni.showToast({
							icon:'none',
							title:'用户名或密码错误'
						})
					}
			}
		},
		}
</script>

<style>
</style>
