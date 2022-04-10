<template>
  <div id="app">
    <div>
      <h1>Магазин</h1>
      <productShowcase v-bind:items="items" @addToCart="addToCart" />
      <shoppingCart v-bind:items="itemsInCart" @removeItem="removeItem" />
    </div>
  </div>
</template>

<script>
import productShowcase from "@/components/productShowcase";
import shoppingCart from "@/components/shoppingCart";
import axios from "axios";

export default {
  name: "App",
  components: {
    productShowcase,
    shoppingCart
  },
  data() {
    return {
      items: [],
      itemsInCart: []
    };
  },
  methods: {
    getItems() {
      const path = "http://127.0.0.1:5000/shop";
      axios.get(path).then(res => {
        this.items = res.data.items;
      });
    },
    addToCart(id) {
      this.itemsInCart.push({ id: id });
    },
    removeItem(id) {
      this.itemsInCart = this.itemsInCart.filter(t => t.id !== id);
    }
  },
  created() {
    this.getItems();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1 {
  margin-bottom: 3rem;
}
</style>
