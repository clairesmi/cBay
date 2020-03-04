<template>
<div id="register">
  <h1>Sign Up!</h1>
  <div class="form-wrapper">
    <form @submit.prevent="handleSubmit">
      <label>Username</label>
      <input 
      placeholder="username"
      name="username"
      v-model="data.username"
      type="text"
      />
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
  name: "register",
  data() {
    return {
      data: {
        username: '',
        email: '',
        password: '',
        password_confirmation: ''
      },
    }
  },

  methods: {

    async handleSubmit() {
      console.log(this.data)
      try {
        await axios.post('/api/register', this.data)
        this.$router.push('/login')
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