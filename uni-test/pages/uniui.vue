<template>
	<view class="container">
		<view class="item" v-for="(value,index) in iconType" :key="index">
		    <icon :type="value" size="26"/>
		    <text>{{value}}</text>
		</view>
	</view>
</template>

<script>
	export default {
	    data() {
	        return {
	            iconType: ['success']
	        }
	    },
	    onLoad() {
	        // #ifdef APP-PLUS|| MP-WEIXIN
	        this.iconType = ['success', 'success_no_circle', 'info', 'warn', 'waiting', 'cancel', 'download', 'search','clear']
	        // #endif
	        // #ifdef MP-ALIPAY
	        this.iconType = ['info', 'warn', 'waiting', 'cancel', 'download', 'search', 'clear', 'success', 'success_no_circle', 'loading']
	        // #endif
	        // #ifdef MP-BAIDU
	        this.iconType = ['success', 'info', 'warn', 'waiting', 'success_no_circle', 'clear', 'search', 'personal', 'setting', 'top', 'close', 'cancel', 'download', 'checkboxSelected', 'radioSelected', 'radioUnselect']
	        // #endif
	    }
	}
</script>

<style>
</style>
