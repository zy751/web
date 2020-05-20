<template>
<div>
  <btn msg="确定" @clickEvent="doSth"><img style="height: 17px;width: 40px"  src="../../static/image/u=3626190683,2368952123&fm=15&gp=0.jpg" slot="icon"></btn>
  <btn msg="取消" @clickEvent="doSth2"></btn>
</div>
</template>

<script>
import btn from '../components/btn'
export default {
  name: 'pagebtn',
  components: { 'btn': btn },
  methods: {
    doSth: function () {
      alert('hi')
    },
    doSth2: function () {
      alert('no')
    }
  }
}
</script>

<style scoped>
button{
 float: left;
 margin: 10px;
}
  img{
    margin: 0;
    padding: 0;
  }
</style>
