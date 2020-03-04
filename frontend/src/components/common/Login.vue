<template>
<div id="login">
  <h1>Login!</h1>
  <div class="form-wrapper">
    <form @submit.prevent="handleSubmit">
      <label>Email</label>
        <input 
      placeholder="email"
      name="email"
      v-model="data.email"
      type="text"
      />
      <label>Password</label>
        <input 
      placeholder="password"
      name="password"
      v-model="data.password"
      type="password"
      />
      <label>Confirm your password</label>
        <input 
      placeholder="password confirmation"
      name="password_confirmation"
      v-model="data.password_confirmation"
      type="password"
      />
      <button type="submit" class="form=button">Submit</button>
    </form>
  </div>
</div>
  
</template>

<script>

import axios from 'axios'

export default {
  name: "login",
  data() {
    return {
      data: {},
    }
  },

  methods: {

    async handleSubmit() {
      console.log(this.data)
      try {
        await axios.post('/api/login', this.data)
        this.$router.push('/profile')
      }
      catch(err) {
        console.log(err)
      }
    },

  }
  
}
</script>
<style scoped>

</style>