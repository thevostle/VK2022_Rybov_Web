<template>
  <div class="productShowcase">
    <productItem v-for="item of items" v-bind:item="item" :key="item.id" v-on:addToCart="addToCart" />
  </div>
</template>

<script>
import productItem from '@/components/productItem';

export default {
  props: ['items'],
  components: {
    productItem,
  },
  methods: {
    addToCart(id) {
      this.$emit('addToCart', id);
    }
  }
};
</script>

<style>
    .productShowcase {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 2rem;
        margin-bottom: 3rem;
    }
</style>