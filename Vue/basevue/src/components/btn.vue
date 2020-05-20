<template>
    <button class="qui-btn" @click="$emit('clickEvent')">
    <slot name="icon"></slot>
      {{msg}}
    </button>
</template>

<script>
export default {
  name: 'btn',
  props: {
    msg: {
      default: '下载'
    }
  },
  methods: {
    btnClick: function () {
      alert(this.msg)
    }
  }
}
</script>

<style scoped>

</style>
