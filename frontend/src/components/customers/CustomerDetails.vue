<template>
  <dialog open>
    <header>
      <h1>{{ customerName }}</h1>
    </header>
    <p>{{ customerDescription }}</p>
    <button @click="$emit('hide-details', true)">Return to list</button>
  </dialog>
</template>

<script>
export default {
  props: {
    customerName: {
      type: String,
      required: true,
    },
    customerDescription: {
      type: String,
      required: false,
    },
  },
  emits: ["hide-details"],
};
</script>

<style></style>
